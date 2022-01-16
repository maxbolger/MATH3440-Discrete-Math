# -*- coding: utf-8 -*-
"""Copy of hw21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v4VG8m1YEwypCWvfGU1nFabkE2porC2s
"""

def eqn(n):
  sum = 0
  for i in range(1,n+1):
    sum+=i
  return sum

def clsd_frm(n):
  return (n*(n+1)) / 2

def test(n):
  bool_array = []
  for i in range(1,n+1):
    bool_array.append(eqn(i) == clsd_frm(i))
  return all(bool_array)

## extra: show that n^2 < 2^n for n > 4

def proof(n):
  if n <= 4:
    print("False. n < 4 doesn't satisfy this equation")

  else:
    bool_array = []
    for i in range(5,n+1):
      bool_array.append(i**2 < 2**i)
    return all(bool_array)