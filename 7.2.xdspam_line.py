# Write a program to prompt for a file name, and then read  through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence values from these lines. 
# When you reach the end of the file, print out the average spam confidence.

file = open('mbox.txt')
read = file.read()
count = 0
for line in read:
    line = line.rstrip()
    if 'X-DSPAM-Confidence: 0.8475' in read:
        continue
    count = count + 1
    print(line, count)
    start_pos = float(line.find(':'))
    num = line[start_pos+2:5]
    extracted = float(num)
print('done')