string = "vcxzxduybfdsobywuefgas"
word = input('Please input the word: ')

pos = string.find(word)

if pos != -1:
    print(f'Yes, found at position {pos}')
else:
    print('No')

