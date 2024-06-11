#pragma once

#include "pch.h"

template <typename T>
struct Action {

};

template <typename T>
struct PathCost {

};

template <typename T>
struct State {

};

template <typename T>
struct Problem {
  State<T> initial_state;
  static std::vector<Action<T>> Actions(State<T> par_state);
  static State<T> Result(State<T> par_state, Action<T> par_action);
  static bool GoalTest(State<T> par_state);
  static PathCost<T> C(State<T> par_state, Action<T> par_action, State<T> par_state_p);
};

template <typename T>
struct Node {
  State<T> state;
  Node<T>* parent;
  Action<T> action;
  PathCost<T> path_cost;
};
