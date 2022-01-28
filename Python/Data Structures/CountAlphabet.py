from sqlite3 import apilevel


data_set = "AABBCCC"
alphabet = 'A'

def fing_alphabet(dataset, alphabet):
    count = 0
    for data in dataset:
        for i in range(len(data)):
            if data[i] == alphabet:
                count += 1

    print(count)

fing_alphabet(data_set, alphabet)

