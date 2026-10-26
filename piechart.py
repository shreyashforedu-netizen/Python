import matplotlib.pyplot as plt

name = ["Rohit", "Kohli", "Dhoni"]
runs = [14000, 16000, 10000]


plt.pie(
    runs,
    labels=name,
    autopct="%1.1f%%"
)

plt.show()