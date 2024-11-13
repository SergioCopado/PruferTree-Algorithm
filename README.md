# PruferTree: Algorithm for Generating and Decoding Prüfer Codes
This project implements a set of Python functions to work with Prüfer codes, a sequence that uniquely represents a labeled tree. The goal is to enable encoding and decoding of trees using their Prüfer code—a useful tool in graph theory and data structures.

## Features
The project includes:

Tree to Prüfer Code Conversion: Given a tree, it generates the Prüfer code sequence representing its structure.
Prüfer Code to Tree Conversion: Constructs the corresponding tree from a Prüfer code sequence.
Auxiliary Tree and Heap Functions: Includes classes for representing trees and heaps, facilitating node management and efficient data handling.

## Project Structure
The project is organized into three main modules:

1. main.py: Contains the primary logic, allowing users to interact with functions to convert between trees and Prüfer codes, as well as to create trees and handle input.
2. Tree.py: Defines a Tree class for tree representation, with methods to add children, traverse, and perform various tree operations.
3. Heap.py: Defines a Heap class to implement a min-heap, which is necessary for efficiently managing leaf nodes in the tree-to-Prüfer code conversion algorithm.
