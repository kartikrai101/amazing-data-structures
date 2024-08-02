<h1>QuadTree Implementation in Python</h1>
<h2>Overview</h2>
<p>This repository contains a Python implementation of a QuadTree data structure. A QuadTree is a type of spatial data structure used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions. It is particularly useful for efficiently querying and managing spatial data.</p>

<h2>Components</h2>
<h3>QuadTreeNode Class</h3>

The QuadTreeNode class represents a single node in the QuadTree. Each node contains:

<ul>
  <li><b>Bounds:</b> The rectangular area covered by the node, defined by (x, y, width, height).</li>
  <li><b>Capacity:</b> The maximum number of points that the node can hold before it needs to subdivide.</li>
  <li><b>Points:</b> A list of points (x, y, data) stored in the node.</li>
  <li><b>Subdivided:</b> A boolean flag indicating whether the node has been subdivided into four children.</li>
  <li><b>Children:</b> A list of four QuadTreeNode children if the node has been subdivided.</li>
</ul>
<h3>Methods</h3>
<ul>
  <li><b>__init__(x, y, width, height, capacity):</b> Initializes a QuadTreeNode with given bounds and capacity.</li>
  <li><b>__str__():</b> Returns a string representation of the node, including bounds and points.</li>
  <li><b>subdivide():</b> Divides the current node into four child nodes (North-West, North-East, South-West, South-East).</li>
  <li><b>insert(x, y, data):</b> Inserts a point (x, y, data) into the QuadTree. If the node exceeds its capacity, it subdivides and distributes points to the children.</li>
  <li><b>search(region):</b> Searches for points within a specified region (x, y, width, height) and returns a list of points that fall within the region.</li>
  <li><b>delete(x, y):</b> Deletes the point (x, y) from the QuadTree. If the point is found and deleted, it returns True; otherwise, it returns False.</li>
</ul>
