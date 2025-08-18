
import sys
import os

from parser.parser import QParser, clean_dir

sys.stdout.reconfigure(encoding='utf-8')

if __name__ == '__main__':
    ff = '1.csv'
    if os.path.exists(ff):
        os.remove(ff)

    clean_dir()

    parser = []
    parser.append(QParser('S1.Vazduhoplovni propisi-.pdf', 'Vazduhoplovni propisi', 'num_abcd', 150, 2, 25, -1, 30, 750))
    parser.append(QParser('S2.Opste znanje o vazduhoplovu.pdf', 'Opste znanje o vazduhoplovu', 'num_1234', 40, 2, 6, 11, 30, 750))
    parser.append(QParser('S3.Performanse leta i planiranje.pdf', 'Performanse leta i planiranje', 'num_1234', 30, 2, 5, 7, 30, 750))
    parser.append(QParser('S4.Ljudske mogucnosti.pdf', 'Ljudske mogucnosti', 'num_1234_bracert', 150, 2, 22, -1, 30, 750))
    parser.append(QParser('S5.Meteorologija.pdf','Meteorologija', 'num_abcd', 150, 2, 26, -1, 30, 750))
    parser.append(QParser('S6.Navigacija.pdf', 'Navigacija', 'num_1234', 41, 2, 6, 9, 30, 750))
    parser.append(QParser('S7.Operativne Procedure.pdf', 'Operativne Procedure', 'num_1234',102, 2, 14,15, 30, 800))
    parser.append(QParser('S8.Teorija letenja.pdf', 'Teorija letenja', 'num_1234',47, 2, 7, 15, 30, 800))
    parser.append(QParser('S9.Komunikacije.pdf', 'Komunikacije', 'num_abcd',150, 2, 22, -1, 30, 750))

    with open(ff, 'w', newline='', encoding='utf-8') as csvfile:
        for p in parser:
            p.parse_lines()
            p.parse(csvfile)


 
          
