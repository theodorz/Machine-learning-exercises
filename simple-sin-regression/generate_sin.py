import numpy as np
import sys

start = float(sys.argv[1])
end = float(sys.argv[2])
density = float(sys.argv[3])
noise = float(sys.argv[4])

print start, end, density, noise

X = np.arange(start, end, density)
true_Y = np.sin( X )
Y = true_Y + (np.random.rand( len(true_Y) )-0.5)*2*noise

np.savetxt('data.txt', (X,Y))
