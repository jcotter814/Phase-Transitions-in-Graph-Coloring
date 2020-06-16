# Phase-Transitions-in-Graph-Coloring
3-coloring a graph is a fundamental problem in computer science and one of the
first problems known to be NP Complete. The problem statement of the general 
k-coloring problem is as follows [1]:
    
    Given an undirected graph G(V,E), assign k colors (labels) to the vertices
    c: V->{1,..,k} such that no adjacent vertices have the same color, i.e.
    ∀(u,v) ∈ E, c(u) != c(v).

The general k-coloring has applications in everything from scheduling, register
allocation in a computer, solving a sodoku puzzle, (literally) coloring a map
and even finding the ground state of a q state Potts spin glass [2](a generalization
of the Ising model with a Hamiltonian of the form H = -J*∑δ(s_i,s_j)). For
k >= 3, the problem is known to be NP Complete for general non planar graphs, 
which implies that the best possible exact algorithms will require exponential time
in the worst case unless P = NP. For k = 2 the problem is equivalent to determining if
a graph is bipartite which is in P. A fun sidenote is that it was proven all
planar graphs are 4 colorable, but the proof required the use of computer 
verification, which was controversial at the time.

One observation made however, was that 3-Coloring a graph is often actually
easy in practice and does not suffer from the exponential worst case behavior
expected. Similar behavior is observed in practical solutions to other 
prototypical NP Complete problems such as 3SAT and Integer Partitioning [2]. 
This begs an obvious question (at least to a physicist): what is the point at 
which these problems transition from easy to hard and what does that transition 
depend on? Numerical evidence shows the existence of a phase transition 
between the problems easily soluble in practice and those that are hard. A phase 
transition in physics is the sharp (or discontinous) change in the bulk properties 
of a material due to a small change in some parameter of the system past a critical 
point. The change in phase of ice to liquid water at 0 degrees celsius is one obvious 
example, but the theory of phase transitions (and critical phenomena in general) 
extends far deeper.

So how do we connect the dots between the numerical evidence that 3-Coloring
exhbits a phase transition in its difficulty and the rich physics literature
on phase transitions? What is the so called order parameter controlling the
transition between easy and hard instances? We do so by studying the behavior 
of 3-Colorability on random graphs. 

First, an extremely brief primer on Erdos-Renyi random graphs. The G(n,p) Erdos
Renyi random graph model is a graph G with n vertices and a fixed probability p
of an edge between all nC2 pairs of vertices. The average degree of a given
vertex is ~pn and the degree distribution in the thermodynamic (large n) limit
is Poisson. One can prove (which I will not reproduce here) that there is a sharp
threshold p = log(n)/n at which the graph is almost surely connected. Furthermore,
there is a threshold c_core so G(n,p = c/n) has a k-core is c > c_core and
no k_core if c < c_core. 

What is a k-core and why is this relevant? A k-core of a graph is a subgraph
of G of the largest set S of vertices where each vertex in S is connected to at
least k vertices in S [1]. It is relevant because of the following fact: If a 
graph G does not have a k-core, it is k-colorable.

This means that there is also a critical value c_k > c_core such that:
    Pr(G(n,p = c/n) is k-colorable) = {1 if c < c_k, 0 if c > c_k}

Finding the value of c_core only provides a lower bound on c_k, upper bounding
it requires more sophisticated analytical techniques. However, studying it
shows some of the deep and fascinating interplay between physics, computational
complexity and graph theory.

In this program I do the following: numerically verify the discontinous
emergence of a 3-core in ER random graphs as a function of the average degree
c, find c_core (and thereby lower bound c_k) and verify the continuous 
emergence of the 2-core. I also analyze the output of a greedy 3 coloring 
algorithm below and above the found value of c_core to get a sense of a
possible upper bound.

[1] Mouatadid, Introduction to Complexity Theory 2014

[2] Mulet et al, Coloring Random Graphs 2018

[3] Mertans,The Easiest Hard Problem: Number Partitioning 2003

[4] Moore, Mertens, The Nature of Computation 2011
