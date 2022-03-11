import sys
import math
import numpy as np
import decimal
# log = ln
from sympy import Symbol, diff, Float, N, lambdify, Abs, exp, sqrt, log, cos, sin
import pandas as pd
# sys.tracebacklimit = 0

x = Symbol('x', real=True)

# N_REQ = número de casas decimais de precisão
N_REQ = int(9)
# N_PREC = número de casas decimais de precisão + 2 casas de sobra
N_PREC = N_REQ + 2

def bisseccao(y, A=-1, B=1):
    print("u", y)
    f = lambdify(x, y, 'sympy')

    # Teorema do Valor Intermediário (TVI)
    # verifica se existe _pelo menos 1_ raiz no intervalo
    if N(f(A), N_PREC) * N(f(B), N_PREC) > 0:
        sys.tracebacklimit = 0
        print("ERRO!!!")
        raise ValueError(f"Favor alterar extremos A e B. Não existe raiz no atual intervalo [{A}, {B}]")

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
        # print(f_c)
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
    return c_list[-1]

def ponto_fixo(phi, A=-10, B=10, N_PREC=10):
    """""""""INPUTS"""""""""
    # A = extremo esquerdo
    A = Float(A, N_PREC)
    # B = extremo direito
    B = Float(B, N_PREC)
    # adapted from https://stackoverflow.com/a/9877279
    # se `f(x)` é uma função qualquer de x
    # fazer f(x) = 0
    # isolar x de um lado. Tudo que sobrar do outro é chamado de `phi(x)`
    # de modo a resultar em x = phi(x)
    # trabalharemos apenas com a phi(x).
    phi = (x**3 + 2) / 7
    # ex: se f(x) = x^3 - 7x + 2,
    # fazemos f(x) = => x^3 - 7x + 2 = 0
    # isolamos x para ficar x = (x^3 + 2) / 7 = phi(x)
    # assim, phi(x) = (x^3 + 2) / 7
    """"""""""""""""""

    f = lambdify(x, phi, 'sympy')
    yprime = lambdify(x, phi.diff(x), 'sympy')
    print(yprime)

    # print(f(Float(0, 25)))
    # print(type(f))
    # print(f(Float(A, N_PREC)))
    # print(N(f(0), N_PREC))

    # Teorema do Valor Intermediário (TVI)
    # verifica se existe _pelo menos 1_ raiz no intervalo
    if f(A) * f(B) > Float(0, N_PREC):
        sys.tracebacklimit = 0
        print("ERRO!!!")
        raise ValueError(
            f"Favor alterar extremos A e B. Não existe raiz no atual intervalo [{A}, {B}]")

    n_list, a_list, b_list, c_list, f_list, e_list = [], [], [], [], [], []

    # n = número da repetição do algoritmo, pertence a |N_PREC (1,2,3,...)
    n = int(0)
    a = A
    b = B

    # print(
    # bisseccao(yprime, A, B, N_PREC)
        # )

    # fator de contração
    C = max([N(yprime(A), N_PREC), N(yprime(B), N_PREC)])
    print(C)

    # while(True):
    #     print(f"Etapa {n} em progresso", flush=True)
    #     # time.sleep(1)
    #     c = Float((a + b) / Float(2, N_PREC), N_PREC)
    #     n += 1
    #     n_list.append(n), a_list.append(a), b_list.append(b), c_list.append(c),
    #     e = (B - A) / (2**n)
    #     f_c = f(c)
    #     f_list.append(f_c), e_list.append(e),
    #     if f_c > 0:
    #         b = c
    #     elif f_c < 0:
    #         a = c
    #     else:
    #         break
    #     if e < 10**(-N_PREC):
    #         break
    # print(c)

    d = {'n': n_list, 'a': a_list, 'b': b_list,
        'c': c_list, 'f_c': f_list, 'e': e_list}
    df = pd.DataFrame(data=d)
    print(df)
    print(f"`{c_list[-1]}` é a melhor estimativa para a raiz `c` da função `{phi}`, com `{N_PREC}` casas decimais de precisão.")

ponto_fixo((x**3 + 2) / 7)