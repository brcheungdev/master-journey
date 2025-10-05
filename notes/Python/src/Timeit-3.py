##################################################
# Timeit-3.py : Computation Time Measurement 
# for prime_list_3()
##################################################

for n in range(1000, 10001, 1000):
    print(f"n={n:5} : ", end = "")
    %timeit primes = prime_list_3(n)
