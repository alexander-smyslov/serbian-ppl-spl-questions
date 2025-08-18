
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
    #+parser.append(QParser('Air law.pdf', 'Air law', 'num_wo_abcd', 79))
    #parser.append(QParser('AGK SPL.pdf', 'Aircraft General Knowledge', 'num_1234', 40))
    #parser.append(QParser('FPL-PERF SPL.pdf', 'Flight Planing and Performance', 'num_1234', 30))
    #parser.append(QParser('Human performance.pdf', 'Human performance and limitations', 'num_1234_bracert', 150))
    #+ parser.append(QParser('Metheorology.pdf','Metheorology', 'num_abcd', 150))
    parser.append(QParser('NAV SPL.pdf', 'Navigation', 'num_1234', 41))
    #parser.append(QParser('OPS SPL.pdf', 'Operational procedures', 'num_1234',102))
    #parser.append(QParser('POF SPL.pdf', 'Principles of Flight', 'num_1234',47))
    #parser.append(QParser('Comunication.pdf', 'Comunication', 'num_abcd',150))

    with open(ff, 'w', newline='', encoding='utf-8') as csvfile:
        for p in parser:
            p.parse_lines(5)
            p.parse(csvfile)


 
          
