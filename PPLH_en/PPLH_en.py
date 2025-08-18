
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
    parser.append(QParser('H1.Air law.pdf', 'Air law', 'num_abcd', 150))
    parser.append(QParser('H2.Aircraft General Knowledge.pdf', 'Aircraft General Knowledge', 'num_abcd', 136))
    parser.append(QParser('H3.Flight Performance.pdf', 'Flight Performance', 'num_abcd', 158))
    parser.append(QParser('H4.Human performance and limitations.pdf', 'Human performance and limitations', 'num_1234_bracert', 150))
    parser.append(QParser('H5.Meteorology.pdf','Meteorology', 'num_abcd', 150))
    parser.append(QParser('H6.Navigation.pdf', 'Navigation', 'num_abcd', 150))
    parser.append(QParser('H7.Operational procedures.pdf', 'Operational procedures', 'num_wo_abcd' ,110))
    parser.append(QParser('H8.Principles of Flight.pdf', 'Principles of Flight', 'num_abcd',151))
    parser.append(QParser('H9.Communications.pdf', 'Communications', 'num_abcd',150))

    with open(ff, 'w', newline='', encoding='utf-8') as csvfile:
        for p in parser:
            p.parse_lines()
            p.parse(csvfile)

