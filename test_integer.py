#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
i = 11000 # size of array
sampl = np.random.randint(low=1, high=999, size=(i,))
sampl = np.append(sampl, 1000)
np.random.shuffle(sampl)

from amplify import (
    BinaryPoly,
    BinaryQuadraticModel,
    sum_poly,pair_sum,
    gen_symbols,
    Solver,
    decode_solution,
)

x = gen_symbols(BinaryPoly,i)

A=2000;B=1;
H = A*(1-sum_poly(x))**2 -B*sum_poly(i, lambda i_ind: sampl[i_ind]*x[i_ind])

model = H


# In[ ]:



from amplify import Solver
from amplify.client import FixstarsClient
#from amplify.client.ocean import DWaveSamplerClient
from amplify.constraint import less_equal, equal_to, penalty
from amplify import BinarySymbolGenerator, Solver
#from amplify.client.ocean import LeapHybridSamplerClient

client = FixstarsClient()
client.token = "XXXXXXXXXX"
client.parameters.timeout = 60000  # Timeout is 60 seconds
#client.parameters.outputs.duplicate = True  # Enable duplicate output for solutions with the same energy values
#client.parameters.outputs.num_outputs = 0   # Output all the found solutions
client.parameters.num_unit_steps = 100
solver = Solver(client)

%%time
result = solver.solve(model)
if len(result) == 0:
    raise RuntimeError("Any one of constraints is not satisfied.")

energy, values = result[0].energy, result[0].values


x_values = decode_solution(x, values)

print(energy)

