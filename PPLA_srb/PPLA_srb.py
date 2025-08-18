
import sys
import os
import csv

from parser.parser import QParser, clean_dir

sys.stdout.reconfigure(encoding='utf-8')

if __name__ == '__main__':
    ff = '1.csv'
    if os.path.exists(ff):
        os.remove(ff)

    clean_dir()

    parser = []
    parser.append(QParser('Vazduhoplovni_propisi.pdf', 'Vazduhoplovni propisi', 'num_abcd', 57,2, 50, -1, 30, 750))
    parser.append(QParser('Poznavanje_vazduhoplova.pdf', 'Poznavanje vazduhoplova', 'num_abcd', 136,2, 50, -1, 30, 750))
    parser.append(QParser('Performanse_i_planiranje_leta.pdf', 'Performanse leta i planiranje', 'num_abcd', 137,2, 50, -1, 30, 750))
    parser.append(QParser('Ljudske_mogucnosti.pdf', 'Ljudske mogucnosti', 'num_abcd', 150,2, 50, -1, 30, 750))
    parser.append(QParser('Meteorologija.pdf','Meteorologija', 'num_abcd', 144,2, 50, -1, 30, 750))
    parser.append(QParser('Navigacija.pdf', 'Navigacija', 'num_abcd', 145,2, 50, -1, 30, 750))
    parser.append(QParser('Operativne_procedure.pdf', 'Operativne Procedure', 'num_abcd',146,2, 50, -1, 30, 750))
    parser.append(QParser('Teorija_letenja.pdf', 'Teorija letenja', 'num_abcd',149,2, 50, -1, 30, 750))
    #parser.append(QParser('Komunikacije.pdf', 'Komunikacije', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.',150))


    with open(ff, 'w', newline='', encoding='utf-8') as csvfile:
        for p in parser:
            p.parse_lines(5)
            p.parse(csvfile)

