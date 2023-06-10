print('Maths quiz time!')

print('Question 1:')
q1 = input('What is 13 x 7? ')
q1a = str(13 * 7)

if q1 == q1a:
    print('Correct!')

else:
    while not q1 == q1a:
        print('Incorrect, try again.')
        q1 = input('What is 13 x 7? ')

q2 = input('What is 14²? ')
q2a = str(14 ** 2)

if q2 == q2a:
    print('Correct again! Now for the final question.')
else:
    while not q2 == q2a:
        print('Incorrect, try again.')
        q2 = input('What is 14²? ')

q3 = input('What is 83 + 41? ')
q3a = str(83 + 41)

if q3 == q3a:
    print('Correct!')
else:
    while not q3 == q3a:
        print('Incorrect, try again.')
        q3 = input('What is 83 + 41? ')
