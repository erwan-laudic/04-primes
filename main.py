"""nombre premier"""
from math import sqrt

#### Fonction secondaire

def isprime(p):
    """isprime"""
    if p == 1 :
        return False
    for i in range(2,int(sqrt(p)+1)):
        if p % i == 0:
            return False
    return True


#### Fonction principale

def main():
    """main"""
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print("108 est premier :", isprime(108))


if __name__ == "__main__":
    main()
