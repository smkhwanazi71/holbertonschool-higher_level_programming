#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """"Instantiation with size
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area() method"""
        return self.__size ** 2
