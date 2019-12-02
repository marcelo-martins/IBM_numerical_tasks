import random
import argparse
from argparse import RawTextHelpFormatter
import matplotlib.pyplot as plt
import numpy as np
import warnings
from math import sqrt
warnings.simplefilter("ignore")

def get_parser():
    parser = argparse.ArgumentParser(description='PCA', formatter_class=RawTextHelpFormatter)
    parser.add_argument('--N', default = 100000,
                        help='Number of elements in the array')
    parser.add_argument('--f', default = 0, choices=range(0,4), type=int,
                        help='Number of elements in the array')
    arguments = parser.parse_args()
    return arguments

def cast(x):
    if(x<0): x = -1
    else: x = 1
    return x

def sum_2(x):
    return x+1

def generate_graph_with_bounds(N):
    upper_bound = [sqrt(i) for i in range(N)]
    lower_bound = [-upper_bound[i] for i in range(N)]
    
    for j in range(3):
        s = 0
        states = [s]
        for i in range(N) : 
            s += cast(random.uniform(-1,1))
            states.append(s)
        plt.plot(states)

    plt.plot(upper_bound, color='r')
    plt.plot(lower_bound, color='r')
    plt.savefig('random_with_bounds.png',dpi=250)

def get_inside_bounds_number(N, totals, first_index, last_index):
    inside = 0
    for i in range(first_index, last_index+1):
        if(-sqrt(N) <= i-N and i-N<=sqrt(N)):
            inside+=totals[i]

    return round(inside*100/N, 2)

def generate_gaussian(N):
    totals = list(np.zeros(N*2).astype('int'))
    possible_results = [i for i in range(-N, N)]
    array = [cast(random.uniform(-1,1)) for i in range(N)]
    
    total=0
    for e in array:
        total += e
        totals[total+N]+=1
    
    first_index = totals.index(next(filter(lambda x: x!=0, totals)))
    totals_rev = totals[::-1]
    last_index = 2*N - 1 - totals_rev.index(next(filter(lambda x: x!=0, totals_rev)))
    plt.bar(possible_results[first_index-int(N/100+5):last_index+int(N/100+5)], totals[first_index-int(N/100+5):last_index+int(N/100+5)])
    plt.axvline(x=-sqrt(N), color='g')
    plt.axvline(x=sqrt(N), color='g')
    inside = get_inside_bounds_number(N, totals, first_index, last_index)
    plt.title(f"inside = {inside}%")
    plt.savefig('random_gaussian_graph.png',dpi=250)

def Main():
    arguments = get_parser()
    N = int(arguments.N)
    choice = int(arguments.f)
    
    if(choice==0):
        generate_graph(N)
        generate_graph_with_bounds(N)
        generate_gaussian(N)
    elif(choice==1):
        generate_graph(N)
    elif(choice==2):
        generate_graph_with_bounds(N)
    elif(choice==3):
        generate_gaussian(N)
        
def generate_graph(N):
    array = [cast(random.uniform(-1,1)) for i in range(N)]
    sum_of_array = sum(list(map(sum_2, array)))

    print(f"Number of 1s: {round(((sum_of_array/2)*100/N),2)}% and -1s: {round(((N - sum_of_array/2)*100/N),2)}%")

    states = []
    total = 0
    for e in array:
        total += e
        states.append(total)

    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(111)
    ax.scatter(np.arange(N), states, c='blue',alpha=0.25,s=0.05)
    ax.plot(states,c='blue',alpha=0.5,lw=0.5,ls='-',)
    plt.title('1D Random Walk')
    plt.tight_layout(pad=0)
    plt.savefig('random_walk_1d.png',dpi=250)

if __name__ == '__main__':
    Main()