# -*- coding: utf-8 -*-
"""w3-computer-program.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l0PjpisawOjFJXN6y_6X2W8xcOCPDtDq
"""

import numpy as np
from math import gcd 
import seaborn as sns
import matplotlib.pyplot as plt

# Solution 1 - Viz

means = [] 
lt = []

def lowestTermsCheck(p,q):

  if gcd(p,q) == 1:
    lt.append(1)

  else: 
    lt.append(0)

  def lowestTermsSim(n,m=100):

    for _ in range(n):
      p = np.random.randint(low=1, high=10001, size=m)
      q = np.random.randint(low=1, high=10001, size=m)

      for i,j in zip(p,q):
        lowestTermsCheck(i,j)

      means.append(np.mean(lt))

    fig, ax = plt.subplots(figsize=(8,5))
    s = sns.histplot(means ,kde=True) 
    plt.title(
    f'Simulating {n} Random Samples of Size {m}\n' \ 
    f'Mean = {round(np.mean(means),3)}'
    )

  return s


# Solution 2

lt = []

def lowestTermsCheck(p,q):

  if gcd(p,q) == 1:
    lt.append(1)

  else:
    lt.append(0)

def lowestTermsSim(m):

  p = np.random.randint(low=1, high=10001, size=m)
  q = np.random.randint(low=1, high=10001, size=m)

  for i,j in zip(p,q):
    lowestTermsCheck(i,j)

  s = (np.mean(lt))

  return s