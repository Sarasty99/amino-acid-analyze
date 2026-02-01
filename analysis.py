from data import amino_acids

def calculate_pi(peptid):
    pka_values = [2.0, 9.0]  # C- и N-концы
    for residue in peptid:
        amino = amino_acids.get(residue.upper())
        if amino and amino.pka_radical:
            pka_values.append(amino.pka_radical)
    pka_values.sort()
    return (pka_values[0] + pka_values[-1]) / 2 if len(pka_values) >= 2 else None

def analyse(peptid, find_part=None):
    # Сброс счетчиков
    for aa in amino_acids.values():
        aa.kol = 0

    # Основной анализ
    total_mass = 0
    amino_list = []

    for part in peptid:
        if part not in amino_acids:
            print(f"{part} - не аминокислота")
            continue
        aa = amino_acids[part]
        aa.intro()
        aa.find()
        total_mass += aa.mass
        amino_list.append(aa.sign)

    # Расчет pI
    pi = calculate_pi(peptid)

    # Поиск подпоследовательности
    positions = []
    if find_part:
        start = 0
        while True:
            pos = peptid.find(find_part, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1

    return {
        'total_mass': total_mass,
        'total_amino': len(amino_list),
        'aminos': amino_list,
        'pi': round(pi, 3) if pi else "N/A",
        'positions': positions
    }