print('square star pattern.')
n=5
for i in range (n):
    for j in range (n):
        print('* ',end='')
    print()   

print("triangle number pattern")

n=5
for i in range(n):
    for j in range(i):
        print(j+1," ",end='')
    print()

print("n number of tables")
print()
n=5
for i in range(2,n+1):
    for j in range(1,11):
        print(i,'X',j,'=',i*j)
    print()