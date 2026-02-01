class AminoAcids():
    def __init__(self, sign, name, mass, radical):
        self.sign = sign
        self.name = name
        self.mass = mass
        self.radical = radical
        self.kol = 0
    def intro(self):
        print(f'\t {self.sign.upper()} - {self.name}, m={self.mass}')
    def find(self):
        self.kol += 1
    def mass_share(self, total_mass):
         return (self.mass * self.kol * 100) / total_mass
amino_acids = {
    'G': AminoAcids('gly', 'глицин', 75.067, 'неполярный радикал, гидрофобный'),
    'V': AminoAcids('val', 'валин', 117.147, 'неполярный радикал, гидрофобный'),
    'L': AminoAcids('leu', 'лейцин', 131.175, 'неполярный радикал, гидрофобный'),
    'I': AminoAcids('ile', 'изолейцин', 131.175, 'неполярный радикал, гидрофобный'),
    'M': AminoAcids('met', 'метионин', 149.208, 'неполярный радикал, гидрофобный'),
    'A': AminoAcids('ala', 'аланин', 89.094, 'неполярный радикал, гидрофобный'),
    'F': AminoAcids('phe', 'фенилаланин', 165.192, 'неполярный радикал, гидрофобный'),
    'W': AminoAcids('trp', 'триптофан', 204.228, 'неполярный радикал, гидрофобный'),
    'P': AminoAcids('pro', 'пролин', 115.132, 'неполярный радикал, гидрофобный'),
    'S': AminoAcids('ser', 'серин', 105.093, 'полярный радикал, гидрофильный'),
    'T': AminoAcids('thr', 'треонин', 119.119, 'полярный радикал, гидрофильный'),
    'C': AminoAcids('cys', 'цистеин', 121.154, 'полярный радикал, гидрофильный'),
    'Y': AminoAcids('tyr', 'тирозин', 181.189, 'полярный радикал, гидрофильный'),
    'N': AminoAcids('asn', 'аспарагин', 132.119, 'полярный радикал, гидрофильный'),
    'Q': AminoAcids('gln', 'глутамин', 146.145, 'полярный радикал, гидрофильный'),
    'D': AminoAcids('asp', 'аспаргиновая кислота', 133.103, 'электрический(-) заряженный радикал, гидрофильный'),
    'E': AminoAcids('glu', 'глутаминовая кислота', 147.130, 'электрический(-) заряженный радикал, гидрофильный'),
    'K': AminoAcids('lys', 'лизин', 146.189, 'электрический(+) заряженный радикал, гидрофильный'),
    'R': AminoAcids('arg', 'аргинин', 174.203, 'электрический(+) заряженный радикал, гидрофильный'),
    'H': AminoAcids('his', 'гистидин', 155.156, 'электрический(+) заряженный радикал, гидрофильный')
}
def analyse(peptid, amino_acids, find_part=None):
    result = {}
    total_mass = 0
    total_amino = 0
    amino_list = []
    positions = []  # список для хранения позиций искомой части
    count = 0

    for amino_acid in amino_acids.values():
        amino_acid.kol = 0
    for peptid_part in peptid:
        if peptid_part not in amino_acids:
            print(peptid_part, '- не аминокислота')
        else:
            amino_in_peptid = amino_acids[peptid_part]
            amino_in_peptid.intro()
            amino_in_peptid.find()
            mass = amino_in_peptid.mass
            sign = amino_in_peptid.sign
            amino_list.append(sign)
            total_amino += 1
            total_mass += mass
    print('Список аминокислот:', amino_list)
    print('Общая масса =', total_mass, '\nОбщее число аминокислот:', total_amino, ', подробнее:')
    result['total_mass'] = total_mass
    result['total_amino'] = total_amino
    result['aminos'] = amino_list
    if total_mass == 0:
        print("Ошибка: Общая масса равна 0. Невозможно рассчитать массовую долю.")
    else:
        for sign, amino_acid in amino_acids.items():
            if amino_acid.kol > 0:
                mass_fraction = amino_acid.mass_share(total_mass)  # определение массовой доли каждой аминокислоты
                print(f'\t {amino_acid.name.title()} в цепочке = {amino_acid.kol};\t массовая доля = {mass_fraction:.2f}%;\n\t Характер радикала: {amino_acid.radical}')
    if find_part:
        start = 0
        while True:
            position = peptid.find(find_part, start)
            if position == -1:
                break
            count += 1
            positions.append(position)
            start = position + 1
        if count == 0:
            print('В последовательности нет таких частей!')
            result['positions'] = []
        else:
            print(f'Искомая последовательность найдена {count} раз(а).')
            print('Позиции вхождений:', positions)
            result['positions'] = positions
    
    return result 
sequence_data = {}  # словарь для хранения информации о последовательностях

is_running = True
while is_running:
    button = input('0-завершение, 1-анализ, 2-сравнение двух, 3-для поиска в цепи: ')
    if button == '1':
        peptid = input("Введите последовательность аминокислот:").upper()
        result = analyse(peptid, amino_acids)
        sequence_data[peptid] = result 
        print(sequence_data)

    elif button == '2':
        first = input('Введите первую последовательность: ').upper()
        result1 = analyse(first,amino_acids)
        
        second = input('Введите вторую последовательность: ').upper()
        result2 = analyse(second,amino_acids)
        
        general = []
        uniq2 = []
        uniq1 = []
        for aminos2 in result2['aminos']:
            if aminos2 in result1['aminos']:
                general.append(aminos2)
            else:
                uniq2.append(aminos2)
        for aminos1 in result1['aminos']:
            if aminos1 not in result2['aminos']:
                uniq1.append(aminos1)

        print('А/к, присутствующие в Двух цепях:', general, '\nА/к, уникальные для Первой:', uniq1,
              '\nА/к, уникальные для Второй:', uniq2)
    elif button == '3':
        if not sequence_data:
            print("Нет доступных последовательностей для поиска. Сначала проанализируйте хотя бы одну последовательность")
        else:
            print("Доступные последовательности:")
            for i, peptid in enumerate(sequence_data.keys()):
                 print(f"{i+1}: {peptid}")
            try:
                choice = int(input("Введите номер последовательности для поиска: ")) - 1
                if 0 <= choice < len(sequence_data):
                    peptid = list(sequence_data.keys())[choice]
                    find_part = input('Введите искомую последовательность:').upper()
                    result = analyse(peptid, amino_acids, find_part=find_part)
                    sequence_data[peptid] = result
                else:
                    print("Неверный номер последовательности.")
            except ValueError:
                print("Пожалуйста, введите число.")   
    elif button == '0':
        is_running = False
        