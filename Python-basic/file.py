
file = open('data.txt','r')
file1 = open('square.txt','w')

lines = file.readlines()
data = []

for line in lines:
    print(line)
    if line[-1]=='\n':
        data.append(line[:-1])
    else:
        data.append(line)
print(data)

for row in data:
    if row.isnumeric():
        row = int(row)
        sqr = row**2
        sqr = str(sqr)
        file1.write(sqr)
        file1.write('\n')

a = "সরকারি"
print(a)



