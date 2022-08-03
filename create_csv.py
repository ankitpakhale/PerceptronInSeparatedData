from calendar import c
import csv
from itertools import count
import random
from tkinter import Place

header = ['CGPA', 'ResumeScore', 'Placed']
CGPA = []
ResumeScore = []
placed = []
counter = 0

while (counter <= 150):
    placed.append('1')
    CGPA.append(float(str(random.uniform(2,6))[:4]))
    ResumeScore.append(float(str(random.uniform(2,6))[:4]))
    counter += 1
    placed.append('0')
    CGPA.append(float(str(random.uniform(5,8))[:4]))
    ResumeScore.append(float(str(random.uniform(4,8))[:4]))
    counter += 1

mainl = zip(CGPA, ResumeScore, placed)

with open('abc.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(mainl)