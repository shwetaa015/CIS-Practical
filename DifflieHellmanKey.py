from random import randint
if __name__ == '__main__':

    p = int(input("Enter the value of prime number p: "))
    g = int(input("Enter the value of generator g: "))
    print('Agreed prime is: %d'%(p))
    print('And agreed generator g is: %d'%(g))

    a = int(input("Enter Alice's secret key: "))
    print('Secret number for Alice is:%d'%(a))

    PUa = int(pow(g,a,p))

    b= int(input("Enter Bob's secret key: "))
    print('Secret number for Bob is: %d'%(b))

    PUb = int(pow(g,b,p))

    ka = int(pow(PUb,a,p))

    kb = int(pow(PUa,b,p))

    print('Secret key for the Alice is: %d'%(ka))
    print('Secret key for the Bob is: %d'%(kb))
