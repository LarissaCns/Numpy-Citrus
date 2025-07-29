"""Analisa e plota a relação entre diâmetro e peso de frutas cítricas (laranjas e toranjas)."""

import numpy as np
import matplotlib.pyplot as plt

URL = "https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv"


def carregar_dados(url):
    """Carrega os dados do CSV remoto e retorna como array NumPy."""
    return np.loadtxt(url, delimiter=",", skiprows=1, usecols=np.arange(1, 6, 1))


def separar_frutas(dados):
    """Separa os dados em laranjas e toranjas."""
    laranja = dados[:5000]
    toranja = dados[5000:]
    return laranja, toranja


def calcular_coeficientes(x, y):
    """
    Calcula os coeficientes (angular e linear) da regressão linear simples.
    Retorna a, b onde: y = ax + b
    """
    n = np.size(x)
    a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - np.sum(x) ** 2)
    b = np.mean(y) - a * np.mean(x)
    return a, b


def plotar_relacao(x1, y1, x2, y2):
    """Plota a relação entre diâmetro e peso de duas frutas."""
    plt.plot(x1, y1, label="Laranja", alpha=0.7)
    plt.plot(x2, y2, label="Toranja", alpha=0.7)
    plt.xlabel("Diâmetro")
    plt.ylabel("Peso")
    plt.title("Relação entre Diâmetro e Peso das Frutas Cítricas")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/grafico_citrus.png", dpi=300)
    plt.show()
    plt.close("all")


def main():
    """Função principal para carregar dados, calcular coeficientes e plotar o gráfico."""
    dados = carregar_dados(URL)
    laranja, toranja = separar_frutas(dados)

    laranja_diametro = laranja[:5000, 0]
    laranja_peso = laranja[:5000, 1]
    toranja_diametro = toranja[5000:, 0]
    toranja_peso = toranja[5000:, 1]

    a_laranja, b_laranja = calcular_coeficientes(laranja_diametro, laranja_peso)
    a_toranja, b_toranja = calcular_coeficientes(toranja_diametro, toranja_peso)

    print(f"Laranja: y = {a_laranja:.2f}x + {b_laranja:.2f}")
    print(f"Toranja: y = {a_toranja:.2f}x + {b_toranja:.2f}")

    plotar_relacao(laranja_diametro, laranja_peso, toranja_diametro, toranja_peso)


if __name__ == "__main__":
    main()
