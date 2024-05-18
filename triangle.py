from math import sqrt


class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        if self.a+self.b>self.c and self.a+self.c>self.b and self.a<self.b+self.c:
            return True
        else:
            return False
        pass
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        pass
        
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        return self.a+self.b+self.b
        pass

    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        d=(self.a+self.b+self.c)/2
        return sqrt(d*(d-self.a)*(d-self.b)*(d-self.c))
        pass
triangle = Triangle(4, 7, 5)
is_valid_triangle = triangle.is_valid()
triangle_perimeter = triangle.perimeter()
triangle_area = triangle.area()

print("Can it be a triangle?", is_valid_triangle)
# Can it be a triangle? True
print("The perimeter of the triangle is:", triangle_perimeter)
# The perimeter of the triangle is: 16
print("The area of the triangle is:", triangle_area)
# The area of the triangle is: 9.797958971132712