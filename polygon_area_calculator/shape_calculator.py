class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    # Use the pythagorean
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    """
    Return a string that represents the shape using lines of '*'.
    # of lines is = to the height
    # of * in each line = to the width
    """
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for i in range(self.height):
            picture += '*' * self.width + '\n'
        return picture

    # Takes another shape and returns the # of times it fits inside the shape
    def get_amount_inside(self, shape):
        width_ratio = self.width // shape.width
        height_ratio = self.height // shape.height
        return width_ratio * height_ratio

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


# Create the class that inherits from the square class
class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def __str__(self):
        return f'Square(side={self.width})'
