class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __repr__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        elif isinstance(other, int):
            return self.floors == other
        else:
            raise TypeError("Невозможно сравнить объекты разных типов")

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        elif isinstance(other, int):
            return self.floors < other
        else:
            raise TypeError("Невозможно сравнивать объекты разных типов")

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        elif isinstance(other, int):
            return self.floors <= other
        else:
            raise TypeError("Невозможно сравнивать объекты разных типов")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        elif isinstance(other, int):
            return self.floors > other
        else:
            raise TypeError("Невозможно сравнивать объекты разных типов")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        elif isinstance(other, int):
            return self.floors >= other
        else:
            raise TypeError("Невозможно сравнивать объекты разных типов")

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        elif isinstance(other, int):
            return self.floors != other
        else:
            raise TypeError("Невозможно сравнивать объекты разных типов")

    def __add__(self, value):
        if not isinstance(value, int):
            raise TypeError("Добавляемое значение должно быть целым числом")

        self.floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


if __name__ == "__main__":
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(f'{h1 == h2}')

    h1 = h1 + 10
    print(h1)
    print(f'{h1 == h2}')

    h1 += 10
    print(h1)

    h2 = 10 + h2
    print(h2)

    print(f'{h1 > h2}')
    print(f'{h1 >= h2}')
    print(f'{h1 < h2}')
    print(f'{h1 <= h2}')
    print(f'{h1 != h2}')