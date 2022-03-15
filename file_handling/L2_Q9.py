import csv
import re

def no_of_lines(regex):
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv
    with open('../../hacker_news.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')

        line_count = 0
        for row in csv_reader:
            if re.search(regex , ''.join(row)):
                line_count += 1
        
        return line_count

print(no_of_lines('[Jj]ava((?<=Java)S|s)cript'))
print(no_of_lines('[pP]ython'))
print(no_of_lines('Java(?=\S)'))

