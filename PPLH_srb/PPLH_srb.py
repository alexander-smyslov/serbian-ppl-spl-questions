
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
    parser.append(QParser('H1.Vazduhoplovni propisi.pdf', 'Vazduhoplovni propisi', 'num_abcd', 150))
    parser.append(QParser('H2.Poznavanje vazduhoplova.pdf', 'Poznavanje vazduhoplova', 'num_abcd', 136))
    parser.append(QParser('H3.Performanse leta.pdf', 'Performanse leta i planiranje', 'num_abcd', 158))
    parser.append(QParser('H4.Ljudske mogucnosti.pdf', 'Ljudske mogucnosti', 'num_1234_bracert', 150))
    parser.append(QParser('H5.Meteorologija.pdf','Meteorologija', 'num_abcd', 150))
    parser.append(QParser('H6.Navigacija.pdf', 'Navigacija', 'num_abcd', 150))
    parser.append(QParser('H7.Operativne procedure.pdf', 'Operativne Procedure', 'num_wo_abcd',110))
    parser.append(QParser('H8.Teorija letenja.pdf', 'Teorija letenja', 'num_abcd',151))
    parser.append(QParser('H9.Komunikacije.pdf', 'Komunikacije', 'num_abcd',150))

    with open(ff, 'w', newline='', encoding='utf-8') as csvfile:
        for p in parser:
            p.parse_lines()
            p.parse(csvfile)

