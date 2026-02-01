class AminoAcids:
    def __init__(self, sign, name, mass, radical, pka_radical=None):
        self.sign = sign
        self.name = name
        self.mass = mass
        self.radical = radical
        self.kol = 0
        self.pka_radical = pka_radical

    def intro(self):
        print(f'\t {self.sign.upper()} - {self.name}, m={self.mass}')

    def find(self):
        self.kol += 1

    def mass_share(self, total_mass):
        return (self.mass * self.kol * 100) / total_mass

amino_acids = {
    'G': AminoAcids('gly', 'глицин', 75.067, 'неполярный радикал, гидрофобный'),
    'V': AminoAcids('val', 'валин', 117.147, 'неполярный радикал, гидрофобный'),
    # ... остальные аминокислоты ...
    'H': AminoAcids('his', 'гистидин', 155.156, 'электрический(+) заряженный радикал, гидрофильный', pka_radical=6.00)
}