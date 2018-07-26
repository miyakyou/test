import matplotlib.pyplot as plt

data = [8,17,11,6,21,7,8,9,0,5,22,14,36,2,5,0,3,0,15,12,36,4,5,2,1,3,6]

plt.title("Histgram")

plt.xlabel("value")
plt.ylabel("frequency")

plt.hist(data)
plt.show()