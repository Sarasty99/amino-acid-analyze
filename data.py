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
    'L': AminoAcids('leu', 'лейцин', 131.175, 'неполярный радикал, гидрофобный'),
    'I': AminoAcids('ile', 'изолейцин', 131.175, 'неполярный радикал, гидрофобный'),
    'M': AminoAcids('met', 'метионин', 149.208, 'неполярный радикал, гидрофобный'),
    'A': AminoAcids('ala', 'аланин', 89.094, 'неполярный радикал, гидрофобный'),
    'F': AminoAcids('phe', 'фенилаланин', 165.192, 'неполярный радикал, гидрофобный'),
    'W': AminoAcids('trp', 'триптофан', 204.228, 'неполярный радикал, гидрофобный'),
    'P': AminoAcids('pro', 'пролин', 115.132, 'неполярный радикал, гидрофобный'),
    'S': AminoAcids('ser', 'серин', 105.093, 'полярный радикал, гидрофильный'),
    'T': AminoAcids('thr', 'треонин', 119.119, 'полярный радикал, гидрофильный'),
    'C': AminoAcids('cys', 'цистеин', 121.154, 'полярный радикал, гидрофильный', pka_radical=8.30),
    'Y': AminoAcids('tyr', 'тирозин', 181.189, 'полярный радикал, гидрофильный', pka_radical=10.10),
    'N': AminoAcids('asn', 'аспарагин', 132.119, 'полярный радикал, гидрофильный'),
    'Q': AminoAcids('gln', 'глутамин', 146.145, 'полярный радикал, гидрофильный'),
    'D': AminoAcids('asp', 'аспаргиновая кислота', 133.103, 'электрический(-) заряженный радикал, гидрофильный', pka_radical=3.90),
    'E': AminoAcids('glu', 'глутаминовая кислота', 147.130, 'электрический(-) заряженный радикал, гидрофильный', 4.25),
    'K': AminoAcids('lys', 'лизин', 146.189, 'электрический(+) заряженный радикал, гидрофильный', pka_radical=10.53),
    'R': AminoAcids('arg', 'аргинин', 174.203, 'электрический(+) заряженный радикал, гидрофильный', pka_radical=12.48),
    'H': AminoAcids('his', 'гистидин', 155.156, 'электрический(+) заряженный радикал, гидрофильный', pka_radical=6.00)
}