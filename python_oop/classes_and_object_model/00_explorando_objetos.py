"""Explora objetos integrados de Python: clases, identidades y métodos."""

number = 42
text = "hello"
numbers = [1, 2, 3]

print("Clases de los objetos:")
print("number:", type(number))
print("text:", type(text))
print("numbers:", type(numbers))

print("\nIdentidades:")
print("number:", id(number))
print("text:", id(text))
print("numbers:", id(numbers))

another_number = 42
print("\nIdentidades de dos números con el mismo valor:")
print("number:", id(number))
print("another_number:", id(another_number))
print("¿Son el mismo objeto?:", number is another_number)

print("\nMétodos y atributos disponibles para text:")
print(dir(text))
print("\nAlgunos métodos de str:")
print("text.upper():", text.upper())
print('text.replace("h", "H"):', text.replace("h", "H"))

list_a = [1, 2]
list_b = [1, 2]
print("\nListas con el mismo contenido:")
print("list_a:", id(list_a))
print("list_b:", id(list_b))
print("¿Tienen el mismo contenido?:", list_a == list_b)
print("¿Son el mismo objeto?:", list_a is list_b)
