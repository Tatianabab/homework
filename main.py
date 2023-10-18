shopping_list = ["яблоки", "молоко", "хлеб", "яйца", "сок"]
for i in shopping_list:
    print(i)
a = shopping_list.pop(1)
print(a)
shopping_list[0] = "банан"
print(shopping_list)
count = len(shopping_list)
print("Количество элементов в списке:", count)
