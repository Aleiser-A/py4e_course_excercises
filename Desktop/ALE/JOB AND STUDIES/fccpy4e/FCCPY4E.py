# Write a program which repeatedly reads number unitl the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using
# try and except and print an error message and skip to the next number

num_count = 0
total = 0.0

while True :
    line = input('Enter a number: ')
    if line == 'done' :
        break
    try:
        f_line = float(line)
        print('Number ' + str(f_line) + ' saved')
    except:
        print('Invalid input')
        continue
    num_count = num_count + 1
    total = total + f_line
#print('DONE!')
print(num_count,total,total/num_count)

