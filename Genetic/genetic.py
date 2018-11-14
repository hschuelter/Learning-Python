import numpy as np
import random as rnd

alfabeto = "abcdefghijklmnopqrstuvwxyz "

def main():
    goal = "to be or not to be"
    mat = []

    for i in range(0, 10):
        word = ""
        for j in range(0, len(goal)-1):
            word = word + alfabeto[ rnd.randint(0, len(alfabeto) - 1) ]
        mat.append(word)
    print(mat)


if __name__ == "__main__": main()