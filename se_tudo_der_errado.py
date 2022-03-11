import math
import numpy as np
# log = ln
from sympy import Symbol, Abs, exp, sqrt, log, cos, sin, nsolve
# sys.tracebacklimit = 0

"""
INSTRUÇÕES

1) Ir para https://live.sympy.org/
2) Substituir a função `f` apropriada
3) Determinar o número de casas decimais de precisão `N_REQ` desejado 
4) Copiar o código abaixo, entre os sinais de # %%%%...
5) Clicar em "Evaluate"
6) O resultado irá aparecer como o exemplo:
    "
    Solução: o zero (raiz) da função está em:
    0.289
    "
"""

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
x = Symbol('x', real=True)

# N_REQ = número de casas decimais de precisão
N_REQ = int(3)

f = x**3 - 7*x + 2

print("Solução: o zero (raiz) da função está em:")
print(nsolve(f, 0, prec=N_REQ))
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%