participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(group_1: str, group_2: str, separator=','):

    participants_1 = group_1.split(separator)
    participants_2 = group_2.split(separator)

    common_participants = set(participants_1).intersection(set(participants_2))

    return sorted(common_participants)

common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print("Общие участники при разделителе '|':", common_participants)