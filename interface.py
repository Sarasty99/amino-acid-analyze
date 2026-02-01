from analysis import analyse
from data import amino_acids

sequence_data = {}

def compare_sequences(seq1, seq2):
    result1 = analyse(seq1)
    result2 = analyse(seq2)

    general = list(set(result1['aminos']) & set(result2['aminos']))
    uniq1 = list(set(result1['aminos']) - set(result2['aminos']))
    uniq2 = list(set(result2['aminos']) - set(result1['aminos']))

    print('А/к в обеих цепях:', general)
    print('Уникальные для первой:', uniq1)
    print('Уникальные для второй:', uniq2)

def main_menu():
    while True:
        choice = input('0-выход, 1-анализ, 2-сравнение, 3-поиск: ')

        if choice == '1':
            seq = input("Введите последовательность: ").upper()
            result = analyse(seq)
            sequence_data[seq] = result
            print(result)

        elif choice == '2':
            seq1 = input('Первая последовательность: ').upper()
            seq2 = input('Вторая последовательность: ').upper()
            compare_sequences(seq1, seq2)

        elif choice == '3':
            if not sequence_data:
                print("Сначала проанализируйте последовательность")
                continue
            print("Доступные последовательности:")
            for i, seq in enumerate(sequence_data.keys()):
                print(f"{i+1}: {seq}")
            try:
                num = int(input("Выберите номер: ")) - 1
                seq = list(sequence_data.keys())[num]
                part = input('Искомая часть: ').upper()
                result = analyse(seq, find_part=part)
                sequence_data[seq] = result
            except (ValueError, IndexError):
                print("Ошибка ввода")

        elif choice == '0':
            break