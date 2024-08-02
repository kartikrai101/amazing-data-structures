class QuadTreeNode:
    def __init__(self, x, y, width, height, capacity):
        self.bounds = (x, y, width, height)  # (x, y, width, height)
        self.capacity = capacity
        self.points = []  # List of (x, y, data) tuples
        self.subdivided = False
        self.children = []

    def __str__(self):
        return f"QuadTreeNode(bounds={self.bounds}, points={self.points})"

    def subdivide(self):
        x, y, w, h = self.bounds
        hw, hh = w / 2, h / 2

        self.children = [
            QuadTreeNode(x, y, hw, hh, self.capacity),  # NW
            QuadTreeNode(x + hw, y, hw, hh, self.capacity),  # NE
            QuadTreeNode(x, y + hh, hw, hh, self.capacity),  # SW
            QuadTreeNode(x + hw, y + hh, hw, hh, self.capacity)  # SE
        ]
        self.subdivided = True

    def insert(self, x, y, data):
        bx, by, bw, bh = self.bounds
        # Check if the point is within the bounds of this node
        if not (bx <= x < bx + bw and by <= y < by + bh):
            return False

        if len(self.points) < self.capacity:
            self.points.append((x, y, data))
            return True
        else:
            if not self.subdivided:
                self.subdivide()
            for child in self.children:
                if child.insert(x, y, data):
                    return True
        return False

    def search(self, region):
        x, y, w, h = region
        bx, by, bw, bh = self.bounds
        results = []

        # Check if the region overlaps with this node's bounds
        if x + w < bx or x > bx + bw or y + h < by or y > by + bh:
            return results

        # Check points in this node
        for px, py, data in self.points:
            if x <= px < x + w and y <= py < y + h:
                results.append((px, py, data))

        # Search in children if they exist
        if self.subdivided:
            for child in self.children:
                results.extend(child.search(region))
        return results

    def delete(self, x, y):
        for i, (px, py, data) in enumerate(self.points):
            if px == x and py == y:
                del self.points[i]
                return True

        if self.subdivided:
            for child in self.children:
                if child.delete(x, y):
                    return True
        
        return False


def main():
    # Create a QuadTree with boundaries (0, 0, 100, 100) and capacity for 4 points per node
    qt = QuadTreeNode(0, 0, 100, 100, 4)

    # Insert points with string data
    qt.insert(10, 10, "A")
    qt.insert(20, 20, "B")
    qt.insert(30, 30, "C")
    qt.insert(40, 40, "D")
    qt.insert(50, 50, "E")  # Should trigger subdivision

    # Search for points in a specific region
    print("Points in region (5, 5, 30, 30):", qt.search((5, 5, 30, 30)))

    # Delete a point
    qt.delete(30, 30)
    print("Points in region (5, 5, 30, 30) after deletion:", qt.search((5, 5, 30, 30)))

 

if __name__ == "__main__":

    main()

