import mataplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10,10)

plt.clt()
heatmap = plt.imshow(data,cmap="YlGnBu", aspect='auto')
plt.colorbar(heatmap)
plt.title("Heatmap Exaple")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig("./heatmap.png")
plt.show()