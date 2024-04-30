food = ["apple", "coconut", "banan"]  # список, коллекция которую можно перебрать.
# print(food[0])  # вывод на экран первого элемента
# food[1] = "peach"  # замена второго элемента.
# print(food)
food.append(True)  # метод добавления элемента в конец.
print(food)
food.extend("string")  # метод добавления каждого символа по отдельности.
print(food)
food.extend(["string", 2])  # метод добавления каждого элемента последовательности.
print(food)
# food.remove("apple")
# print(food)
print("coconut" in food)  # команда проверки есть ли элемент в списке или нет.
print("coconut" not in food)  # команда проверки отсутствия элемента.
print(food[0:2])
