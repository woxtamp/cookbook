def save_file_to_list():
    with open('files/recipes.txt', 'r', encoding='utf-8') as recipes:
        recipes_list = []
        for line in recipes:
            recipes_list.append(line.strip())
        return recipes_list


def convert_list_to_dict():
    ingredient_params = ['ingredient_name', 'quantity', 'measure']
    cook_book = {}
    dishes_list = []
    dishes_ingredients_count = []
    ingredients_list = []
    ingredients_list_with_params = []

    for dish in save_file_to_list():
        if not dish.isdecimal() and '|' not in dish and dish != '':
            dishes_list.append(dish)

    for counts in save_file_to_list():
        if counts.isdecimal():
            dishes_ingredients_count.append(counts)

    for ingredients in save_file_to_list():
        if '|' in ingredients:
            ingredients_list.append(ingredients)

    for item in ingredients_list:
        count = 0
        ingredients_dict = {}
        for element in item.split(' | '):
            ingredients_dict[ingredient_params[count]] = element
            count += 1
        ingredients_list_with_params.append(ingredients_dict)

    count = 0
    for dish_number in range(len(dishes_list)):
        ingredients_count = int(dishes_ingredients_count[dish_number])
        cook_book[dishes_list[dish_number]] = ingredients_list_with_params[count:count + ingredients_count]
        count += ingredients_count
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    buy_dict = {}
    loc_dict_cook_book = convert_list_to_dict()
    for dish in dishes:
        if dish == '' or dish == ' ':
            continue
        list_ingr_to_dishes = loc_dict_cook_book.get(str(dish))
        for ing in list_ingr_to_dishes:
            if ing['ingredient_name'] not in buy_dict.keys():
                buy_dict[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': 0}
            buy_dict[ing['ingredient_name']]['quantity'] = buy_dict[ing['ingredient_name']]['quantity'] + (
                int(ing['quantity'])) * person_count
    return buy_dict

print(convert_list_to_dict())
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
