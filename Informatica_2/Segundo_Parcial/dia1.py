#Iniciamos con la explicacion de los arrys, investigar el comportamiento de los arrys, estabas comiendo
import numpy as np
import matplotlib as plt
#x=np.linspace(start,stop,numero de datos,contar ultimo numero)
#y=np.logspace(0,10,10,False,base=2)
#z=np.arange(start,stop,...)
y=np.logspace(0,10,10,False,base=2)
x=np.linspace(0,10,10,False)
""" 
print(x)
print(y) """
plt.pyplot(x)
#reshape refomrmar
#Las matrices inician desde el (0,0), al indexar se excluye el ultimo numero, por lo que selecciona con una mas de ello.
#Las dimensiones de la matriz 3D es ↓→↗


