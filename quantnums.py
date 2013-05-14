########################################################
# Quantum Numbers to Element Finder
# Written by Brian Guadalupe
# May 4, 2013
# Finds the element given the quantum numbers:
# n = principal quantum number
# l = orbital quantum number (s=0 p=1 d=2 f=3)
# m  = magnetic quantum number
#  l
# m  = spin quantum number (-1/2=paired 1/2=unpaired)
#  s
#
# For example:
# python quantnums.py 3 1 0 +1/2
########################################################

from __future__ import division
import sys
 
arrows = 0
atnum = {'Ru': 44, 'Re': 75, 'Rf': 104, 'Rg': 111, 'Ra': 88, 'Rb': 37, 'Rn': 86, 'Rh': 45, 'Be': 4, 'Ba': 56, 'Bh': 107, 'Bi': 83, 'Bk': 97, 'Br': 35, 'H': 1, 'P': 15, 'Os': 76, 'Es': 99, 'Hg': 80, 'Ge': 32, 'Gd': 64, 'Ga': 31, 'Pr': 59, 'Pt': 78, 'Pu': 94, 'C': 6, 'Pb': 82, 'Pa': 91, 'Pd': 46, 'Cd': 48, 'Po': 84, 'Pm': 61, 'Hs': 108, 'Uup': 115, 'Uus': 117, 'Ho': 67, 'Hf': 72, 'K': 19, 'He': 2, 'Md': 101, 'Mg': 12, 'Mo': 42, 'Mn': 25, 'O': 8, 'Mt': 109, 'S': 16, 'W': 74, 'Zn': 30, 'Eu': 63, 'Zr': 40, 'Er': 68, 'Ni': 28, 'No': 102, 'Na': 11, 'Nb': 41, 'Nd': 60, 'Ne': 10, 'Np': 93, 'Fr': 87, 'Fe': 26, 'Fl': 114, 'Fm': 100, 'B': 5, 'F': 9, 'Sr': 38, 'N': 7, 'Kr': 36, 'Si': 14, 'Sn': 50, 'Sm': 62, 'V': 23, 'Sc': 21, 'Sb': 51, 'Sg': 106, 'Se': 34, 'Co': 27, 'Cn': 112, 'Cm': 96, 'Cl': 17, 'Ca': 20, 'Cf': 98, 'Ce': 58, 'Xe': 54, 'Lu': 71, 'Cs': 55, 'Cr': 24, 'Cu': 29, 'La': 57, 'Li': 3, 'Lv': 116, 'Tl': 81, 'Tm': 69, 'Lr': 103, 'Th': 90, 'Ti': 22, 'Te': 52, 'Tb': 65, 'Tc': 43, 'Ta': 73, 'Yb': 70, 'Db': 105, 'Dy': 66, 'Ds': 110, 'I': 53, 'U': 92, 'Y': 39, 'Ac': 89, 'Ag': 47, 'Uut': 113, 'Ir': 77, 'Am': 95, 'Al': 13, 'As': 33, 'Ar': 18, 'Au': 79, 'At': 85, 'In': 49, 'Uuo': 118}
spdf = ""
sym = ""
symlist = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Uut', 'Fl', 'Uup', 'Lv', 'Uus', 'Uuo']
symnums = ['s1', 's2', 's1', 's2', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 's1', 's2', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 's1', 's2', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 's1', 's2', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 's1', 's2', 'd1', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 's1', 's2', 'd1', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6']
tuples = [('H', '1s1'), ('He', '1s2'), ('Li', '2s1'), ('Be', 's2'), ('B', 'p1'), ('C', 'p2'), ('N', 'p3'), ('O', 'p4'), ('F', 'p5'), ('Ne', 'p6'), ('Na', 's1'), ('Mg', 's2'), ('Al', 'p1'), ('Si', 'p2'), ('P', 'p3'), ('S', 'p4'), ('Cl', 'p5'), ('Ar', 'p6'), ('K', 's1'), ('Ca', 's2'), ('Sc', 'd1'), ('Ti', 'd2'), ('V', 'd3'), ('Cr', 'd4'), ('Mn', 'd5'), ('Fe', 'd6'), ('Co', 'd7'), ('Ni', 'd8'), ('Cu', 'd9'), ('Zn', 'd10'), ('Ga', 'p1'), ('Ge', 'p2'), ('As', 'p3'), ('Se', 'p4'), ('Br', 'p5'), ('Kr', 'p6'), ('Rb', 's1'), ('Sr', 's2'), ('Y', 'd1'), ('Zr', 'd2'), ('Nb', 'd3'), ('Mo', 'd4'), ('Tc', 'd5'), ('Ru', 'd6'), ('Rh', 'd7'), ('Pd', 'd8'), ('Ag', 'd9'), ('Cd', 'd10'), ('In', 'p1'), ('Sn', 'p2'), ('Sb', 'p3'), ('Te', 'p4'), ('I', 'p5'), ('Xe', 'p6'), ('Cs', 's1'), ('Ba', 's2'), ('La', 'd1'), ('Ce', 'f1'), ('Pr', 'f2'), ('Nd', 'f3'), ('Pm', 'f4'), ('Sm', 'f5'), ('Eu', 'f6'), ('Gd', 'f7'), ('Tb', 'f8'), ('Dy', 'f9'), ('Ho', 'f10'), ('Er', 'f11'), ('Tm', 'f12'), ('Yb', 'f13'), ('Lu', 'f14'), ('Hf', 'd2'), ('Ta', 'd3'), ('W', 'd4'), ('Re', 'd5'), ('Os', 'd6'), ('Ir', 'd7'), ('Pt', 'd8'), ('Au', 'd9'), ('Hg', 'd10'), ('Tl', 'p1'), ('Pb', 'p2'), ('Bi', 'p3'), ('Po', 'p4'), ('At', 'p5'), ('Rn', 'p6'), ('Fr', 's1'), ('Ra', 's2'), ('Ac', 'd1'), ('Th', 'f1'), ('Pa', 'f2'), ('U', 'f3'), ('Np', 'f4'), ('Pu', 'f5'), ('Am', 'f6'), ('Cm', 'f7'), ('Bk', 'f8'), ('Cf', 'f9'), ('Es', 'f10'), ('Fm', 'f11'), ('Md', 'f12'), ('No', 'f13'), ('Lr', 'f14'), ('Rf', 'd2'), ('Db', 'd3'), ('Sg', 'd4'), ('Bh', 'd5'), ('Hs', 'd6'), ('Mt', 'd7'), ('Ds', 'd8'), ('Rg', 'd9'), ('Cn', 'd10'), ('Uut', 'p1'), ('Fl', 'p2'), ('Uup', 'p3'), ('Lv', 'p4'), ('Uus', 'p5'), ('Uuo', 'p6')]
symdict = {'6s1': 'Cs', '6s2': 'Ba', '3p1': 'Al', '3p2': 'Si', '3p3': 'P', '3p4': 'S', '3p5': 'Cl', '3p6': 'Ar', '2s2': 'Be', '6p5': 'At', '6p4': 'Po', '6p6': 'Rn', '6p1': 'Tl', '6p3': 'Bi', '6p2': 'Pb', '3s1': 'Na', '3s2': 'Mg', '4f9': 'Dy', '4f8': 'Tb', '4f5': 'Sm', '4f4': 'Pm', '4f7': 'Gd', '4f6': 'Eu', '4f1': 'Ce', '2s1': 'Li', '4f3': 'Nd', '4f2': 'Pr', '6d7': 'Mt', '7s1': 'Fr', '7s2': 'Ra', '5p6': 'Xe', '5p4': 'Te', '5p5': 'I', '5p2': 'Sn', '5p3': 'Sb', '5p1': 'In', '2p1': 'B', '2p3': 'N', '2p2': 'C', '2p5': 'F', '2p4': 'O', '2p6': 'Ne', '5f8': 'Bk', '5f9': 'Cf', '5f1': 'Th', '5f2': 'Pa', '5f3': 'U', '5f4': 'Np', '5f5': 'Pu', '5f6': 'Am', '5f7': 'Cm', '4f11': 'Er', '4f10': 'Ho', '4f13': 'Yb', '4f12': 'Tm', '4f14': 'Lu', '4p6': 'Kr', '4p5': 'Br', '4p4': 'Se', '4p3': 'As', '4p2': 'Ge', '4p1': 'Ga', '6d10': 'Cn', '5f12': 'Md', '5f13': 'No', '5f10': 'Es', '5f11': 'Fm', '5f14': 'Lr', '5d2': 'Hf', '3d5': 'Mn', '3d6': 'Fe', '5d1': 'La', '5d6': 'Os', '5d7': 'Ir', '5d4': 'W', '5d5': 'Re', '5d8': 'Pt', '5d9': 'Au', '3d8': 'Ni', '3d9': 'Cu', '1s2': 'He', '1s1': 'H', '6d1': 'Ac', '6d3': 'Db', '6d2': 'Rf', '6d5': 'Bh', '6d4': 'Sg', '3d10': 'Zn', '6d6': 'Hs', '6d9': 'Rg', '6d8': 'Ds', '3d4': 'Cr', '5d3': 'Ta', '3d7': 'Co', '3d1': 'Sc', '3d2': 'Ti', '3d3': 'V', '5s2': 'Sr', '5s1': 'Rb', '4s2': 'Ca', '4s1': 'K', '7p4': 'Lv', '7p5': 'Uus', '7p6': 'Uuo', '7p1': 'Uut', '7p2': 'Fl', '7p3': 'Uup', '4d9': 'Ag', '4d8': 'Pd', '4d3': 'Nb', '4d2': 'Zr', '4d1': 'Y', '4d7': 'Rh', '4d6': 'Ru', '4d5': 'Tc', '4d4': 'Mo', '5d10': 'Hg', '4d10': 'Cd'}
row18 = [('He', 2), ('Ne', 10), ('Ar', 18), ('Kr', 36), ('Xe', 54), ('Rn', 86)]


n = int(sys.argv[1])
l = int(sys.argv[2])
m = int(sys.argv[3])
s = sys.argv[4]

if l == 0:
   spdf = "s"
elif l == 1:
   spdf = "p"
elif l == 2:
   spdf = "d"
elif l == 3:
   spdf = "f"
else:
   print "Argument 'l' is invalid"


if l == 0:
   if s == 1 / 2:
      arrows = 1
   else:
      arrows = 2
elif l == 1:
   if s == 1 / 2:
      arrows = m + 2
   else:
      arrows = m + 5
elif l == 2:
   if s == 1 / 2:
      arrows = m + 3
   else:
      arrows = m + 8
elif l == 3:
   if s == 1 / 2:
      arrows = m + 4
   else:
      arrows = m + 11
else:
   print "Arguments 'l' & 's' are invalid"  

lvl = str(n) + spdf + str(arrows)

def getElement(lvl):
        return symdict[lvl]

def getAtomicNum(sym):
        return atnum[sym]

print "\nThe element is: "
if getAtomicNum(getElement(lvl)) >= 100:
        print "   " + getElement(lvl)
elif getAtomicNum(getElement(lvl)) < 10:
        print " " + getElement(lvl)
else:
        print "  " + getElement(lvl)
print getAtomicNum(getElement(lvl))

