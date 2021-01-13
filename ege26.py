f = open("27888.txt", "r")
a = 1
while True:
    s = f.readline()
    if a == 1:
        s.split(' ')
    if not s:
        break
    a += 1
    print(s)

f.close()