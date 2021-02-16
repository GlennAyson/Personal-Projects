import csv

sentence = raw_input("Enter a Password: ")
print(sentence)

with open ('Passwords.csv', 'a') as new_file:
    csv_writer = csv.writer(new_file, delimiter = '-')
    new_file.write(sentence)

with open('Passwords.csv', 'r') as curr_file:
    csv_reader = csv.reader(curr_file , delimiter = '\t')

    for line in csv_reader:
        print(line)
