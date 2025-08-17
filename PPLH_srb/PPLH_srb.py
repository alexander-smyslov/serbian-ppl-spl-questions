
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
    parser.append(QParser('H1.Vazduhoplovni propisi.pdf', 'Vazduhoplovni propisi', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 150))
    parser.append(QParser('H2.Poznavanje vazduhoplova.pdf', 'Poznavanje vazduhoplova', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 136))
    parser.append(QParser('H3.Performanse leta.pdf', 'Performanse leta i planiranje', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 158))
    parser.append(QParser('H4.Ljudske mogucnosti.pdf', 'Ljudske mogucnosti', '^{number}\\.', '^1\\) ', '^2\\) ', '^3\\) ', '^4\\) ', 150))
    parser.append(QParser('H5.Meteorologija.pdf','Meteorologija', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 150))
    parser.append(QParser('H6.Navigacija.pdf', 'Navigacija', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 150))
    parser.append(QParser('H7.Operativne procedure.pdf', 'Operativne Procedure', '^{number}\\.', '^a\\.', '^b\\.', '^c\\.', '^d\\.',110))
    parser.append(QParser('H8.Teorija letenja.pdf', 'Teorija letenja', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.',151))
    parser.append(QParser('H9.Komunikacije.pdf', 'Komunikacije', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.',150))

    with open(ff, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['number','question', 'a','b','c','d','right_answer','category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel', delimiter = ';',  quotechar = '"', quoting=csv.QUOTE_ALL)
        for p in parser:
            p.parse(writer)

