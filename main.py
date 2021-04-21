class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age if self.age > 0 and isinstance(self.age, int) else print('Неправильный возраст')


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14159 * self.r ** 2
