
with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline())
        recipes = []
        for num in range(ingredients_count):
            recipe = file.readline().strip()
            name, amount, unit = recipe.split('|')
            recipes.append({'name': name, 'amount': amount, 'unit': unit})
        file.readline()
        cook_book[dish_name] = recipes

for key, value in cook_book.items():
    print(f'\n{key}\n')
    for key in value:
        print(f'{key}')
print()

def get_shop_list_by_dishes(dishes, person_count):
    new_recipe = {}
    for el in dishes:
        if el in cook_book.keys():
            for el in cook_book[el]:
                new_recipe[el['name']] = {'measur': el['unit'], 'quantity':
                                           int(el['amount']) * person_count}
        else:
            return f'Такого рецепта нет в книге'
    for key, value in new_recipe.items():
        print(key, value)
    return

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

