class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
        
    def __add__(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)
    
    def __bool__(self) -> bool:
        return bool(abs(self))
    
    def __abs__(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5
    
    def __mul__(self, scalar: float) -> 'Vector':
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)
    
if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    v3 = v1 + v2
    print(f"v3: {v3}")
    
    magnitude = abs(v1)
    print(f"|v1|: {magnitude}")
    
    v4 = v1 * 2
    print(f"v4: {v4}")