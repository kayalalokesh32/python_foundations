print('1-10 numbers')
i=1
while (i<=10):  
    print(i)
    i+=1
print('1-20 even numbers')
n=1
while(n<=20):
    m=n%2   #to get riminder
    if(m==0):
        print(n)
    n+=1
print('reverse of a number')
add=0
number=int(input("Enter a number:"))

temp=number
while(number>0):

    last=number%10   #to take last nmber
    add=(add*10)+last   #to add last number
    number//=10     # to remove added number

print('reverse:',add)# to print reverse

print('Keep asking input until user types exit')

while(True):
    key='exit'
    user=input('Enter key :')
    if(key==user):
        print('welcome')
        break
    else:
        print('try again')
        continue