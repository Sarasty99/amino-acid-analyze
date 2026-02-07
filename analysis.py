from data import amino_acids

def calculate_gravy(sequence):
    """Рассчитывает индекс GRAVY"""
    total_hydropathy = sum(amino_acids[aa].hydropathy for aa in sequence if aa in amino_acids)
    return total_hydropathy / len(sequence)

def calculate_extinction(sequence):
    """Рассчитывает коэффициент экстинкции"""
    # Упрощенная формула (нужно уточнить реальные коэффициенты)
    return sum(amino_acids[aa].extinction for aa in sequence if aa in amino_acids)

def find_amyloid_regions(sequence, window=5):
    """Находит потенциальные амилоидные участки"""
    amyloidogenic = ['V', 'I', 'L', 'F', 'W', 'Y', 'C']  # Пример амилоидогенных АК
    regions = []

    for i in range(len(sequence) - window + 1):
        window_seq = sequence[i:i+window]
        count = sum(1 for aa in window_seq if aa in amyloidogenic)
        if count/window > 0.6:  # Порог 60%
            regions.append((i, i+window-1, window_seq))

    return regions

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
    gravy = calculate_gravy(peptid)
    extinction = calculate_extinction(peptid)
    amyloid_regions = find_amyloid_regions(peptid)

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
        'positions': positions,
        'gravy': round(gravy, 3),
        'extinction': round(extinction, 3),
        'amyloid_regions': amyloid_regions,
        'pi': round(pi, 3) if pi else "N/A"
    }