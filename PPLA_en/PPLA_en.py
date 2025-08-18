
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
    parser.append(QParser('Air law.pdf', 'Air law', 'num_abcd', 79,2, 10, -1, 30, 750))
    parser.append(QParser('Aircraft  General Knowledge.pdf', 'Aircraft General Knowledge', 'num_abcd', 150,2, 17, -1, 30, 750))
    parser.append(QParser('Flight performance and planning.pdf', 'Flight Performance', 'num_abcd', 148,2, 50, -1, 30, 750))
    parser.append(QParser('Human performance.pdf', 'Human performance and limitations', 'num_abcd', 150,2, 50, -1, 30, 750))
    parser.append(QParser('Metheorology.pdf','Meteorology', 'num_abcd', 150,2, 50, -1, 30, 750))
    parser.append(QParser('Navigation.pdf', 'Navigation', 'num_abcd', 138,2, 50, -1, 30, 750))
    parser.append(QParser('Operational procedures.pdf', 'Operational procedures', 'num_abcd',150,2, 50, -1, 30, 750))
    parser.append(QParser('Principles of Flight.pdf', 'Principles of Flight', 'num_abcd',150,2, 50, -1, 30, 750))
    parser.append(QParser('Comunication.pdf', 'Communication', 'num_abcd',137,2, 50, -1, 30, 750))


    with open(ff, 'w', newline='', encoding='utf-8') as csvfile:
        for p in parser:
            p.parse_lines(5)
            p.parse(csvfile)

