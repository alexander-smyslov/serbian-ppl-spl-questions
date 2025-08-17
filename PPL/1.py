import json
import sys
import re
import os
import csv
import pymupdf


sys.stdout.reconfigure(encoding='utf-8')

# Open and read the JSON file
with open('1.json', 'r', encoding='utf-8') as file:
    data = json.load(file)



theme = {}
theme['rules'] ='Vazduhoplovni propisi';
theme['komunication'] ='Komunikacije';
theme['limits'] ='Ljudske mogucnosti';
theme['meteo'] ='Meteorologija';
theme['nav'] ='Navigacija';
theme['operproc'] ='Operativne Procedure';
theme['perfom'] ='Performanse leta i planiranje';
theme['aircraft'] ='Opste znanje o vazduhoplovu';
theme['princflight'] ='Teorija letenja';



qes_to_cat = {}
qes_answer = {}
qes_right = {}

for c in data['test']:
    qu = c['question'].rstrip()
    an = c['answer'].rstrip()

    qes_to_cat[qu]=c['t']
    if qu not in qes_answer:
        qes_answer[qu]=[]
    qes_answer[qu].append(an)
    if c['correct']:
        qes_right[qu] = an
    #print(cosponsor)
    #print('\n----\n')

n = 1
with open('1.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['number','question', 'a','b','c','d','right_answer','category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel', delimiter = ';',  quotechar = '"', quoting=csv.QUOTE_ALL)
    for key, value in qes_answer.items():
        x = len(value)
        answer1 = ''
        answer2 = ''
        answer3 = ''
        answer4 = ''
        cat = qes_to_cat[key]
        kkey = key.replace('\n', '\\n')
        right = qes_right[qu]
        right_ = 'A'
    
        if x > 0: 
            answer1 = value[0].replace('\n', '\\n')
            if value[0] == right: 
                right_ = 'A'
        if x > 1: 
            answer2 = value[1].replace('\n', '\\n')
            if value[1] == right: 
                right_ = 'B'
        if x > 2: 
            answer3 = value[2].replace('\n', '\\n')
            if value[2] == right: 
                right_ = 'C'
        if x > 3: 
            answer4 = value[3].replace('\n', '\\n')
            if value[3] == right: 
                right_ = 'D'
    
        right = qes_right[qu]
        writer.writerow({'number': n,'question': kkey, 'a': answer1 ,'b': answer2 ,'c': answer3 ,'d': answer4 ,'right_answer': right_ , 'category': cat});

        print(f'"{kkey}"; "{answer1}";  "{answer2}";  "{answer3}";  "{answer4}"; "{right_}"; "{cat}";')
        n = n + 1

#for key, value in qes_right.items():
#    print(f'--  {key} {value} --\n')
  
