# C++, Java: this


class Animal:
    def __init__(self, weight: float, height: float):
        self.weight = weight
        self.height = height

    def jump(self) -> None:
        print("Jump!")


def main() -> None:
    dog = Animal(10, 0.8)
    print(dog.height)
    print(dog.weight)
    dog.jump()

    cat = Animal(3, 0.3)
    print(cat.height)
    print(cat.weight)
    cat.jump()


if __name__ == "__main__":
    main()
