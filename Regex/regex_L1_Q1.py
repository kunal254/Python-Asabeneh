import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.sub('[.,]', '', paragraph).split(' ')

result = list()

for i in set(words):
    result.append( (words.count(i), i) )

print(sorted(result, reverse=True))


