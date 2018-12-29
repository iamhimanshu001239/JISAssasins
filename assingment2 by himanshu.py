# sum of digits of a given no

class Qseven:
    def giveno(self):
        x=int(input("give a number"))
        self.value=x;
    def calculator(self):
        s=0
        r=0
        z=str(self.value)
        while(s < len(z)):
            r=int(r+(self.value)%10)
            self.value=self.value/10
            s=s+1
        print("sum of all digit of your no",r)
v=Qseven()
v.giveno()
v.calculator()


#bonus question 2 by himanshu
import random
x=int(input("give a 6 digit no\n"))
c=0
m=random.randint(100000,999999)
while(m!=x):
    c=c+1
    m=random.randint(100000,999999)
    print(m)

print("no of tries to generate randomly your given no  is",c)



# question 25

x=input("give a character or no\n")


if ord(x) in range(ord("a"),ord("Z")) and ord(x) not in  range(90,96):
    print("you gave aplhabet")

elif ord(x) in range(ord("0"),ord("9")):
    print("you gave number")
else:
    print("social character")



