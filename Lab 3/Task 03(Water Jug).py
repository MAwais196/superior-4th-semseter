class WaterJugDFS:
    def __init__(self, a, b, target):
        self.a = a
        self.b = b
        self.target = target
        self.visited = set()

    def is_valid(self, x, y):
        """Check if the state (x, y) is valid."""
        return 0 <= x <= self.a and 0 <= y <= self.b

    def dfs(self, x, y, path):
        """DFS function to explore all states."""
        if (x, y) in self.visited:
            return False
        self.visited.add((x, y))
        
       
        print(f"Current state: Jug1={x}, Jug2={y}")
        
        
        if x == self.target or y == self.target:
            print(f"Target reached: Jug1={x}, Jug2={y}")
            print(f"Path: {path}")
            return True
        
        # Perform opertions
        operations = [
            ("Fill Jug1", self.a, y),  
            ("Fill Jug2", x, self.b), 
            ("Empty Jug1", 0, y),      
            ("Empty Jug2", x, 0),      
            ("Pour Jug1 to Jug2", max(0, x - (self.b - y)), min(self.b, y + x)),  
            ("Pour Jug2 to Jug1", min(self.a, x + y), max(0, y - (self.a - x)))   
        ]
        
        for op, new_x, new_y in operations:
            if self.is_valid(new_x, new_y):
                
                print(f"Performing operation: {op}")
                
                if self.dfs(new_x, new_y, path + [op]):
                    return True
        
        return False

    def solve(self):
        """Solve the Water Jug problem using DFS."""
        if self.dfs(0, 0, []):
            print("Solution found!")
        else:
            print("No solution exists.")

# Example Usage
a = 4  
b = 3  
target = 2 

water_jug = WaterJugDFS(a, b, target)
water_jug.solve()
