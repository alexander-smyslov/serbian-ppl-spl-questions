
import sys
import os
import csv
import shutil

from parser.parser import QParser, clean_dir

sys.stdout.reconfigure(encoding='utf-8')

if __name__ == '__main__':
    ff = '1.csv'
    if os.path.exists(ff):
        os.remove(ff)

    clean_dir()

    parser = []
    parser.append(QParser('S1.Vazduhoplovni propisi-.pdf', 'Vazduhoplovni propisi', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 150))
    parser.append(QParser('S2.Opste znanje o vazduhoplovu.pdf', 'Opste znanje o vazduhoplovu', '^{number} - ', '^1\\. ', '^2\\. ', '^3\\. ', '^4\\. ', 40))
    parser.append(QParser('S3.Performanse leta i planiranje.pdf', 'Performanse leta i planiranje', '^{number} - ', '^1\\. ', '^2\\. ', '^3\\. ', '^4\\. ', 30))
    parser.append(QParser('S4.Ljudske mogucnosti.pdf', 'Ljudske mogucnosti', '^{number}\\.', '^1\\) ', '^2\\) ', '^3\\) ', '^4\\) ', 150))
    parser.append(QParser('S5.Meteorologija.pdf','Meteorologija', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 150))
    parser.append(QParser('S6.Navigacija.pdf', 'Navigacija', '^{number} - ', '^1\\. ', '^2\\. ', '^3\\. ', '^4\\. ', 41))
    parser.append(QParser('S7.Operativne Procedure.pdf', 'Operativne Procedure', '^{number} - ', '^1\\. ', '^2\\. ', '^3\\. ', '^4\\. ',102))
    parser.append(QParser('S8.Teorija letenja.pdf', 'Teorija letenja', '^{number} - ', '^1\\. ', '^2\\. ', '^3\\. ', '^4\\. ',47))
    parser.append(QParser('S9.Komunikacije.pdf', 'Komunikacije', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.',150))

    with open(ff, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['number','question', 'a','b','c','d','right_answer','category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel', delimiter = ';',  quotechar = '"', quoting=csv.QUOTE_ALL)
        for p in parser:
            p.parse_lines()
            p.parse(writer)


 
          
