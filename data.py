class AminoAcids:
    def __init__(self, sign, name, mass, radical, pka_radical=None, hydropathy=None, extinction=None):
        self.sign = sign
        self.name = name
        self.mass = mass
        self.radical = radical
        self.kol = 0
        self.pka_radical = pka_radical
        self.hydropathy = hydropathy  
        self.extinction = extinction

    def intro(self):
        print(f'\t {self.sign.upper()} - {self.name}, m={self.mass}')

    def find(self):
        self.kol += 1

    def mass_share(self, total_mass):
        return (self.mass * self.kol * 100) / total_mass

amino_acids = {
    'G': AminoAcids('gly', 'глицин', 75.067, 'неполярный радикал, гидрофобный', hydropathy=-0.4, extinction=0),
    'V': AminoAcids('val', 'валин', 117.147, 'неполярный радикал, гидрофобный', hydropathy= 4.2, extinction=0),
    'L': AminoAcids('leu', 'лейцин', 131.175, 'неполярный радикал, гидрофобный', hydropathy=3.8, extinction=0),
    'I': AminoAcids('ile', 'изолейцин', 131.175, 'неполярный радикал, гидрофобный', hydropathy=4.5, extinction=0),
    'M': AminoAcids('met', 'метионин', 149.208, 'неполярный радикал, гидрофобный', hydropathy=1.9, extinction=0),
    'A': AminoAcids('ala', 'аланин', 89.094, 'неполярный радикал, гидрофобный', hydropathy=1.8, extinction=0),
    'F': AminoAcids('phe', 'фенилаланин', 165.192, 'неполярный радикал, гидрофобный', hydropathy=2.8, extinction=0),
    'W': AminoAcids('trp', 'триптофан', 204.228, 'неполярный радикал, гидрофобный', hydropathy=-0.9, extinction=0),
    'P': AminoAcids('pro', 'пролин', 115.132, 'неполярный радикал, гидрофобный', hydropathy=-1.6, extinction=0),
    'S': AminoAcids('ser', 'серин', 105.093, 'полярный радикал, гидрофильный', hydropathy=-0.8, extinction=0),
    'T': AminoAcids('thr', 'треонин', 119.119, 'полярный радикал, гидрофильный', hydropathy=-0.7, extinction=0),
    'C': AminoAcids('cys', 'цистеин', 121.154, 'полярный радикал, гидрофильный', pka_radical=8.30, hydropathy=2.5, extinction=0),
    'Y': AminoAcids('tyr', 'тирозин', 181.189, 'полярный радикал, гидрофильный', pka_radical=10.10, hydropathy=-1.3, extinction=0),
    'N': AminoAcids('asn', 'аспарагин', 132.119, 'полярный радикал, гидрофильный', hydropathy=-3.5, extinction=0),
    'Q': AminoAcids('gln', 'глутамин', 146.145, 'полярный радикал, гидрофильный', hydropathy=-3.5, extinction=0),
    'D': AminoAcids('asp', 'аспаргиновая кислота', 133.103, 'электрический(-) заряженный радикал, гидрофильный', pka_radical=3.90, hydropathy=-3.5, extinction=0),
    'E': AminoAcids('glu', 'глутаминовая кислота', 147.130, 'электрический(-) заряженный радикал, гидрофильный', 4.25, hydropathy=-3.5, extinction=0),
    'K': AminoAcids('lys', 'лизин', 146.189, 'электрический(+) заряженный радикал, гидрофильный', pka_radical=10.53, hydropathy=-3.9, extinction=0),
    'R': AminoAcids('arg', 'аргинин', 174.203, 'электрический(+) заряженный радикал, гидрофильный', pka_radical=12.48, hydropathy=-4.5, extinction=0),
    'H': AminoAcids('his', 'гистидин', 155.156, 'электрический(+) заряженный радикал, гидрофильный', pka_radical=6.00, hydropathy=-3.2, extinction=0)
}