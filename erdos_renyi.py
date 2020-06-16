# -*- coding: utf-8 -*-
"""
@author: James Cotter
A class for the Erdos-Renyi G(n,p) random graph model.
"""

import random
import numpy as np
from collections import defaultdict

class Erdos_Renyi:
    """
    A class for the Erdos-Renyi G(n,p) where n is the number of vertices and
    p is the probability of an edge existing between any two pairs of vertices.
    """
    def __init__(self,nodes,prob):
        
        self.n = nodes
        self.p = prob
        
        #initialize random seed
        random.seed(None)
             
        self.adj_list = defaultdict(list)
        
        #initialize adjacency list
        for i in range(self.n):
            self.adj_list[i] = []
        
        #populate edges by comparing probability to random value
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    if(random.random() < self.p):
                        self.add_edge(i,j)
                    
    def add_edge(self,u,v):
        """
        Add an edge from u to v, and v to u because the graph is undirected.
        Inputs:
            u: int, node
            v: int, node
        """
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    
    def print_adjacency(self):
        """
        Helpful for testing.
        """
        print(self.adj_list)
    
    def DFS(self,node,k,marked,degree):
        """
        In order to find k cores, will need to do a depth first search, pruning
        the nodes with degree less than k. Pruning a node also means that
        its neighbors' degree becomes lower.
        Input:
            node: int, vertex
            k: int
            marked: arr
            degree: int
        Output:
            bool
        """
        
        marked[node] +=1
        
        for v in self.adj_list[node]:
            
            #reduce degree of neighbors
            if degree[node] < k:
                degree[v] -= 1
            
            if not marked[v]:
                if(self.DFS(v,k,marked,degree)):
                    degree[node] -= 1
        
        if degree[node] < k:
            return True
        else:
            return False
            
    def fraction_in_k_core(self,k):
        """
        Uses a depth first search algorithm to find the fraction of vertices in 
        a k-core of the graph.
        Inputs:
            k: int, the degree of the k-core
        Outputs:
            gamma: float, the fraction of vertices included in the k-core.
        """
        
        #before searching, none are visited
        visit = np.zeros(self.n)
        
        #array for keeping track of degrees of each vertex
        degrees = np.zeros(self.n)
        for i in self.adj_list:
            degrees[i] = len(self.adj_list[i])
        
        #start from min degree vertex
        start = np.where(degrees == min(degrees))[0][0]
        self.DFS(start,k,visit,degrees)
        
        #account for disconnected vertices
        for v in range(self.n):
            if not visit[v]:
                self.DFS(v,k,visit,degrees)
        
        #commpute fraction of vertices in k-core and return it
        count = 0
        for i in range(self.n):
            if degrees[i] >= k:
                count+=1
        
        return count/self.n
        
    
    def greedy_coloring(self,k):
        """
        An approximate greedy algorithm for k-coloring the graph. Runs in
        polynomial time, but has no guarantee to find the minimum number of
        colors. Can use up to min(degree)+1 colors, the worst case is
        given by the Grundy number of the graph. 
        Inputs:
            k: int, k-coloring number
        Outputs:
            possible: bool, whether or not the graph can be colored with less
                      than k colors.
        """
        
        #coloring is key:value pair of vertex->color
        coloring = {}
        
        #iterate over nodes
        for v in self.adj_list:
            
            #iterate over neighbors to find already used colors
            used = [coloring[n] for n in self.adj_list[v] if n in coloring]
            coloring[v] = self.greedy_util(used)
            
        #find largest number of colors used on any vertex
        n_colors = max(coloring.values())
        
        return n_colors < k
        
    def greedy_util(self,colors):
        """
        Finds the mex (minimum excluded value) of the color list.
        Inputs:
            colors: list, colors already used
        Outputs:
            i: int, new color to be used
        """
        unique_colors = set(colors)
        i = 0
        
        while i >= 0:
            if i not in unique_colors:
                return i
            else:
                i+=1
                
        return i  
    
    def colorable(self,vertex,color_arr,color):
        """
        Checks if the assignment of color to the vertex is valid. Used in 
        the exact_coloring function to check if an assignment is ok.
        Inputs:
            vertex: int
            color_arr: array, list of colorings
            color: int, "color" represented by an int \in {1,..,k}
        Outputs:
            bool, whether color can be used on that vertex.
        """
        for i in self.adj_list[vertex]:
            if (color_arr[i] == color):
                return False
            
        return True
        
    def exact_coloring(self,ind,colors,k):
        """
        Finds an exact coloring of the graph using a recursive algorithm.
        Still O(k^n) in the worst case, but smarter than an unstructured
        search of all possibilities. Based on the backtracking algorithm
        given here: https://www.geeksforgeeks.org/m-coloring-problem-backt
        racking-5/ (they use an adjacency matrix, not list).
        Inputs:
            ind: int, node
            colors: array, colorings
            k: int, k-coloring to be performed
        Outputs:
            colored: bool, indicates whether or not there is a coloring.
        """
        
        if (ind == self.n):
            return True
        
        for color in range(1,k+1):
            if self.colorable(ind,colors,color):
                colors[ind] = color
                if self.exact_coloring(ind+1,colors,k):
                    return True
                colors[ind] = 0
        
    def call_exact(self,k):
        """
        Calls the recursive exact algorithm and returns whether an exact
        coloring was found.
        Input:
            k: k-coloring
        Output:
            bool, whether or not a coloring was found
        """
        #initialize the colors
        colors_arr = [0]*self.n
        
        if self.exact_coloring(0,colors_arr,k):
            return True
        else:
            return False
    
    
    
    

