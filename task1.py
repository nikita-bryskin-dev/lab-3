def find_item_index(items_list, item_to_find):
    """Функция для поиска индекса первого вхождения товара."""
    try:
        return items_list.index(item_to_find)
    except ValueError:
        return None

# Список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

print(items_list) # Список товаров в листе

# Товары для поиска
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # Вызов функции для получения индекса товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")