import scipy as s
import numpy as n
import matplotlib as m
import csv
import warnings
import scipy.stats

warnings.filterwarnings("ignore")

data = {'fg': [], 'threePt': [], 'margin': []}

confidence = 0.95
n = 5


def calculateConfidence(input):
    m = s.mean(input)
    std_err = s.stats.sem(input)
    h = std_err * s.stats.t.ppf((1 + confidence) / 2, n - 1)
    start = m - h
    end = m + h
    print(f'Start: {start}\nEnd: {end}\n\n')


def getData(r):

    data['fg'].append(float(r['FG%']))
    data['threePt'].append(float(r['3pt%']))
    data['margin'].append(float(r['MofV']))


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

print('UTA\n')
with open('data/UTA5.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)

    print(f'Field Goal Confidence Interval:')
    calculateConfidence(data["fg"])
    print(f'Three Point Confidence Interval:')
    calculateConfidence(data["threePt"])
    print(f'Margin of Victory Confidence Interval:')
    calculateConfidence(data["margin"])

data = {'fg': [], 'threePt': [], 'margin': []}
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

print('SAC\n')
with open('data/SAC5.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)

    print(f'Field Goal Confidence Interval:')
    calculateConfidence(data["fg"])
    print(f'Three Point Confidence Interval:')
    calculateConfidence(data["threePt"])
    print(f'Margin of Victory Confidence Interval:')
    calculateConfidence(data["margin"])

data = {'fg': [], 'threePt': [], 'margin': []}
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

print('MIL\n')
with open('data/MIL5.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)

    print(f'Field Goal Confidence Interval:')
    calculateConfidence(data["fg"])
    print(f'Three Point Confidence Interval:')
    calculateConfidence(data["threePt"])
    print(f'Margin of Victory Confidence Interval:')
    calculateConfidence(data["margin"])

data = {'fg': [], 'threePt': [], 'margin': []}
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

print('PHI\n')
with open('data/PHI5.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)

    print(f'Field Goal Confidence Interval:')
    calculateConfidence(data["fg"])
    print(f'Three Point Confidence Interval:')
    calculateConfidence(data["threePt"])
    print(f'Margin of Victory Confidence Interval:')
    calculateConfidence(data["margin"])

data = {'fg': [], 'threePt': [], 'margin': []}
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

print('GSW\n')
with open('data/GSW5.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)

    print(f'Field Goal Confidence Interval:')
    calculateConfidence(data["fg"])
    print(f'Three Point Confidence Interval:')
    calculateConfidence(data["threePt"])
    print(f'Margin of Victory Confidence Interval:')
    calculateConfidence(data["margin"])

data = {'fg': [], 'threePt': [], 'margin': []}
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

print('LAC\n')
with open('data/LAC5.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in reader:
        getData(row)

    print(f'Field Goal Confidence Interval:')
    calculateConfidence(data["fg"])
    print(f'Three Point Confidence Interval:')
    calculateConfidence(data["threePt"])
    print(f'Margin of Victory Confidence Interval:')
    calculateConfidence(data["margin"])

data = {'fg': [], 'threePt': [], 'margin': []}
