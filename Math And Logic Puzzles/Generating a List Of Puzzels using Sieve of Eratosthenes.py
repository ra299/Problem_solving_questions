def sieve(n):

    prime = [True for i in range(n+1)]
    p = 2

    while( p*p <= n):
        if(prime[p] == True):
            for i in range(p*p, n+1, p):
                prime[i] = False
        p+=1

    for i in range(2,n+1):
        if(prime[i]):
            print(i)

if __name__ == "__main__":
    n = 10
    print("Following are the prime numbers smaller")
    print("than or equal to", n)
    sieve(n)
