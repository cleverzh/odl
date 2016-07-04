# -*- coding: utf-8 -*-
"""
Created on Tue May 31 13:36:12 2016

@author: johan79
"""

from __future__ import print_function, division, absolute_import
from future import standard_library
standard_library.install_aliases()
#from builtins import super

import numpy as np

import odl
from odl.solvers.functional.default_functionals import *

# Discretization parameters
n = 4

# Discretized spaces
space = odl.uniform_discr([0, 0], [1, 1], [n, n])


print(space)

l1func = L1Norm(space)
l1prox = l1func.proximal(sigma=1.5)
l1conjFun = l1func.conjugate_functional


# Create phantom
phantom = odl.util.shepp_logan(space, modified=True)*5+1

LogPhantom=np.log(phantom)





onevector=space.one()*5

prox_phantom=l1prox(phantom)
l1conjFun_phantom = l1conjFun(phantom)

l2func=odl.solvers.functional.L2Norm(space)
l2prox = l2func.proximal(sigma=1.5)
l2conjFun = l2func.conjugate_functional
l2Grad = l2func.gradient

prox2_phantom=l2prox(phantom*10)
l2conjFun_phantom = l2conjFun(phantom/10)

l22=odl.solvers.functional.L2NormSquare(space)
prox22=l22.proximal(1)(phantom)

l22(phantom)
cf22=l22.conjugate_functional(phantom)

l1func3=-3*l1func

l1func3(phantom)
l1func(phantom)

F=l22

epsK=1e-8

print(epsK)

(F(phantom+epsK*LogPhantom)-F(phantom))/epsK

LogPhantom.inner(F.gradient(phantom))

print(l22(phantom))

print((-2*l22)(phantom))

print((l22*2)(phantom))




x = space.element(np.random.standard_normal((n,n)))
#    y = space.element(np.random.rand(n,n))

scal=np.random.standard_normal()
F=odl.solvers.functional.L2Norm(space)

Fs=F*scal    
    
print(Fs(x))


z=(F*scal).gradient(x)    



'''
def test_gradient_solver(op_term, x_0, n_iter=100 ):
    
    functional=op_term[0]
    linear_op=op_term[1]
    value=op_term[2]
    x=x_0    
    beta=functional.grad_lipschitz
    
    for _ in range(n_iter):
    
        
#        Make a simple test case:
    
    
'''

#a=1+2j
#np.sign(a)

#l2der_0=l2func.derivative(space.one)




'''
# Initialize convolution operator by Fourier formula
#     conv(f, g) = F^{-1}[F[f] * F[g]]
# Where F[.] is the Fourier transform and the fourier transform of a guassian
# with standard deviation filter_width is another gaussian with width
# 1 / filter_width
filter_width = 2.0  # standard deviation of the Gaussian filter
ft = odl.trafos.FourierTransform(space)
c = filter_width**2 / 4.0**2
gaussian = ft.range.element(lambda x: np.exp(-(x[0] ** 2 + x[1] ** 2) * c))
convolution = ft.inverse * gaussian * ft

# Optional: Run diagnostics to assure the adjoint is properly implemented
# odl.diagnostics.OperatorTest(conv_op).run_tests()

# Create phantom
phantom = odl.util.shepp_logan(space, modified=True)

# Create vector of convolved phantom
data = convolution(phantom)
data.show('Convolved data')

# Set up the Chambolle-Pock solver:

# Initialize gradient operator
gradient = odl.Gradient(space, method='forward')

# Column vector of two operators
op = odl.BroadcastOperator(convolution, gradient)

# Create the proximal operator for unconstrained primal variable
proximal_primal = odl.solvers.proximal_zero(op.domain)

# Create proximal operators for the dual variable

# l2-data matching
prox_convconj_l2 = odl.solvers.proximal_cconj_l2_squared(space, g=data)

# Isotropic TV-regularization i.e. the l1-norm
prox_convconj_l1 = odl.solvers.proximal_cconj_l1(gradient.range, lam=0.0003,
                                                 isotropic=True)

# Combine proximal operators, order must correspond to the operator K
proximal_dual = odl.solvers.combine_proximals(prox_convconj_l2,
                                              prox_convconj_l1)


# --- Select solver parameters and solve using Chambolle-Pock --- #


# Estimated operator norm, add 10 percent to ensure ||K||_2^2 * sigma * tau < 1
op_norm = 1.1 * odl.power_method_opnorm(op, 5)

niter = 500  # Number of iterations
tau = 1.0 / op_norm  # Step size for the primal variable
sigma = 1.0 / op_norm  # Step size for the dual variable


# Optionally pass partial to the solver to display intermediate results
partial = (odl.solvers.PrintIterationPartial() &
           odl.solvers.ShowPartial(display_step=20))

# Choose a starting point
x = op.domain.zero()

# Run the algorithm
odl.solvers.chambolle_pock_solver(
    op, x, tau=tau, sigma=sigma, proximal_primal=proximal_primal,
    proximal_dual=proximal_dual, niter=niter, partial=partial)

# Display images
phantom.show(title='original image')
data.show(title='convolved image')
x.show(title='deconvolved image', show=True)
'''

