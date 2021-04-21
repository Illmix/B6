# from test import Rectangle, Square
#
# rect_1 = Rectangle(3, 4)
# rect_2 = Rectangle(12, 5)
#
# square_1 = Square(4)
# square_2 = Square(8)
#
#
# figures = [rect_1, rect_2, square_1, square_2]
# for figure in figures:
#     if isinstance(figure, Square):
#         print(figure.get_area_square())
#     else:
#         print(figure.get_area())

from main import Cat, Circle

cat_1 = Cat('Пупс', 'Male', 22)

print(cat_1.get_name(),
      cat_1.get_gender(),
      cat_1.get_age())

circle_1 = Circle(20)

print(circle_1.get_area())
