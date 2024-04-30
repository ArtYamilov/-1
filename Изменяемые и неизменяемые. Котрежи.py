# tuple_ = 1, 2, 3, 4, True, "Strint"  # Кортеж - коллекция, как и список, но неизменяемая.
# Значения выводятся в круглых скобках.
# tuple_2 = (1, 2, 3, 4)
# tuple_3 = tuple([1, 2, 3, 4])
# print(tuple_)
# print(type(tuple_))
# print(tuple_2)
# print(tuple_3)
# print(tuple_[0])
# tuple_[0] = 150 #  Останется не изменным.
# print(tuple_)
# tuple_ = 1, 2, 3, 4, 5, 6, True, "String"
# list_ = [1, 2, 3, 4, 5, 6, True, "String"]
# print(tuple_.__sizeof__())  # команда указывающая размер в памяти.
# print(list_.__sizeof__())
# tuple_ = ([1, 2], 0) + (1, 2)  # конкатенация.
# print(tuple_)
# tuple_[0][0] = 2  # замена элемента в котрежи состоящего из списка и элемента.
# print(tuple_)
# tuple_ = (1, 2) * 3
# print(tuple_)
immutable_var = 2, 3.1, "Верного пути", True  # integer, float, string, boolean.
print(immutable_var)
# immutable_var[2] = "На ином пути"  # Кортеж - является неизменяемой коллекцией.
# Включает в себя такие особенности, как - незменяемость, занимает меньший объём памяти,
# может хранить в себе изменяемые объекты и поддерживает конкатенацию и умножение строк.
# print(immutable_var)

mutable_list = ["День сурка", 33, True]
print(mutable_list)
mutable_list[0] = "День курка"
mutable_list[1] = 34
print(mutable_list)
