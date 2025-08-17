
import sys
import os
import csv

from parser.parser import QParser

sys.stdout.reconfigure(encoding='utf-8')

if __name__ == '__main__':
    ff = '1.csv'
    if os.path.exists(ff):
        os.remove(ff)

    parser = []
    parser.append(QParser('Vazduhoplovni_propisi.pdf', 'Vazduhoplovni propisi', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 57))
    parser.append(QParser('Poznavanje_vazduhoplova.pdf', 'Poznavanje vazduhoplova', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 136))
    parser.append(QParser('Performanse_i_planiranje_leta.pdf', 'Performanse leta i planiranje', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 137))
    parser.append(QParser('Ljudske_mogucnosti.pdf', 'Ljudske mogucnosti', '^{number}\\.', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 150))
    parser.append(QParser('Meteorologija.pdf','Meteorologija', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 144))
    parser.append(QParser('Navigacija.pdf', 'Navigacija', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 145))
    parser.append(QParser('Operativne_procedure.pdf', 'Operativne Procedure', '^{number}\\.', '^a\\.', '^b\\.', '^c\\.', '^d\\.',146))
    parser.append(QParser('Teorija_letenja.pdf', 'Teorija letenja', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.',149))
    #parser.append(QParser('Komunikacije.pdf', 'Komunikacije', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.',150))


    with open(ff, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['number','question', 'a','b','c','d','right_answer','category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel', delimiter = ';',  quotechar = '"', quoting=csv.QUOTE_ALL)
        for p in parser:
            p.parse_lines(5, False, True)
            p.parse(writer)

