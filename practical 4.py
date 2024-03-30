#function for GCD
def gcd(a, b):
    if a>b:
        c=b
    else:
        c=a
    for i in range (1, c+1):
        if (a%i==0 and b%i==0):
            G=i
    print("GCD is:",G)
# function for LCM
def lcm(a, b):
    if a>b:
        l=a
    else:
        l=b
        while(1):
            if (l%a==0 and l%b==0):
                print("lcm:",l)
                break
            l=l+1
# function for  co-prime
def coprime(a, b):
    hcf=1
    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            hcf=i
    if hcf==1:
        print(f'{a} and {b} are coprime ')
    else:
        print(f'{a} and {b} are not coprime ')