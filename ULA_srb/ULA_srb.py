
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
    parser.append(QParser('ULA  -  Opste znanje o vazduhoplovu-motorni zmaj.pdf', 'Opste znanje o vazduhoplovu-motorni zmaj', 'num_abcd_bracert', 110,  2, 15, -1, 30, 750))
    parser.append(QParser('ULA  -  Opste znanje o vazduhoplovu.pdf', 'Opste znanje o vazduhoplovu', 'num_abcd_bracert', 98, 2, 14, -1, 30, 750))
    parser.append(QParser('ULA  -  Performanse leta i planiranje.pdf', 'Performanse leta i planiranje', 'num_abcd_bracert', 27,2, 5, -1, 30, 750))
    #parser.append(QParser('ULA  -  Ljudske mogucnosti i ogranicenja.pdf ', 'Ljudske mogucnosti', 'num_1234', 81, 2, 11, -1, 30, 750))
    #parser.append(QParser('ULA  -  Meteorologija.pdf','Meteorologija', 'num_abcd_bracert', 110 ,2, 14, -1, 30, 750))
    #parser.append(QParser('ULA  -  Navigacija.pdf', 'Navigacija', 'num_abcd', 145,2, 50, -1, 30, 750))
    #parser.append(QParser('ULA  -  Teorija letenja.pdf', 'Teorija letenja', 'num_abcd', 60, 2, 50, -1, 30, 750))
    #parser.append(QParser('ULA  -  Komunikacije.pdf', 'Komunikacije', 'num_wo_1234',45, 2, 8, -1, 30, 750)) # 45


    with open(ff, 'w', newline='', encoding='utf-8') as csvfile:
        for p in parser:
            p.parse_lines(10)
            p.parse(csvfile)

