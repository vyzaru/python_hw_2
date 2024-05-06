from random import choices

list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]

def rand_item(list_in):
    return choices(list_in, k=2)

print(rand_item(list_el))