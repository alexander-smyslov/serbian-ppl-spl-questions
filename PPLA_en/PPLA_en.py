
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
    parser.append(QParser('Air law.pdf', 'Air law', '^{number}\\.', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 79))
    parser.append(QParser('Aircraft  General Knowledge.pdf', 'Aircraft General Knowledge', '^{number}\\.', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 150))
    parser.append(QParser('Flight performance and planning.pdf', 'Flight Performance', '^{number}\\.', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 148))
    parser.append(QParser('Human performance.pdf', 'Human performance and limitations', '^{number}\\.', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 150))
    parser.append(QParser('Metheorology.pdf','Meteorology', '^{number}\\.', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 150))
    parser.append(QParser('Navigation.pdf', 'Navigation', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 138))
    parser.append(QParser('Operational procedures.pdf', 'Operational procedures', '^{number}\\.', '^a\\.', '^b\\.', '^c\\.', '^d\\.',150))
    parser.append(QParser('Principles of Flight.pdf', 'Principles of Flight', '^{number}\\.', '^a\\.', '^b\\.', '^c\\.', '^d\\.',150))
    parser.append(QParser('Comunication.pdf', 'Communication', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.',137))


    with open(ff, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['number','question', 'a','b','c','d','right_answer','category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel', delimiter = ';',  quotechar = '"', quoting=csv.QUOTE_ALL)
        for p in parser:
            p.parse_lines(5, False, True)
            p.parse(writer)

