def find_common_participants(group1, group2, separator=','):
    # Разделяем строки на списки участников
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))
    
    # Находим общих участников
    common_participants = participants1.intersection(participants2)
    
    # Возвращаем отсортированный список
    return sorted(common_participants)

# Пример использования
participants_first_group = "ИвановІПетровІСидоров"
participants_second_group = "ПетровІСидоровІСмирнов"

# Проверка работы функции с разделителем 'І'
common_participants = find_common_participants(participants_first_group, participants_second_group, separator='І')
print("Общие участники:", common_participants)