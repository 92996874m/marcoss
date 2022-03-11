import sys
import math
import numpy as np
import decimal
# log = ln
from sympy import Symbol, Float, Integer, N, lambdify, exp, sqrt, log, cos, sin
import pandas as pd
# sys.tracebacklimit = 0

x = Symbol('x', real=True)
# para inserir funções literais: usar funções do `sympy`
# ex: sqrt(x) = x ^ (1/2) =(python)= x ** (1/2)
# inserir valores numéricos das funções: usar funções do `math`
# ex: math.sqrt(2) = raiz quadrada de 2 = 2^(1/2) =(python)= 2**(1/2)

"""""""""INPUTS"""""""""
# N_REQ = número de casas decimais de precisão
N_REQ = int(3)
# N_PREC = número de casas decimais de precisão + 2 casas de sobra
N_PREC = N_REQ + 2
# COLOCAR NÚMEROS DECIMAIS ENTRE ASPAS!!!! SENÃO NÃO TEM PRECISÃO
# A = extremo esquerdo
A = Float(-1, N_PREC)
# B = extremo direito
B = Float(1, N_PREC)
# adapted from https://stackoverflow.com/a/9877279
# se `f(x)` é uma função qualquer de x
# fazer f(x) = 0
# isolar x de um lado. Tudo que sobrar do outro é chamado de `phi(x)`
# de modo a resultar em x = phi(x)
# trabalharemos apenas com a phi(x).
phi = 1 / (1 + x**2)
# ex: x**2 * exp(x) + sqrt(x) - ( 1 / log(x) ) * ( 1 / cos(x) ) * sin(x)
# ex: se f(x) = x^3 - 7x + 2,
# fazemos f(x) = => x^3 - 7x + 2 = 0
# isolamos x para ficar x = (x^3 + 2) / 7 = phi(x)
# assim, phi(x) = (x^3 + 2) / 7
""""""""""""""""""

f = lambdify(x, phi, 'sympy')
yprime = lambdify(x, phi.diff(x), 'sympy')
print(yprime)

# Teorema do Valor Intermediário (TVI)
# verifica se existe _pelo menos 1_ raiz no intervalo
# NÃO APLICÁVEL AQUI, QUEREMOS PHI(X) = X, e não 0
# if f(A) * f(B) > Float(0, N_PREC):
#     print("ERRO!!!")
#     raise ValueError(
#         f"Favor alterar extremos A e B. Não existe raiz no atual intervalo [{A}, {B}]")

n_list, a_list, b_list, c_list, f_list, e_list = [], [], [], [], [], []

# n = número da repetição do algoritmo, pertence a |N_PREC (1,2,3,...)
n = int(0)
a = A
b = B
# estimativa inicial
c = Float((a + b) / Float(2, N_PREC), N_PREC)

# fator de contração
# VERIFICAR MANUALMENTE
C = Float(3, N_PREC) * Float(math.sqrt(3), N_PREC) / Float(8, N_PREC)
print("C manual:", C)
# raiz quadrada: `math.sqrt()`

"""cálculo automático do fator de contração"""
# range de derivadas entre A e B
expoente = abs(Integer(N_REQ - 2))
derivadas_C = [
    N(yprime(i/10**(expoente)), 2)
    for i in range(
        int(A) * 10**(expoente),
        int(B) * 10**(expoente)
    )
]
derivadas_C.extend([N(yprime(A), N_PREC), N(yprime(B), N_PREC)])
# pegar a maior delas
C = max(derivadas_C)
print("C calculado:", C)

# Fator de contração tem que ser menor que 1
if C >= 1:
    print("ERRO!!!")
    raise ValueError(
        f"Fator de contração maior que 1. Favor verificar e inserir manualmente o C.")

while(True):
    print(f"Etapa {n} em progresso...", end="\t", flush=True)
    # time.sleep(1)
    n += 1
    n_list.append(n), a_list.append(a), b_list.append(b), c_list.append(c)

    if n < 2:
        e = Float((abs(a) + abs(b)), N_PREC) / Float(2, N_PREC)
    else:
        e = Float(1/(1-C) * (C**n) * abs(c_list[0] - c_list[1]), N_PREC)

    f_c = N(f(c), N_PREC)
    f_list.append(f_c), e_list.append(e)

    if n > 3:
        if float(abs(f_list[n-1]) - abs(f_list[n-2])) > float(e_list[n-2]):
            print("ERRO!!!")
            raise ValueError(
                f"Função está divergindo. Escolha outro intervalo inicial, nem que seja maior.")
    if e < 10**(-N_REQ):
        break
    else:
        c = c - ( f_c / yprime(c) )


e_list[0] = Float(1/(1-C) * (C**1) * abs(c_list[0] - c_list[1]), N_PREC)
print("\n", c)

d = {'n': n_list, 'a': a_list, 'b': b_list,
     'c': c_list, 'f_c': f_list, 'e': e_list}
df = pd.DataFrame(data=d)
print(df)
print(f"`{c_list[-1]}` é a melhor estimativa para a raiz da função `phi(x) = {phi}`, com `{N_REQ}` casas decimais de precisão, com `{len(n_list)}` iterações.")
