# -*- coding: utf-8 -*-
"""makemore_from_scratch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E03IBqOWgaIxceadULytAlsknI9u-IuB
"""

words=open('names.txt', 'r').read().splitlines()

words[:10]

len(words)

min(len(w) for w in words)

max(len(w) for w in words)

