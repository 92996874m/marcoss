import sys
import math
import numpy as np
import decimal
# log = ln
from sympy import Symbol, Float, lambdify, N, exp, sqrt, log, cos, sin
import pandas as pd
# import time

x = Symbol('x', real=True)

"""""""""INPUTS"""""""""
# N_REQ = número de casas decimais de precisão
N_REQ = int(11)
# N_PREC = número de casas decimais de precisão + 2 casas de sobra
N_PREC = N_REQ + 2
# COLOCAR NÚMEROS DECIMAIS ENTRE ASPAS!!!! SENÃO NÃO TEM PRECISÃO
# A = extremo esquerdo
A = Float(0, N_PREC)
# B = extremo direito
B = Float(20, N_PREC)
# adapted from https://stackoverflow.com/a/9877279
# y = função qualquer de x
y = x - math.pi
""""""""""""""""""

f = lambdify(x, y, 'sympy')

# Teorema do Valor Intermediário (TVI)
# verifica se existe _pelo menos 1_ raiz no intervalo
if N(f(A), N_PREC) * N(f(B), N_PREC) > 0:
    sys.tracebacklimit = 0
    print("ERRO!!!")
    raise ValueError(
        f"Favor alterar extremos A e B. Não existe raiz no atual intervalo [{A}, {B}]"
    )

n_list, a_list, b_list, c_list, f_list, e_list = [], [], [], [], [], []

# n = número da repetição do algoritmo, pertence a |N (1,2,3,...)
n = int(0)
a = A
b = B
while(True):
    print(f"Etapa {n} em progresso", flush=True)
    # time.sleep(1)
    c = Float((a + b) / 2, N_PREC)
    n += 1
    n_list.append(n), a_list.append(a), b_list.append(b), c_list.append(c),
    e = (B - A) / (2**n)
    f_c = N(f(c), N_PREC)
    f_list.append(f_c), e_list.append(e),
    if f_c > 0:
        b = c
    elif f_c < 0:
        a = c
    else:
        break
    if e < 10**(-N_REQ):
        break
print(c)

d = {'n': n_list, 'a': a_list, 'b': b_list,
     'c': c_list, 'f_c': f_list, 'e': e_list}
df = pd.DataFrame(data=d)
print(df)
print(f"`{c_list[-1]}` é a melhor estimativa para a raiz `c` da função `{y}`, com `{N_REQ}` casas decimais de precisão.")
