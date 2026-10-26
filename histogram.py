import matplotlib.pyplot as plt

name = ["Rohit", "Kohli", "Dhoni"]
runs = [14000, 16000, 10000]

plt.hist(runs, bins=5, edgecolor="black")

plt.xlabel("Runs")
plt.ylabel("Frequency")
plt.title("Histogram of Players' Runs")

plt.show()