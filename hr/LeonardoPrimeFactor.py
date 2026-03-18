import math

def primeCount(n):
    num = 1
    brp = 0
    primePert = 4
    i = 0
    firstPrime = [2, 3]

    while num < n:
        if i <= 1:
            num *= firstPrime[i]
            # print("num:", num, "fac", firstPrime[i]) 
            i += 1
            brp += 1
            continue
        else:
            while True:
                primePert += 1
                prime = True

                if math.sqrt(primePert) == int(math.sqrt(primePert)):
                    prime = False

                for j in range(2, int(math.sqrt(primePert)) + 1):
                    if primePert % j == 0:
                        prime = False
                        break

                # print("kondisi prime", prime)

                if prime:
                    break

            num *= primePert
            # print("num:", num, "fac", primePert)

            brp += 1

    if n<3 and n!= num:
      brp-=1
    return brp
