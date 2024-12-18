# CS2 Fall 2024 Note 30

## Depth-first search

Depth-first search (DFS) is an algorithm for traversing or searching tree or
graph data structures.  The algorithm starts at the root node (selecting some
arbitrary node as the root node in the case of a graph) and explores as far as
possible along each branch before backtracking.  Extra memory, usually a stack,
is needed to keep track of the nodes discovered so far along a specified branch
which helps in backtracking of the graph.

Consider the graph below.

![a graph with seven nodes](pictures/dfs.svg)

If the algorithm starts at node A, explores neighbors in alphabetic order, never
visits a node twice, it will visit the nodes in this order: A, B, D, F, E, C, G.
