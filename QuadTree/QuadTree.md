QuadTree Implementation in Python
Overview
This repository contains a Python implementation of a QuadTree data structure. A QuadTree is a type of spatial data structure used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions. It is particularly useful for efficiently querying and managing spatial data.

Components
QuadTreeNode Class
The QuadTreeNode class represents a single node in the QuadTree. Each node contains:

Bounds: The rectangular area covered by the node, defined by (x, y, width, height).
Capacity: The maximum number of points that the node can hold before it needs to subdivide.
Points: A list of points (x, y, data) stored in the node.
Subdivided: A boolean flag indicating whether the node has been subdivided into four children.
Children: A list of four QuadTreeNode children if the node has been subdivided.
Methods
__init__(x, y, width, height, capacity): Initializes a QuadTreeNode with given bounds and capacity.
__str__(): Returns a string representation of the node, including bounds and points.
subdivide(): Divides the current node into four child nodes (North-West, North-East, South-West, South-East).
insert(x, y, data): Inserts a point (x, y, data) into the QuadTree. If the node exceeds its capacity, it subdivides and distributes points to the children.
search(region): Searches for points within a specified region (x, y, width, height) and returns a list of points that fall within the region.
delete(x, y): Deletes the point (x, y) from the QuadTree. If the point is found and deleted, it returns True; otherwise, it returns False.