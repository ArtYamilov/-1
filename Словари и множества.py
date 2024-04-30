# phone_book = {"Артур": 89603885699, "Тимур1": 89373602964}
# phone_book["Артур"] = 89374750567  # заменит значение ключа.
# phone_book["Руся"] = 89220619915  # добавит новый ключ со значением.
# # del phone_book["Артур"]
# phone_book.update({"Рустем": 89053095091,
#                    "Тимур2": 89876274926,
#                    "Рамиль": 89216554510})  # добавит или заменит несколько ключей со значениями.
# print(phone_book)
# print(phone_book.get("Артур"))  # возвращает значение по указанному ключу.
# print(phone_book.get("Руслан", "Ключ отсутствует"))  # вместо none замена на второе значение.
# print(phone_book)
# #a = phone_book.pop("Артур")  # удаляет ключ и возвращает ему соответствующее значение.
# #print(phone_book)
# #print(a)
# list_ = [1, 2, 3]
# list_.pop(0)  # удаляет значение в списке.
# print(list_)
# print(phone_book.keys())
# print(phone_book.values())
# print(phone_book.items())
# set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4}  # множества - хранит в себе только уникальные значения.
# print(set_)
# set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, "String", True, (1, 2, 3)}
# print(set_)
# list_1 = [1, 2, 1, 1, 1, 2, 3, 3, 4]
# print(set(list_1))  # команда перевода во множество.
# list_1 = set(list_1)
# print(list_1)
# print(list_1.remove(4))  # удаляет элемент с множества.
# print(list_1)
# print(list_1.add(5))  # добавляет элемент в конец множества.
# print(list_1)
my_list = ["Apple", "Banana", "Orange", "Pineapple", "Strawberry"]
print(my_list)
print(my_list[0], my_list[3])
print(my_list[2:5])
my_list[2] = "Tangarine"
print(my_list)

my_dict = {"Apple": "Яблоко", "Banana": "Банан", "Orange": "Апельсин"}
print(my_dict)
print(my_dict.values())
my_dict["Apple"] = "Груша"
my_dict["Kiwi"] = "Киви"
print(my_dict)
