import numpy as np
import matplotlib.pyplot as plt

plt.ioff()
x= np.linspace(0,1,100,False)
y= x**2 + 2
y2=x**3 +2

plt.plot(x,y)
plt.plot(x,y2)
plt.title("Number1")
plt.xlabel("Aveces X")
plt.ylabel("Aveces Y")
plt.show()
print("Hola Mundo")
#puedo generar dos plots, si estos se presentan antes del show ambos se grafican juntos, y si cada uno tiene su show se mostrara uno tras otro
#El plt.ion hace que solo se muestre la ventana emergente mientras se corre el codigo y de esta manera dejar de funcionar al finalizar el codigo

""" datos=np.arange(0,360)
datos=np.radians(datos)
datos=np.sin(datos)
plt.plot(datos,"m--")
plt.show() """
#Se puedene pasar a radianes las mediciones de las graficas

""" datos_x = np.array([1,2,3,34,5,5])
datos_y = np.array([3,6,9,162,15,15])
plt.plot(datos_x,datos_y)
plt.show() """

#El plt.subplot(2,1,1)   (filas,columnas, numero de panel) genera subespacios adaptables como si fuese una matriz de espacios teniendo de esta manera espacios alterables de filasxcolumnas
#Generando una interfaz orientada a objetos
#ax=plt.axes() para crear un objeto axes
#fig=plt.figure() para crear un objeto tipo figura

