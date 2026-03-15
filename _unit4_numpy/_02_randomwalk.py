import numpy as np
import random 
import matplotlib.pyplot as plt

def main():
    position = 0
    walk = [position]
    step = 1000 
    for i in range(step):
        step =1 if  random.randint(0,1) else -1
        position += step
        walk.append(position)

    
    plt.plot(walk[:100])
    plt.show()

def main2():
    nsteps = 1000
    rng = np.random.default_rng(seed=12345)
    draws = rng.integers(0,2,size=nsteps)
    steps = np.where(draws == 0, 1, -1)
    walk = steps.cumsum()

    print((np.abs(walk) >=10).argmax())

    plt.plot(walk[:100])
    plt.show()
    
if __name__ == "__main__":
    main2()