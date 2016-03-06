from matplotlib import pyplot as pp
import numpy as np


noise_sigma = 0.5
X = np.arange(-np.pi,np.pi,0.1)
T = np.sin( X )
Y = T + (np.random.rand( len(T) )-0.5)*2*noise_sigma

pp.plot(X,T,'k-.')
pp.plot(X,Y,'r.')
pp.grid()
pp.xlabel('X')
pp.ylabel('Y')
pp.title('Visualization of the data')

K = []
power = 4

for i in range( len(X) ):
    v = []
    for p in range( power ):
        v.append( X[i] ** p )
    K.append( v )

K = np.matrix( K )
Y = np.matrix( Y ).T
w = np.linalg.inv( K.T * K )*K.T*Y
pred_Y = K*w
pred_Y = np.squeeze( pred_Y.tolist() )

pp.plot( X,T,'k-.')
pp.plot( X,Y,'r.')
pp.plot( X,pred_Y,'b.')
pp.grid()
pp.xlabel('X')
pp.ylabel('Y')
pp.title('Visualization of the data')
