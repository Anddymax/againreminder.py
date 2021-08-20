#define function for greatest common divisor
def findgcd(a,b):
    if (b==0):
        return a
    else:
        return findgcd(b, a%b)
num1=float(input('Enter num1:'))
num2=float(input('Enter num2:'))
gcd=findgcd(num1,num2)
print('GCD of {0} and {1} is {2}'.format(num1,num2,gcd))
#formula for gcd to lcm
lcm=(num1*num2)/gcd
print('LCD of {0} and {1} is {2}'.format(num1, num2,lcm))
