# Exercise 5: Minimalist Email Client.
# Write a program to read through the mail box data and when you find
# line that starts with “From”, you will split the line into words using the
# split function. We are interested in who sent the message, which is the
# second word on the From line.
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# You will parse the From line and print out the second word for each
# From line, then you will also count the number of From (not From:)
# lines and print out a count at the end.

# https://www.py4e.com/code3/mbox.txt

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
file = open(fname)
count = 0
for line in file:
    if not line.startswith('From '):
        continue
    word = line.split()
    second = word[1]
    count = count + 1
    print(second)
print('There were', count, 'lines in the file with From as the first word')
