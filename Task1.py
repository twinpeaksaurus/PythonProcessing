"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

#count up the number of rows in the first and second columns in each csv file
#But what about repeats?
#each time a new number is encountered, add it to a list of unique numbers
#if the next number is already in there, do not count it

unique_numbers = []

for text in texts:
    if text[0] not in unique_numbers:
        unique_numbers.append(text[0])
    if text[1] not in unique_numbers:
        unique_numbers.append(text[1])

for call in calls:
    if call[0] not in unique_numbers:
        unique_numbers.append(call[0])
    if call[1] not in unique_numbers:
        unique_numbers.append(call[1])


print("There are " + len(unique_numbers) + " unique telephone numbers in the logs.")