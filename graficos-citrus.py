"""Loads citrus fruit data, plots the relationship between diameter and weight"""
import numpy as np
import matplotlib.pyplot as plt

URL = "https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv"

dados = np.loadtxt(URL, delimiter=",", skiprows=1, usecols=np.arange(1, 6, 1))

laranja_diametro = dados[:5000, 0]
laranja_peso = dados[:5000, 1]

plt.plot(laranja_diametro, laranja_peso, label="laranja")
plt.xlabel("Diâmetro")
plt.ylabel("Peso")

toranja_diametro = dados[5000:, 0]
toranja_peso = dados[5000:, 1]

plt.plot(toranja_diametro, toranja_peso, label="toranja")
plt.xlabel("Diâmetro")
plt.ylabel("Peso")


# Coeficiente angular e linear laranjas
x_laranjas = laranja_diametro
y_laranjas = laranja_peso
n_laranjas = np.size(x_laranjas)

a_laranjas = (
    n_laranjas * np.sum(x_laranjas * y_laranjas)
    - np.sum(x_laranjas) * np.sum(y_laranjas)
) / (n_laranjas * np.sum(x_laranjas**2) - np.sum(x_laranjas) ** 2)

b_laranjas = np.mean(y_laranjas) - a_laranjas * np.mean(x_laranjas)


# Coeficiente angular e linear toranjas
x_toranjas = toranja_diametro
y_toranjas = toranja_peso
n_toranjas = np.size(x_toranjas)

a_toranjas = (
    n_toranjas * np.sum(x_toranjas * y_toranjas)
    - np.sum(x_toranjas) * np.sum(y_toranjas)
) / (n_toranjas * np.sum(x_toranjas**2) - np.sum(x_toranjas) ** 2)

b_toranjas = np.mean(y_toranjas) - a_toranjas * np.mean(x_toranjas)



if __name__ == "__main__":
    plt.show()
    plt.close('all')
