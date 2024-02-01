# basic application of matplotlib in python3
import matplotlib.pyplot as plt

a = [2, 4, 5]
b = [2, 3, 6]

plt.plot(a, b)

plt.xlabel('X Axis')
plt.ylabel( 'Y Axis')
plt.title('Demo Graph ')
plt.show()