##################################################
# Timeit-1.py : Computation Time Measurement 
# for prime_list_1()
##################################################

for n in range(1000, 10001, 1000):
    print(f"{n = :5} : ", end = "")
    %timeit primes = prime_list_1(n)
