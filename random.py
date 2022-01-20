#19.01.2022 - lesson 3
#списки - это изменяемый тип данных
#list(range(1, 100, 20)) - получим список от 1 до 100 с шагом 20

example_list = [1, False, "a"]
for element in example_list:
    print(element)
#[:] - это срез
#print(example_list[от_куда:до_куда:шаг])
#сортировка списка
unsorted_list = [2, 3, 1, 4, 5]
print(sorted(unsorted_list))
print(unsorted_list)

#кортежи через круглые скобки ()

#####
#a = 'test'
#s = f"A is {a}"
####
