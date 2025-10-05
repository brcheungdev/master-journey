##################################################
# plot_graph_2-3.py - plot graphs example 
# for prime_list_2 and prime_list_3
##################################################

import matplotlib.pyplot as plt

x   = [1000*i for i in range(11)]
y_2 = [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0] # ms
y_3 = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0] # ms

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(1,1,1)

ax.plot(x, y_2, label="prime_list_2" )
ax.plot(x, y_3, label="prime_list_3")

ax.grid()
ax.set_title("prime_list_2 vs. prime_list_3")
ax.set_xlabel("checked numbers")
ax.set_ylabel("computation time (ms)")
ax.legend()

plt.savefig("primes_2-3.png")
plt.show()
