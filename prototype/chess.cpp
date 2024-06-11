#include "pch.h"

#include "search.h"

struct Chess {};

enum Player : uint8_t {
  White = 0,
  Black,
  PlayerCount
};

enum Piece : uint8_t {
  ___ = 0,

  W_P,
  W_N,
  W_B,
  W_R,
  W_Q,
  W_K,

  B_P,
  B_N,
  B_B,
  B_R,
  B_Q,
  B_K,

  W_FIRST = W_P,
  W_LAST = W_K,

  B_FIRST = B_P,
  B_LAST = B_K,
};

enum Space {
  A1,
  A2,
  A3,
  A4,
  A5,
  A6,
  A7,
  A8,

  B1,
  B2,
  B3,
  B4,
  B5,
  B6,
  B7,
  B8,

  C1,
  C2,
  C3,
  C4,
  C5,
  C6,
  C7,
  C8,

  D1,
  D2,
  D3,
  D4,
  D5,
  D6,
  D7,
  D8,

  E1,
  E2,
  E3,
  E4,
  E5,
  E6,
  E7,
  E8,

  F1,
  F2,
  F3,
  F4,
  F5,
  F6,
  F7,
  F8,

  G1,
  G2,
  G3,
  G4,
  G5,
  G6,
  G7,
  G8,

  H1,
  H2,
  H3,
  H4,
  H5,
  H6,
  H7,
  H8,

  SpaceCount
};

struct Coord {
  Coord(Space par_space) : c(par_space / 8), r(par_space % 8) {}
  Coord(int8_t par_c, int8_t par_r) : c(par_c), r(par_r) {}

  int8_t c, r;

  operator Space () const { return Space(8*c + r ); }
};

void ForEachSpace(std::function<void(Space)> par_function) {
  for (int i = 0; i < SpaceCount; ++i)
    par_function(Space(i));
}

Player ToPlayer(Piece par_piece) {
  assert(par_piece != ___);

  return (par_piece <= W_LAST) ? White : Black;
}

template <>
struct Action<Chess> {
  Action() { *this = Checkmate; }
  Action(Space par_orig, Space par_dest, Piece par_promotion = ___)
    : orig(par_orig), dest(par_dest), promotion(par_promotion) {}

  bool operator==(const Action<Chess>& par_rhs) const {
    return orig == par_rhs.orig && dest == par_rhs.dest && promotion == par_rhs.promotion;
  }

  Space orig, dest;
  Piece promotion;

  static const Action Checkmate;
};

const Action<Chess> Action<Chess>::Checkmate = { A1, A1, ___ };

template <> struct State<Chess> {
  State() {
    board = { ___ };
    board[A2] = board[B2] = board[C2] = board[D2] = board[E2] = board[F2] = board[G2] = board[H2] = W_P;
    board[B1] = board[G1] = W_N;
    board[C1] = board[F1] = W_B;
    board[A1] = board[H1] = W_R;
    board[D1] = W_Q;
    board[E1] = W_K;

    board[A7] = board[B7] = board[C7] = board[D7] = board[E7] = board[F7] = board[G7] = board[H7] = B_P;
    board[B8] = board[G8] = B_N;
    board[C8] = board[F8] = B_B;
    board[A8] = board[H8] = B_R;
    board[D8] = B_Q;
    board[E8] = B_K;

    king_space = { E1, E8 };
    king_moved = { false, false };
    rookA_moved = { false, false };
    rookH_moved = { false, false };
    check = false;
  }

  State& operator=(const State& par_state) {
    board = par_state.board;
    moves = par_state.moves;
    king_space = par_state.king_space;
    king_moved = par_state.king_moved;
    rookA_moved = par_state.rookA_moved;
    rookH_moved = par_state.rookH_moved;
    check = false;

    return *this;
  }

  std::array<Piece, SpaceCount> board;
  std::vector<Action<Chess>> moves;
  std::array<Space, PlayerCount> king_space;
  std::array<bool, PlayerCount> king_moved;
  std::array<bool, PlayerCount> rookA_moved;
  std::array<bool, PlayerCount> rookH_moved;
  bool check;
};

template <>
struct PathCost<Chess> {
  PathCost() {
    piece_weight = 1.f;
    child_count = 0;
    min_child_cost = 0.f;
    expanded = false;
  }
  PathCost(const State<Chess>& par_state) {
    const Player player = Player(par_state.moves.size() % 2);
    float w_pieces = 0.f;
    float b_pieces = 0.f;

    for (Piece piece : par_state.board) {
      switch (piece) {
      case W_P:
        w_pieces += 1;
        break;

      case W_N:
        w_pieces += 2;
        break;

      case W_B:
        w_pieces += 3;
        break;

      case W_R:
        w_pieces += 5;
        break;

      case W_Q:
        w_pieces += 9;
        break;

      case B_P:
        b_pieces += 1;
        break;

      case B_N:
        b_pieces += 2;
        break;

      case B_B:
        b_pieces += 3;
        break;

      case B_R:
        b_pieces += 5;
        break;

      case B_Q:
        b_pieces += 9;
        break;

      default:
        break;
      }
    }

    piece_weight = player == White ? (w_pieces / b_pieces) : (b_pieces / w_pieces);
    child_count = 0;
    min_child_cost = 0.f;
    expanded = false;
  }

  operator float () const {
    if (not expanded)
      return piece_weight;

    if (child_count == 0)
      return 0;

    return 1.f / min_child_cost;
  }

  float piece_weight = 1.f;
  size_t child_count = 0;
  float min_child_cost = 0.f;
  bool expanded = false;
};

void ForEachSpaceHorizontalAndVertical(const std::function<void(Space)>& par_function, const std::array<Piece, SpaceCount>& par_board, Space par_space) {
  const Coord coord(par_space);

  for (int8_t h = -1; h <= 1; h += 1) {
    for (int8_t v = -1; v <= 1; v += 1) {
      if (std::abs(h) + std::abs(v) != 1)
        continue;

      for (Coord dest = { int8_t(coord.c + h), int8_t(coord.r + v) }; 0 <= dest.c && dest.c < 8 && 0 <= dest.r && dest.r < 8; dest.c += h, dest.r += v) {
        const Space space = dest;

        par_function(space);

        if (par_board[space] != ___)
          break;
      }
    }
  }
}

void ForEachSpaceDiagonal(const std::function<void(Space)>& par_function, const std::array<Piece, SpaceCount>& par_board, Space par_space) {
  const Coord coord(par_space);

  for (int8_t h = -1; h <= 1; h += 2) {
    for (int8_t v = -1; v <= 1; v += 2) {
      for (Coord dest = { int8_t(coord.c + h), int8_t(coord.r + v) }; 0 <= dest.c && dest.c < 8 && 0 <= dest.r && dest.r < 8; dest.c += h, dest.r += v) {
        const Space space = dest;

        par_function(space);

        if (par_board[space] != ___)
          break;
      }
    }
  }
}

void ForEachSpaceL(const std::function<void(Space)>& par_function, Space par_space) {
  const Coord coord(par_space);

  for (int8_t c = -2; c <= 2; ++c) {
    for (int8_t r = -2; r <= 2; ++r) {
      if (std::abs(c) + std::abs(r) != 3)
        continue;

      if (coord.c + c < 0 || coord.c + c >= 8
        || coord.r + r < 0 || coord.r + r >= 8)
        continue;

      const Space space = Coord(coord.c + c, coord.r + r);
      par_function(space);
    }
  }
}

void PawnActions(std::vector<Action<Chess>>& par_actions, const State<Chess>& par_state, Space par_space) {
  const Coord coord(par_space);
  const Player player = Player(par_state.moves.size() % 2);
  const auto& board = par_state.board;
  const int8_t v = player == White ? 1 : -1;
  const int8_t r_final = player == White ? 7 : 0;
  const int8_t r_start = player == White ? 1 : 6;
  const int8_t r_en_pessant = player == White ? 4 : 3;

  const Space space_forward_1 = Coord(coord.c, coord.r + v);

  if (board[space_forward_1] == ___) {
    if (coord.r + v == r_final) {
      par_actions.emplace_back(par_space, space_forward_1, player == White ? W_N : B_N);
      par_actions.emplace_back(par_space, space_forward_1, player == White ? W_B : B_B);
      par_actions.emplace_back(par_space, space_forward_1, player == White ? W_R : B_R);
      par_actions.emplace_back(par_space, space_forward_1, player == White ? W_Q : B_Q);
    }
    else {
      par_actions.emplace_back(par_space, space_forward_1);
    }

    if (coord.r == r_start) {
      const Space space_forward_2 = Coord(coord.c, coord.r + 2*v);

      if (board[space_forward_2] == ___) {
        par_actions.emplace_back(par_space, space_forward_2);
      }
    }
  }

  for (int8_t h = -1; h <= 1; h += 2) {
    const Coord diag = Coord(coord.c + h, coord.r + v);
      
    if (0 <= diag.c && diag.c < 8) {
      const Space space_diag = Coord(coord.c + h, coord.r + v);
      const Piece piece_diag = board[space_diag];

      if (piece_diag != ___ && ToPlayer(piece_diag) != player) {
        par_actions.emplace_back(par_space, space_diag);
      }

      if (coord.r == r_en_pessant) {
        const Space space_side = Coord(coord.c + h, coord.r);
        const Piece piece_side = board[space_side];

        if ((piece_side == W_P || piece_side == B_P) && ToPlayer(piece_side) != player) {
          const Action<Chess> last_move = par_state.moves.back();
          const Coord last_move_orig(last_move.orig);
          const Coord last_move_dest(last_move.dest);

          if (last_move.dest == space_side && last_move_orig.r - last_move_dest.r == 2) {
            par_actions.emplace_back(par_space, space_diag);
          }
        }
      }
    }
  }
}

void KnightActions(std::vector<Action<Chess>>& par_actions, const State<Chess>& par_state, Space par_space) {
  const Player player = Player(par_state.moves.size() % 2);
  const auto& board = par_state.board;

  ForEachSpaceL([&](Space par_space_dest) {
    const Piece piece_dest = board[par_space_dest];

    if (piece_dest == ___ || ToPlayer(piece_dest) != player) {
      par_actions.emplace_back(par_space, par_space_dest);
    }
  }, par_space);
}

void BishopActions(std::vector<Action<Chess>>& par_actions, const State<Chess>& par_state, Space par_space) {
  const Player player = Player(par_state.moves.size() % 2);
  const auto& board = par_state.board;

  ForEachSpaceDiagonal([&](Space par_space_dest) {
    const Piece piece_dest = board[par_space_dest];

    if (board[par_space_dest] == ___ || ToPlayer(piece_dest) != player) {
      par_actions.emplace_back(par_space, par_space_dest);
    }
  }, par_state.board, par_space);
}

void RookActions(std::vector<Action<Chess>>& par_actions, const State<Chess>& par_state, Space par_space) {
  const Coord coord(par_space);
  const Player player = Player(par_state.moves.size() % 2);
  const auto& board = par_state.board;

  ForEachSpaceHorizontalAndVertical([&](Space par_space_dest) {
    const Piece piece_dest = board[par_space_dest];

    if (board[par_space_dest] == ___ || ToPlayer(piece_dest) != player) {
      par_actions.emplace_back(par_space, par_space_dest);
    }
  }, par_state.board, par_space);
}

void KingActions(std::vector<Action<Chess>>& par_actions, const State<Chess>& par_state, Space par_space) {
  const Coord coord(par_space);
  const Player player = Player(par_state.moves.size() % 2);
  const auto& board = par_state.board;

  for (int8_t h = -1; h <= 1; h += 1) {
    for (int8_t v = -1; v <= 1; v += 1) {
      if (h == 0 && v == 0)
        continue;

      const Coord dest = { int8_t(coord.c + h), int8_t(coord.r + v) };

      if (dest.c && dest.c < 8 && 0 <= dest.r && dest.r < 8) {
        const Space dest_space = dest;
        const Piece dest_piece = board[dest_space];

        if (dest_piece == ___ || ToPlayer(dest_piece) != player) {
          par_actions.emplace_back(par_space, dest_space);
        }
      }
    }
  }

  // Castling
  if (par_state.king_moved[player] == false) {
    // Kingside Castle
    if (par_state.rookH_moved[player] == false) {
      const bool no_pieces_between = (player == White) ? board[F1] == ___ && board[G1] == ___ : board[F8] == ___ && board[G8] == ___;

      if (no_pieces_between) {
        bool any_check = false;

        for (int i = 0; i < 3; ++i) {
          const Action<Chess> action = { par_space, Space(Coord(coord.c + i, coord.r)) };
          const State<Chess> state = Problem<Chess>::Result(par_state, action);
          if (state.check) {
            any_check = true;
            break;
          }
        }

        if (any_check == false) {
          par_actions.emplace_back(par_space, Space(Coord(coord.c + 2, coord.r)));
        }
      }
    }

    // Queenside Castle
    if (par_state.rookA_moved[player] == false) {
      const bool no_pieces_between = (player == White) ? board[B1] == ___ && board[C1] == ___ && board[D1] == ___ : board[B8] == ___ && board[C8] == ___ && board[D8] == ___;

      if (no_pieces_between) {
        bool any_check = false;

        for (int i = 0; i < 3; ++i) {
          const Action<Chess> action = { par_space, Space(Coord(coord.c - i, coord.r)) };
          const State<Chess> state = Problem<Chess>::Result(par_state, action);
          if (state.check) {
            any_check = true;
            break;
          }
        }

        if (any_check == false) {
          par_actions.emplace_back(par_space, Space(Coord(coord.c - 2, coord.r)));
        }
      }
    }
  }
}

bool IsCheckForPlayer(const std::array<Piece, SpaceCount>& par_board, Player par_player, Space par_king) {
  const Coord coord(par_king);
  bool check = false;

  ForEachSpaceHorizontalAndVertical([&](Space par_space) {
    const Piece piece = par_board[par_space];

    if (piece != ___ && ToPlayer(piece) != par_player) {
      if (piece == W_R || piece == B_R || piece == W_Q || piece == B_Q) {
        check = true;
        return;
      }

      if (piece == W_K || piece == B_K) {
        const Coord coord_king(par_space);

        if (std::abs(coord.c - coord_king.c) + std::abs(coord.r - coord_king.r) == 1) {
          check = true;
          return;
        }
      }
    }
  }, par_board, par_king);

  if (check) return check;

  ForEachSpaceDiagonal([&](Space par_space) {
    const Piece piece = par_board[par_space];

    if (piece != ___ && ToPlayer(piece) != par_player) {
      if (piece == W_B || piece == B_B || piece == W_Q || piece == B_Q) {
        check = true;
        return;
      }

      const Coord coord_piece(par_space);
      if (std::abs(coord.c - coord_piece.c) + std::abs(coord.r - coord_piece.r) == 2) {
        if (piece == W_K || piece == B_K) {
          check = true;
          return;
        }

        if (piece == W_P || piece == B_P) {
          if ((par_player == White && (coord_piece.r == coord.r + 1)) || (par_player == Black && (coord_piece.r == coord.r - 1))) {
            check = true;
            return;
          }
        }
      }
    }
  }, par_board, par_king);

  if (check) return check;

  ForEachSpaceL([&](Space par_space) {
    const Piece piece = par_board[par_space];

    if (piece != ___ && ToPlayer(piece) != par_player) {
      if (piece == W_N || piece == B_N) {
        check = true;
        return;
      }
    }
  }, par_king);

  return check;
}

template<> std::vector<Action<Chess>> Problem<Chess>::Actions(State<Chess> par_state) {
  std::vector<Action<Chess>> actions;
  const Player player = Player(par_state.moves.size() % 2);

  // For each board space
  ForEachSpace([&](Space par_space) {
    const auto& board = par_state.board;
    const Piece piece = board[par_space];

    // If piece controlled by current player
    if (piece != ___ && ToPlayer(piece) == player) {
      const Coord coord(par_space);

      switch (piece) {
      case W_P: 
      case B_P:
        PawnActions(actions, par_state, par_space);
        break;

      case W_N:
      case B_N:
        KnightActions(actions, par_state, par_space);
        break;

      case W_B:
      case B_B:
        BishopActions(actions, par_state, par_space);
        break;

      case W_R:
      case B_R:
        RookActions(actions, par_state, par_space);
        break;

      case W_Q:
      case B_Q:
        BishopActions(actions, par_state, par_space);
        RookActions(actions, par_state, par_space);
        break;

      case W_K:
      case B_K:
        KingActions(actions, par_state, par_space);
        break;

      default:
        assert(0);
      }
    }
  });

  return actions;
}

template<> State<Chess> Problem<Chess>::Result(State<Chess> par_state, Action<Chess> par_action) {
  State<Chess> state = par_state;

  const Coord orig = par_action.orig;
  const Coord dest = par_action.dest;
  const Piece piece_orig = par_state.board[par_action.orig];
  const Piece piece_dest = par_state.board[par_action.dest];
  const Player player = Player(par_state.moves.size() % 2);

  state.board[par_action.dest] = state.board[par_action.orig];
  state.board[par_action.orig] = ___;

  // En Pessant
  if ((piece_orig == W_P || piece_orig == B_P) && piece_dest == ___ && orig.c != dest.c) {
    const Space space_captured_pawn = Coord(dest.c, player == White ? dest.r - 1 : dest.r + 1);

    assert(state.board[space_captured_pawn] == (player == White ? B_P : W_P));
    state.board[space_captured_pawn] = ___;
  }

  // Castle
  if ((piece_orig == W_K || piece_orig == B_K) && std::abs(orig.c - dest.c) == 2) {
    switch (par_action.dest) {
    case C1:
      state.board[A1] = ___;
      state.board[D1] = W_R;
      break;

    case G1:
      state.board[H1] = ___;
      state.board[F1] = W_R;
      break;

    case C8:
      state.board[A8] = ___;
      state.board[D8] = B_R;
      break;

    case G8:
      state.board[H8] = ___;
      state.board[F8] = B_R;
      break;
    }
  }

  // Promotion
  if ((piece_orig == W_P && dest.r == 7) || (piece_orig == B_P && dest.r == 0)) {
    state.board[par_action.dest] = par_action.promotion;
  }

  state.moves.push_back(par_action);

  if (piece_orig == W_K) {
    state.king_space[White] = par_action.dest;
    state.king_moved[White] = true;
  }
  if (piece_orig == B_K) {
    state.king_space[Black] = par_action.dest;
    state.king_moved[Black] = true;
  }
  if (par_action.orig == A1) state.rookA_moved[White] = true;
  if (par_action.orig == A8) state.rookA_moved[Black] = true;
  if (par_action.orig == H1) state.rookH_moved[White] = true;
  if (par_action.orig == H8) state.rookH_moved[Black] = true;

  // Check
  const Space king_space = state.king_space[player];
  state.check = IsCheckForPlayer(state.board, player, king_space);

  return state;
}

template<> bool Problem<Chess>::GoalTest(State<Chess> par_state) {
  assert(0);
  return {};
}

template<> PathCost<Chess> Problem<Chess>::C(State<Chess> par_state, Action<Chess> par_action, State<Chess> par_state_p) {
  assert(0);
  return {};
}

template <> struct Node<Chess> {
  State<Chess> state;
  Node<Chess>* parent = nullptr;
  std::optional<Action<Chess>> action;
  std::vector<Node<Chess>*> children;
  PathCost<Chess> path_cost = {};
};

class ChessAgent {
public:
  ChessAgent() : root(nullptr) {}

  Action<Chess> operator()(Problem<Chess> par_problem) {
    Init(par_problem);

    return (*this)();
  }

  Action<Chess> operator()(std::vector<Action<Chess>> par_actions) {
    for (Action<Chess> action : par_actions) {
      assert(root != nullptr);
      auto it = std::find_if(root->children.begin(), root->children.end(), [&](Node<Chess>* par_node) { return par_node->action == action; });
      assert(it != root->children.end());
      Node<Chess>* new_root = *it;

      root->children.erase(it);
      for (Node<Chess>* child : root->children) {
        NodeDestruct(child);
      }

      root = new_root;
      root->parent = nullptr;
    }

    return (*this)();
  }

private:
  Action<Chess> operator()() {
    const float time_limit = 5.f;
    float time_elapsed = 0.f;

    const auto start_time = std::chrono::steady_clock::now();
    while (time_elapsed < time_limit) {
      if (Done())
        break;

      Think();

      const auto time = std::chrono::steady_clock::now();
      const auto duration = std::chrono::duration_cast<std::chrono::duration<float>>(time - start_time);
      time_elapsed = duration.count();
    }

    return Result();
  }

  bool Done() const {
    const bool root_expanded = root->path_cost.expanded;
    const float root_cost = root->path_cost;

    return root_expanded && (std::isinf(root_cost) || root_cost == 0.f);
  }

  void Init(Problem<Chess> par_problem) {
    root = NodeConstruct(par_problem.initial_state);
  }

  Action<Chess> Result() const {
    if (root->children.empty()) {
      return Action<Chess>::Checkmate;
    }

    auto it = std::ranges::min_element(root->children, [](Node<Chess>* par_lhs, Node<Chess>* par_rhs) {
      return par_lhs->path_cost < par_rhs->path_cost;
    });

    assert((*it)->action.has_value());
    return (*it)->action.value();
  }

  void Think() {
    Node<Chess>* node = root;
    while (node->path_cost.expanded == true) {
      node = *std::ranges::min_element(node->children, [](Node<Chess>* par_lhs, Node<Chess>* par_rhs) {
        return par_lhs->path_cost < par_rhs->path_cost;
      });
    }

    NodeExpand(node);
  }

  Node<Chess>* NodeConstruct(State<Chess> par_state, Node<Chess>* par_parent = nullptr, std::optional<Action<Chess>> par_action = {}) {
    Node<Chess>* node = new Node<Chess>;
    node->state = par_state;
    node->parent = par_parent;
    node->action = par_action;
    node->path_cost = PathCost<Chess>(par_state);

    return node;
  }

  void NodeDestruct(Node<Chess>* par_node) {
    if (par_node->path_cost.expanded) {
      for (Node<Chess>* child : par_node->children) {
        NodeDestruct(child);
      }
    }

    delete par_node;
  }

  void NodeExpand(Node<Chess>* par_node) {
    assert(par_node->path_cost.expanded == false);

    const std::vector<Action<Chess>> actions = Problem<Chess>::Actions(par_node->state);

    for (const Action<Chess>& action : actions) {
      const State<Chess> state = Problem<Chess>::Result(par_node->state, action);
      if (not state.check) {
        Node<Chess>* child = NodeConstruct(state, par_node, action);
        par_node->children.push_back(child);
      }
    }
    par_node->path_cost.expanded = true;

    UpdateTree(par_node);
  }

  void UpdateTree(Node<Chess>* par_node) {
    Node<Chess>* node = par_node;

    while (node != nullptr) {
      assert(node->path_cost.expanded);

      if (node->children.size() > 0) {
        node->path_cost.min_child_cost = (*std::ranges::min_element(node->children, [](Node<Chess>* par_lhs, Node<Chess>* par_rhs) {
          return par_lhs->path_cost < par_rhs->path_cost;
        }))->path_cost;

        if (node->path_cost.min_child_cost == 0.f) {
          for (Node<Chess>*& child : node->children) {
            if (child->path_cost != 0) {
              NodeDestruct(child);
              child = nullptr;
            }
          }

          std::erase(node->children, nullptr);
        }
      }
      node->path_cost.child_count = node->children.size();

      node = node->parent;
    }
  }

  Node<Chess>* root;
};

std::ostream& operator<<(std::ostream& par_ostream, Space par_space) {
  const Coord coord(par_space);

  par_ostream << (char)('A' + coord.c) << (char)('1' + coord.r);

  return par_ostream;
}

std::ostream& operator<<(std::ostream& par_ostream, const Action<Chess>& par_action) {
  par_ostream << par_action.orig << " " << par_action.dest;

  if (par_action.promotion != ___) {
    par_ostream << " (";
    switch (par_action.promotion) {
    case W_N:
    case B_N:
      par_ostream << "Knight";
      break;

    case W_B:
    case B_B:
      par_ostream << "Bishop";
      break;

    case W_R:
    case B_R:
      par_ostream << "Rook";
      break;

    case W_Q:
    case B_Q:
      par_ostream << "Queen";
      break;

    default:
      assert(0);
    }
    par_ostream << ")";
  }

  return par_ostream;
}

Action<Chess> ToAction(const std::string& par_orig, const std::string& par_dest) {
  const Coord orig(par_orig[0] - 'A', par_orig[1] - '1');
  const Coord dest(par_dest[0] - 'A', par_dest[1] - '1');

  return { orig, dest };
}

std::array<Piece, SpaceCount> Board(const std::array<Piece, SpaceCount>& par_board, Player par_player = White) {
  std::array<Piece, SpaceCount> board;

  const int8_t r_first = par_player == White ? 7 : 0;
  const int8_t c_first = par_player == White ? 0 : 7;
  const int8_t h = par_player == White ? 1 : -1;
  const int8_t v = par_player == White ? -1 : 1;

  for (int8_t i = 0, r = 0; r < 8; ++r) {
    for (int8_t c = 0; c < 8; ++c, ++i) {
      const Coord coord(c_first + h*c, r_first + v*r);
      const Space space = coord;

      board[space] = par_board[i];
    }
  }

  return board;
}

State<Chess> Blank() {
  State<Chess> state = {};
  state.board = Board({
    ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___
    });
  state.king_moved = { false, false };
  state.king_space = { E1, E8 };
  state.rookA_moved = { false, false };
  state.rookH_moved = { false, false };

  return state;
}

State<Chess> Puzzle1() {
  State<Chess> state = {};
  state.board = Board({
    B_R, ___, B_B, ___, ___, B_B, B_K, B_R,
    B_P, B_P, B_P, ___, ___, ___, B_P, B_P,
    ___, ___, B_N, ___, ___, ___, ___, ___,
    ___, ___, ___, B_Q, B_P, ___, ___, ___,
    ___, ___, W_B, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___,
    W_P, W_P, W_P, W_P, ___, W_P, W_P, W_P,
    W_R, W_N, W_B, ___, W_K, ___, ___, W_R
    });
  state.king_moved = { false, true };
  state.king_space = { E1, G8 };
  state.rookA_moved = { false, false };
  state.rookH_moved = { false, false };

  return state;
}

State<Chess> Puzzle2() {
  State<Chess> state = {};
  state.board = Board({
    B_R, B_N, ___, B_R, ___, ___, B_K, ___,
    ___, B_P, B_Q, ___, ___, B_P, ___, B_P,
    B_P, ___, ___, B_P, ___, B_B, B_P, W_B,
    ___, ___, ___, W_P, ___, ___, ___, ___,
    W_P, ___, ___, ___, W_Q, ___, ___, ___,
    ___, ___, W_P, W_B, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, W_P, W_P, W_P,
    ___, ___, W_R, ___, W_R, ___, W_K, ___
    });
  state.king_moved = { true, true };
  state.king_space = { G1, G8 };
  state.rookA_moved = { true, false };
  state.rookH_moved = { true, true };

  return state;
}

State<Chess> Puzzle3() {
  State<Chess> state = {};
  state.board = Board({
    ___, ___, ___, B_K, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, B_P, ___,
    ___, ___, ___, W_K, ___, B_P, W_P, B_P,
    ___, ___, ___, W_P, B_R, W_P, ___, ___,
    B_P, ___, ___, ___, ___, ___, ___, ___,
    W_P, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, W_Q, ___, ___, ___, W_P,
    ___, B_Q, ___, ___, ___, ___, ___, ___
    });
  state.king_moved = { true, true };
  state.king_space = { D6, D8 };
  state.rookA_moved = { true, true };
  state.rookH_moved = { true, true };

  return state;
}

State<Chess> Puzzle4() {
  State<Chess> state = {};
  state.board = Board({
    W_R, W_N, W_B, W_K, ___, W_B, W_N, W_R,
    W_P, W_P, W_P, ___, ___, W_P, W_P, W_P,
    ___, ___, ___, ___, ___, W_Q, ___, ___,
    ___, ___, ___, W_P, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, B_N, ___, ___,
    B_P, B_P, B_P, ___, B_P, B_P, B_P, B_P,
    B_R, B_N, B_B, B_K, B_Q, B_B, ___, B_R
    }, Black);
  state.king_moved = { false, false };
  state.king_space = { E1, E8 };
  state.rookA_moved = { false, false };
  state.rookH_moved = { false, false };
  state.moves = { { D4, C3 } };

  return state;
}

State<Chess> Puzzle5() {
  State<Chess> state = {};
  state.board = Board({
    ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, B_P, ___, B_K, ___, ___, B_P,
    B_P, ___, W_P, ___, ___, ___, ___, ___,
    ___, B_P, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, B_B, ___, ___, ___, ___,
    ___, ___, ___, ___, W_N, W_P, ___, ___,
    W_P, ___, ___, W_K, ___, ___, W_P, ___,
    ___, ___, ___, ___, ___, ___, ___, ___
    });
  state.king_moved = { true, true };
  state.king_space = { D2, E7 };
  state.rookA_moved = { true, true };
  state.rookH_moved = { true, true };

  return state;
}

State<Chess> Puzzle6() {
  State<Chess> state = {};
  state.board = Board({
    B_R, ___, B_B, B_Q, B_K, ___, ___, B_R,
    B_P, B_P, B_P, ___, ___, B_P, B_P, B_P,
    ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, B_P, W_P, ___, ___, ___,
    ___, B_B, ___, ___, B_N, ___, ___, ___,
    ___, ___, W_N, W_Q, ___, ___, ___, ___,
    W_P, W_P, W_P, ___, W_B, W_P, W_P, W_P,
    W_R, ___, W_B, ___, W_K, ___, ___, W_R
    });
  state.king_moved = { false, false };
  state.king_space = { E1, E8 };
  state.rookA_moved = { false, false };
  state.rookH_moved = { false, false };
  state.moves = { {}, { D7, D5 } };

  return state;
}

int main() {
  const Problem<Chess> problem = { Puzzle1() };
  ChessAgent agent = {};

  Action<Chess> action = agent(problem);

  while (true) {
    if (action == Action<Chess>::Checkmate) {
      std::cout << "Checkmate!" << std::endl;
      break;
    }
    else {
      std::cout << "Best Action: " << action << std::endl;
    }

    std::vector<Action<Chess>> actions;
    actions.resize(2);
    for (int i = 0; i < 2; ++i) {
      std::string orig, dest;
      std::cout << "Next Action: ";
      std::cin >> orig;
      std::cin >> dest;
      actions[i] = ToAction(orig, dest);
    }

    action = agent(actions);
  }

  return 0;
}
