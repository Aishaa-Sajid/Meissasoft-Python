class Rectangle:
    def __init__(self,width,height):
       self._width=width
       self._height=height

    @property        #Getter
    def width(self):
        return self._width
    @property       #Getter
    def height(self):
        return self._height
    
    @width.setter         #Setter | Setters are linked to or dependent to Getters
    def width(self,width):
        self._width=width

    @height.setter       #Setter
    def height(self,height):
        self._height=height

    
obj=Rectangle(2,7)
# obj.height=5
# obj.width=6
print(obj.width)
print(obj.height)
