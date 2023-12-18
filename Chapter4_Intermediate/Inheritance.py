class Animal:
    def __init__(self, weight: float, height: float) -> None:
        self.weight = weight
        self.height = height

    def print_data(self) -> None:
        print("Height: ", self.height)
        print("Weight: ", self.weight)


class Dog(Animal):
    def __init__(self, weight: float, height: float) -> None:
        super().__init__(weight, height)

    def bark(self) -> None:
        print("Bark!")


class Cat(Animal):
    def __init__(self, weight: float, height: float) -> None:
        super().__init__(weight, height)

    def meow(self) -> None:
        print("Meow!")


def main() -> None:
    dog = Dog(10, 0.8)
    dog.print_data()
    dog.bark()

    cat = Cat(3, 0.3)
    cat.print_data()
    cat.meow()


if __name__ == "__main__":
    main()
