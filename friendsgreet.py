n = 3 # n = input('How many friends? ')
names = 'mushraf yenoshan Rekha '.split() # names = input('Who are they? ').split()

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        print(f'{names[i]}: Hi {names[j]}!')

for i in range(n):
    print(f'{names[i]}: Bye guys!')
    for j in range(i + 1, n):
        print(f'{names[j]}: Bye {names[i]}!')