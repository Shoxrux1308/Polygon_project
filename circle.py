from math import pi


class Circle:
    def __init__(self, radius:float):
        self.radius = radius
        
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        
        Args:
            No
        Returns:
            bool: True if the circle is valid, False otherwise
        """
        if self.radius>0:
            return 1==1
        else:
            return 1==0
    
    def diameter(self) -> float:
        '''
        This method finds the diameter of the circle.
        Args:
            no
        Returns:
            float: return diameter of the circle if the circle is valid, 0 otherwise
        '''
        return self.radius*2
    
    def circumference(self) -> float:
        '''
        This method finds the circumference of the circle.
        Args:
            no
        Returns:
            float: return circumference of the circle if the circle is valid, 0 otherwise
        '''
        return 2*pi*self.radius
        pass
    
    def area(self) -> float:
        '''
        This method finds the area of the circle.
        Args:
            no
        Returns:
            float: return area of the circle if the circle is valid, 0 otherwise
        '''
        return pi*self.radius**2
        pass
circle = Circle(4)
is_valid_circle = circle.is_valid()
circle_diameter = circle.diameter()
circle_circumference = circle.circumference()
circle_area = circle.area()

print("Can it be a circle?", is_valid_circle)
# Can it be a circle? True
print("The diameter of the circle is:", circle_diameter)
# The diameter of the circle is: 8
print("The circumference of the circle is:", circle_circumference)
# The circumference of the circle is: 25.132741228718345
print("The area of the circle is:", circle_area)