#!/usr/bin/env python3
"""Demonstrate inheritance and polymorphism with animal classes."""


class Animal:
    """Represent an animal with a default sound."""

    def speak(self):
        """Return the animal's default sound."""
        return "Some sound"


class Dog(Animal):
    """Represent a dog."""

    def speak(self):
        """Return the sound made by a dog."""
        return "Woof"


class Cat(Animal):
    """Represent a cat."""

    def speak(self):
        """Return the sound made by a cat."""
        return "Meow"


def main():
    """Demonstrate polymorphic method calls and class relationships."""
    animals = [Dog(), Cat(), Dog()]

    for animal in animals:
        print(animal.speak())

    dog = Dog()
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))


if __name__ == "__main__":
    main()
