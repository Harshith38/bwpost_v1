by K.Mirusch, Simon 
{date:2022-11-01}} {{time:22:50}}
Status: Reading
Tags: #MasterThesis/NeuralNetwork
KeyWords: Data-driven scientific computing, learning unknown physics. FEM, Machine Learning.



## Introduction 

Since the cost of computing and data storage has a huge surge(explosion) extracting information from the data has become overwhelming. a disadvantage of NN is that a prior they embed no inherent knowledge of physical or mathematical, laws governing the underlying the systems at hand.

Disadvantage of PDE's, they are rigid, rely on explicit assumptions, large to be computaionaly infeasible. the PDE's lack the ability to learn from observational input.

Raissi (7) :- Introduced physics informed neural network (PINN) for solving PDE by training a neural Network with a loss Function of PDE residual. this is then combined with a discovery of governing equation throught identtification of coefficients in the PDE.  this gives a good approximation solution but the training problem becomes more complex. --- read again the  highlighted Text
the PDE solvers such as FEM, Finite volume methods have rich theory, providing convergence guarantees. such theories PINN have recently emerged (10,11,12)

This Paper provides a methodology to combine the strength of PDE based modelling- eg., the geometric flexibility and rich set of finite element fucntions of FEM, with the flexibility of neural network to express unknown functions. 
Framework ADCME.js (14, 15) successfully trains FE models with NN, to identify physical steady state Navier Strokes Equation or learining the constitutive relations.