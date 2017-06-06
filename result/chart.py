with open('../musicdata/data.csv', 'r') as f:
    lines = f.readlines()
    
genre = []
degree = []

for line in lines:
    values = line.split(',')
    genre.append(float(values[1]))
    degree.append(float(values[2]))

import matplotlib.pyplot as plt
plt.plot(degree, genre, 'bo')
plt.axis([-10, 40, 0, 0.5])
plt.show()