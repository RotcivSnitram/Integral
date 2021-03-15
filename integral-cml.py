'''
Documentação:
Calcula a integral de funções escolhidas pelos métodos de Simpson e dos trapézios

Ao digitar o comando no terminal deve-se colocar:
python (ou python3) nomedoarquivo.py 'equação f(x)' valor_do_intervalo_inicial valor_do_intervalo_final precisão
'''

# Biblioteca
import numpy as np
import math
import sys
from scipy.integrate import simps
import matplotlib.pyplot as plt

# Funções
def f(x):
    # Documentação:
    """
    Digite em forma de string a sua função

    Parâmetros: x
    Retorno: eval
    """ 
    return eval(sys.argv[1])

def trapezio(fun, a, b, k):
    # Documentação:
    """
    Integração numérica pelo método dos trapézios: 
    Tk = [dxk/2]*[f(a) + 2*∑ f(a + jdxk) + f(b)]
    onde dxk = (b-a)/2**k e o somatório é de j = 1 até j = 2**k - 1 
    
    Parâmetros: fun (função -> float), a (float), b (float) e k (int)
    Retorno: resultado da integral númerica pelo método dos trapézios (float)

    Exemplo:
    >>> Digite o limite inferior da integral: -2
    >>> Digite o limite superior da integral: 2
    >>> Digite a precisão desejada: 0.000001
    >>> O valor da integral pelo método dos trapézios é 0.954499
    """
    
    n = 2**k
    h = (x_f - x_i)/n
    integral_MT = f(x_i) + f(x_f)

    for i in range(1, n):
        xn = x_i + i*h
        integral_MT += 2*f(xn)
    
    integral_MT = (integral_MT)*(h/2)
    
    return integral_MT

def Simpson(fun, a, b, k):
    # Documentação:
    """
    Integração numérica pelo método de Simpson:
    Sk = [dxk/3]*[f(a) + 4*∑ f(a + jdxk) + 2*∑ f(a + jdxk) + f(b)]
    onde dxk = (b-a)/2**k e o primeiro somatório é de j(ímpar) = 1 até j = 2**k - 1 e o segundo somatório é de j(par) = 2 até j = 2**k - 2
    
    Parâmetros: fun (função -> float), a (float), b (float) e k (int)
    Retorno: resultado da integral númerica pelo método de Simpson (float)

    Exemplo:
    >>> Digite o limite inferior da integral: -2
    >>> Digite o limite superior da integral: 2
    >>> Digite a precisão desejada: 0.000001
    >>> O valor da integral pelo método de Simpson é 0.954499
    """
    
    n = 2**k
    h = (x_f - x_i)/n
    somatorio = 0

    for i in range(1, n - 1):
        xn = x_i + i*h
        if (i % 2) != 0:
            somatorio += 4*f(xn)
        else:
            somatorio += 2*f(xn)
    integral_MS = (h/3)*(somatorio + f(x_i) + f(x_f))

    return integral_MS

# Parâmetros
x_i = eval(sys.argv[2])
x_f = eval(sys.argv[3])
precisao = eval(sys.argv[4])
valoranterior_MT = 10**20
x = np.linspace(x_i, x_f, 50)
y = f(x)

# Gráfico da função
plt.plot(x, y, 'o')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfico da função escolhida")
plt.legend()
plt.grid(True)
plt.show()

# Método dos Trapézios
for k in range(0,50):
    integralMT = trapezio(f(x), x_i, x_f, k)
    #print(k, integralMT)
    if math.fabs(integralMT - valoranterior_MT)/math.fabs(integralMT) < precisao: break
    valoranterior_MT = integralMT

# Prints do método dos trapézios
print("\nO valor da integral pelo método dos trapézios é %1.6f" %integralMT)
print("O programa parou após %1.0f iterações" %k)

# Método de Simpson
valoranterior_MS1 = 10**20

for k in range(0, 50):
    integralMS1 = Simpson(f(x), x_i, x_f, k)
    #print(k, integralMS1)
    if math.fabs(integralMS1 - valoranterior_MS1)/math.fabs(integralMS1) < precisao: break
    valoranterior_MS1 = integralMS1

# Método de Simpson com os valores do método dos trapézios
valoranterior_MT = trapezio(f(x), x_i, x_f, k = 0)
valoranterior_MS2 = 10**20

for k in range(0, 50):
    integralMT = trapezio(f(x), x_i, x_f, k)
    integralMS2 = integralMT + (integralMT - valoranterior_MT)/3
    #print(k, integralMS2)
    if math.fabs(integralMS2 - valoranterior_MS2)/math.fabs(integralMS2) < precisao: break
    valoranterior_MS2 = integralMS2
    valoranterior_MT = integralMT

# Prints do método de Simpson
print("\nO valor da integral pelo método de Simpson é %1.6f" %integralMS1)
print("\nO valor da integral pelo método de Simpson utilizando os resultados do método dos trapézios é %1.6f" %integralMS2)
print("O programa parou após %1.0f iterações" %k)