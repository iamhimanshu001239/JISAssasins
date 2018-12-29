# program 1 by HIMANSHU
'''''
x=int(input("give a 4 digit no\n"))
ceve=0
codd=0
czero=0
zz=str(x)

if len(zz)==4:
    while(x!=0):
        r=x%10
        print(r)
        if(r==0):
            czero=czero+1
        elif(r%2==0):
            ceve=ceve+1
        else:
            codd=codd+1
        x=int(x/10)
        print( "x=",x)



else:
    print("invalid input,please give 4 digit no")

print(" no of even digits=",ceve,"no of odd digits=",codd,"no of zeroes=",czero)

'''



#bonus question
'''import random
user=int(input("give a four digit no \n"))
cn = random.randint(1000,9999)
print(cn)
cow=0
bull=0

m=(str(user))
n=str(cn)
i=0
while(i<4):
    if (m[i]==n[i]):
        cow=cow+1
    else:
        bull=bull+1
    i=i+1

print(cow)
print(bull)
'''


# bonus question using classes
import random
class gem:
    def getval(self):
        self.value=int(input("give a four digit\n"))



    def finder(self):

        cn = random.randint(1000, 9999)
        print("your no=",self.value)
        print(cn)
        cow = 0
        bull = 0
        m = (str(self.value))
        n = str(cn)
        i = 0
        while (i < 4):
            if (m[i] == n[i]):
                cow = cow + 1
            else:
                bull = bull + 1
            i = i + 1

        print(cow)
        print(bull)

v=gem()
v.getval()
v.finder()





