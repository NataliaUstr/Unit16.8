from Rectangle import Rectangle, Square, Circle
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print("Площадь прямоугольника1:", rect_1.get_area())
print("Площадь прямоугольника2:", rect_2.get_area())

sq_1 = Square(5)
sq_2 = Square(10)
print("Площадь квадрата1:", sq_1.get_area_square(),
      "Площадь квадрата2:", sq_2.get_area_square())

Circle_1 = Circle(6)
print("Площадь круга:", Circle_1.get_area_circle())


figures = [rect_1, rect_2, sq_1, sq_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())