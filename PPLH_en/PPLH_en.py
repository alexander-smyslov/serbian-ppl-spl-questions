
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
    parser.append(QParser('H1.Air law.pdf', 'Air law', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 150))
    parser.append(QParser('H2.Aircraft General Knowledge.pdf', 'Aircraft General Knowledge', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 136))
    parser.append(QParser('H3.Flight Performance.pdf', 'Flight Performance', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 158))
    parser.append(QParser('H4.Human performance and limitations.pdf', 'Human performance and limitations', '^{number}\\.', '^1\\) ', '^2\\) ', '^3\\) ', '^4\\) ', 150))
    parser.append(QParser('H5.Meteorology.pdf','Meteorology', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 150))
    parser.append(QParser('H6.Navigation.pdf', 'Navigation', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.', 150))
    parser.append(QParser('H7.Operational procedures.pdf', 'Operational procedures', '^{number}\\.', '^a\\.', '^b\\.', '^c\\.', '^d\\.',110))
    parser.append(QParser('H8.Principles of Flight.pdf', 'Principles of Flight', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.',151))
    parser.append(QParser('H9.Communications.pdf', 'Communications', '^{number}\\. ', '^a\\.', '^b\\.', '^c\\.', '^d\\.',150))

    with open(ff, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['number','question', 'a','b','c','d','right_answer','category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel', delimiter = ';',  quotechar = '"', quoting=csv.QUOTE_ALL)
        for p in parser:
            p.parse(writer)

