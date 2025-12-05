class Base():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    def shape(self):
        return "This is a shape"
    
class Square(Base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
    def shape(self):
        return "This is a square"
    
    def draw(self):
        return f"""
({self.x}, {self.y})\n{self.size}"""
def main():
    s = Square(2,3,5)
    print(s.shape() + s.draw())
    
main()