class Elements:

  def __init__(self, name, atomicNumber, symbol, atomicWeight, numberGroup, K,
L, M, N, O, P, Q, s, p, d, f, g):
    self.name = name
    self.atomicNumber = atomicNumber
    self.symbol = symbol
    self.atomicWeight = atomicWeight
    self.numberGroup = numberGroup
    self.K = K
    self.L = L
    self.M = M
    self.N = N
    self.O = O
    self.P = P
    self.Q = Q
    self.s = s
    self.p = p
    self.d = d
    self.f = f
    self.g = g

H = Elements('Hidrogênio', 1, 'H', 1.008, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,0)
He = Elements('Hélio', 2, 'He', 4.0026, 18, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0)
Li = Elements('Lítio', 3, 'Li', 6.94, 1, 2, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0)
Be = Elements('Berílio', 4, 'Be', 9.0122, 2, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0,
              0)
B = Elements('Boro', 5, 'B', 10.81, 13, 2, 3, 0, 0, 0, 0, 2, 3, 0, 0, 0, 0)
C = Elements('Carbono', 6, 'C', 12.01, 14, 2, 4, 0, 0, 0, 0, 2, 4, 0, 0, 0, 0)
N = Elements('Nitrogênio', 7, 'N', 14.01, 15, 2, 5, 0, 0, 0, 0, 2, 5, 0, 0, 0,
             0)
O = Elements('Oxigênio', 8, 'O', 16.0, 16, 2, 6, 0, 0, 0, 0, 2, 6, 0, 0, 0, 0)
F = Elements('Flúor', 9, 'F', 19.0, 17, 2, 7, 0, 0, 0, 0, 2, 7, 0, 0, 0, 0)
Ne = Elements('Neônio', 10, 'Ne', 20.18, 18, 2, 8, 0, 0, 0, 0, 2, 8, 0, 0, 0,
              0)
Na = Elements('Sódio', 11, 'Na', 22.99, 1, 2, 8, 1, 0, 0, 0, 2, 8, 1, 0, 0, 0)

Mg = Elements('Magnésio', 12, 'Mg', 24.31, 2, 2, 8, 2, 0, 0, 0, 2, 2, 8, 2, 0,
              0)
Si = Elements('Silício', 14, 'Si', 28.09, 14, 2, 8, 4, 0, 0, 0, 2, 2, 8, 4, 0,
              0)
P = Elements('Fósforo', 15, 'P', 30.97, 15, 2, 8, 5, 0, 0, 0, 2, 2, 8, 5, 0, 0)
S = Elements('Enxofre', 16, 'S', 32.07, 16, 2, 8, 6, 0, 0, 0, 2, 2, 8, 6, 0, 0)
Cl = Elements('Cloro', 17, 'Cl', 35.45, 17, 2, 8, 7, 0, 0, 0, 2, 2, 8, 7, 0, 0)
Ar = Elements('Argônio', 18, 'Ar', 39.95, 18, 2, 8, 8, 0, 0, 0, 2, 2, 8, 8, 0,
              0)
K = Elements('Potássio', 19, 'K', 39.1, 1, 2, 8, 8, 1, 0, 0, 2, 2, 8, 8, 1, 0)
Ca = Elements('Cálcio', 20, 'Ca', 40.08, 2, 2, 8, 8, 2, 0, 0, 2, 2, 8, 8, 2, 0)
Sc = Elements('Escândio', 21, 'Sc', 44.96, 3, 2, 8, 9, 2, 0, 0, 2, 2, 8, 9, 2,
              0)
Ti = Elements('Titânio', 22, 'Ti', 47.87, 4, 2, 8, 10, 2, 0, 0, 2, 2, 8, 10, 2,
              0)
V = Elements('Vanádio', 23, 'V', 50.94, 5, 2, 8, 11, 2, 0, 0, 2, 2, 8, 11, 2,
             0)
Cr = Elements('Cromo', 24, 'Cr', 52.00, 6, 2, 8, 13, 1, 0, 0, 2, 2, 8, 13, 1,
              0)
Mn = Elements('Manganês', 25, 'Mn', 54.94, 7, 2, 8, 13, 2, 0, 0, 2, 2, 8, 13,
              2, 0)
Fe = Elements('Ferro', 26, 'Fe', 55.85, 8, 2, 8, 14, 2, 0, 0, 2, 2, 8, 14, 2,
              0)
Co = Elements('Cobalto', 27, 'Co', 58.93, 9, 2, 8, 15, 2, 0, 0, 2, 2, 8, 15, 2,
              0)
Ni = Elements('Níquel', 28, 'Ni', 58.69, 10, 2, 8, 16, 2, 0, 0, 2, 2, 8, 16, 2,
              0)
Cu = Elements('Cobre', 29, 'Cu', 63.55, 11, 2, 8, 18, 1, 0, 0, 2, 2, 8, 18, 1,
              0)
Zn = Elements('Zinco', 30, 'Zn', 65.38, 12, 2, 8, 18, 2, 0, 0, 2, 2, 8, 18, 2,
              0)
# Declarações de objetos para mais elementos químicos
Ga = Elements('Gálio', 31, 'Ga', 69.72, 13, 2, 8, 18, 3, 0, 0, 2, 2, 8, 18, 3,
              0)
Ge = Elements('Germanio', 32, 'Ge', 72.63, 14, 2, 8, 18, 4, 0, 0, 2, 2, 8, 18,
              4, 0)
As = Elements('Arsênio', 33, 'As', 74.92, 15, 2, 8, 18, 5, 0, 0, 2, 2, 8, 18,
              5, 0)
Se = Elements('Selênio', 34, 'Se', 78.97, 16, 2, 8, 18, 6, 0, 0, 2, 2, 8, 18,
              6, 0)
Br = Elements('Bromo', 35, 'Br', 79.90, 17, 2, 8, 18, 7, 0, 0, 2, 2, 8, 18, 7,
              0)
Kr = Elements('Criptônio', 36, 'Kr', 83.80, 18, 2, 8, 18, 8, 0, 0, 2, 2, 8, 18,
              8, 0)
Rb = Elements('Rubídio', 37, 'Rb', 85.47, 1, 2, 8, 18, 8, 1, 0, 2, 2, 8, 18, 8,
              1)
Sr = Elements('Estrôncio', 38, 'Sr', 87.62, 2, 2, 8, 18, 8, 2, 0, 2, 2, 8, 18,
              8, 2)
Y = Elements('Ítrio', 39, 'Y', 88.91, 3, 2, 8, 18, 9, 2, 0, 2, 2, 8, 18, 9, 2)
Zr = Elements('Zircônio', 40, 'Zr', 91.22, 4, 2, 8, 18, 10, 2, 0, 2, 2, 8, 18,
              10, 2)
Nb = Elements('Nióbio', 41, 'Nb', 92.91, 5, 2, 8, 18, 12, 1, 0, 2, 2, 8, 18,
              12, 1)
Mo = Elements('Molibdênio', 42, 'Mo', 95.95, 6, 2, 8, 18, 13, 1, 0, 2, 2, 8,
              18, 13, 1)
Tc = Elements('Tecnécio', 43, 'Tc', 98.00, 7, 2, 8, 18, 13, 2, 0, 2, 2, 8, 18,
              13, 2)
Ru = Elements('Rutênio', 44, 'Ru', 101.1, 8, 2, 8, 18, 15, 1, 0, 2, 2, 8, 18,
              15, 1)
Rh = Elements('Ródio', 45, 'Rh', 102.9, 9, 2, 8, 18, 16, 1, 0, 2, 2, 8, 18, 16,
              1)
Pd = Elements('Paládio', 46, 'Pd', 106.4, 10, 2, 8, 18, 18, 0, 0, 2, 2, 8, 18,
              18, 0)
Ag = Elements('Prata', 47, 'Ag', 107.9, 11, 2, 8, 18, 18, 1, 0, 2, 2, 8, 18,
              18, 1)
# Continuação das declarações de objetos para mais elementos químicos
Cd = Elements('Cádmio', 48, 'Cd', 112.4, 12, 2, 8, 18, 18, 2, 0, 2, 2, 8, 18,
              18, 2)
In = Elements('Índio', 49, 'In', 114.8, 13, 2, 8, 18, 18, 3, 0, 2, 2, 8, 18,
              18, 3)
Sn = Elements('Estanho', 50, 'Sn', 118.7, 14, 2, 8, 18, 18, 4, 0, 2, 2, 8, 18,
              18, 4)
Sb = Elements('Antimônio', 51, 'Sb', 121.8, 15, 2, 8, 18, 18, 5, 0, 2, 2, 8,
              18, 18, 5)
Te = Elements('Telúrio', 52, 'Te', 127.6, 16, 2, 8, 18, 18, 6, 0, 2, 2, 8, 18,
              18, 6)
I = Elements('Iodo', 53, 'I', 126.9, 17, 2, 8, 18, 18, 7, 0, 2, 2, 8, 18, 18,
             7)
Xe = Elements('Xenônio', 54, 'Xe', 131.3, 18, 2, 8, 18, 18, 8, 0, 2, 2, 8, 18,
              18, 8)
Cs = Elements('Césio', 55, 'Cs', 132.9, 1, 2, 8, 18, 18, 8, 1, 2, 2, 8, 18, 18,
              8)
Ba = Elements('Bário', 56, 'Ba', 137.3, 2, 2, 8, 18, 18, 8, 2, 2, 2, 8, 18, 18,
              8)
La = Elements('Lantânio', 57, 'La', 138.9, 3, 2, 8, 18, 18, 9, 2, 2, 2, 8, 18,
              18, 9)
Ce = Elements('Cério', 58, 'Ce', 140.1, 3, 2, 8, 18, 19, 9, 2, 2, 2, 8, 18, 19,
              9)
Pr = Elements('Praseodímio', 59, 'Pr', 140.9, 3, 2, 8, 18, 21, 8, 0, 2, 2, 8,
              18, 21, 8)
Nd = Elements('Neodímio', 60, 'Nd', 144.2, 3, 2, 8, 18, 22, 8, 0, 2, 2, 8, 18,
              22, 8)
Pm = Elements('Promécio', 61, 'Pm', 145.0, 3, 2, 8, 18, 23, 8, 0, 2, 2, 8, 18,
              23, 8)
Sm = Elements('Samário', 62, 'Sm', 150.4, 3, 2, 8, 18, 24, 8, 0, 2, 2, 8, 18,
              24, 8)
Eu = Elements('Európio', 63, 'Eu', 152.0, 3, 2, 8, 18, 25, 8, 0, 2, 2, 8, 18,
              25, 8)
Gd = Elements('Gadolínio', 64, 'Gd', 157.3, 3, 2, 8, 18, 25, 9, 0, 2, 2, 8, 18,
              25, 9)
Tb = Elements('Térbio', 65, 'Tb', 158.9, 3, 2, 8, 18, 27, 8, 0, 2, 2, 8, 18,
              27, 8)
Dy = Elements('Disprósio', 66, 'Dy', 162.5, 3, 2, 8, 18, 28, 8, 0, 2, 2, 8, 18,
              28, 8)
Ho = Elements('Hólmio', 67, 'Ho', 164.9, 3, 2, 8, 18, 29, 8, 0, 2, 2, 8, 18,
              29, 8)
Er = Elements('Érbio', 68, 'Er', 167.3, 3, 2, 8, 18, 30, 8, 0, 2, 2, 8, 18, 30,
              8)
Tm = Elements('Túlio', 69, 'Tm', 168.9, 3, 2, 8, 18, 31, 8, 0, 2, 2, 8, 18, 31,
              8)
Yb = Elements('Itérbio', 70, 'Yb', 173.0, 3, 2, 8, 18, 32, 8, 0, 2, 2, 8, 18,
              32, 8)
Lu = Elements('Lutécio', 71, 'Lu', 175.0, 3, 2, 8, 18, 32, 9, 0, 2, 2, 8, 18,
              32, 9)
Hf = Elements('Háfnio', 72, 'Hf', 178.5, 4, 2, 8, 18, 32, 10, 0, 2, 2, 8, 18,
              32, 10)
Ta = Elements('Tântalo', 73, 'Ta', 180.9, 5, 2, 8, 18, 32, 11, 0, 2, 2, 8, 18,
              32, 11)
W = Elements('Tungstênio', 74, 'W', 183.8, 6, 2, 8, 18, 32, 12, 0, 2, 2, 8, 18,
             32, 12)
Re = Elements('Rênio', 75, 'Re', 186.2, 7, 2, 8, 18, 32, 13, 0, 2, 2, 8, 18,
              32, 13)
Os = Elements('Ósmio', 76, 'Os', 190.2, 8, 2, 8, 18, 32, 14, 0, 2, 2, 8, 18,
              32, 14)
Ir = Elements('Irídio', 77, 'Ir', 192.2, 9, 2, 8, 18, 32, 15, 0, 2, 2, 8, 18,
              32, 15)
Pt = Elements('Platina', 78, 'Pt', 195.1, 10, 2, 8, 18, 32, 17, 0, 2, 2, 8, 18, 32, 17)
Au = Elements('Ouro', 79, 'Au', 197.0, 11, 2, 8, 18, 32, 18, 0, 2, 2, 8, 18,
              32, 18)
Hg = Elements('Mercúrio', 80, 'Hg', 200.6, 12, 2, 8, 18, 32, 18, 2, 2, 2, 8,
              18, 32, 18)
Tl = Elements('Tálio', 81, 'Tl', 204.4, 13, 2, 8, 18, 32, 18, 3, 2, 2, 8, 18,
              32, 18)
Pb = Elements('Chumbo', 82, 'Pb', 207.2, 14, 2, 8, 18, 32, 18, 4, 2, 2, 8, 18,
              32, 18)
Bi = Elements('Bismuto', 83, 'Bi', 208.9, 15, 2, 8, 18, 32, 18, 5, 2, 2, 8, 18,32, 18)
Th = Elements('Tório', 90, 'Th', 232.0, 3, 2, 8, 18, 32, 18, 10, 2, 2, 8, 18,
              32, 18)
Pa = Elements('Protactínio', 91, 'Pa', 231.0, 3, 2, 8, 18, 32, 20, 9, 2, 2, 8,
              18, 32, 20)
U = Elements('Urânio', 92, 'U', 238.0, 3, 2, 8, 18, 32, 21, 9, 2, 2, 8, 18, 32,
             21)
Np = Elements('Neptúnio', 93, 'Np', 237.0, 3, 2, 8, 18, 32, 22, 9, 2, 2, 8, 18,
              32, 22)
Pu = Elements('Plutônio', 94, 'Pu', 244.0, 3, 2, 8, 18, 32, 24, 8, 2, 2, 8, 18,
              32, 24)
Am = Elements('Amerício', 95, 'Am', 243.0, 3, 2, 8, 18, 32, 25, 8, 2, 2, 8, 18,
              32, 25)
Cm = Elements('Cúrio', 96, 'Cm', 247.0, 3, 2, 8, 18, 32, 25, 9, 2, 2, 8, 18,
              32, 25)
Bk = Elements('Berquélio', 97, 'Bk', 247.0, 3, 2, 8, 18, 32, 27, 8, 2, 2, 8,
              18, 32, 27)
Cf = Elements('Califórnio', 98, 'Cf', 251.0, 3, 2, 8, 18, 32, 28, 8, 2, 2, 8,
              18, 32, 28)
Es = Elements('Einstênio', 99, 'Es', 252.0, 3, 2, 8, 18, 32, 29, 8, 2, 2, 8,
              18, 32, 29)
Fm = Elements('Férmio', 100, 'Fm', 257.0, 3, 2, 8, 18, 32, 30, 8, 2, 2, 8, 18,
              32, 30)
Md = Elements('Mendelévio', 101, 'Md', 258.0, 3, 2, 8, 18, 32, 31, 8, 2, 2, 8,
              18, 32, 31)
No = Elements('Nobélio', 102, 'No', 259.0, 3, 2, 8, 18, 32, 32, 8, 2, 2, 8, 18,
              32, 32)
Lr = Elements('Laurêncio', 103, 'Lr', 262.0, 3, 2, 8, 18, 32, 32, 8, 2, 2, 8,
              18, 32, 32)
