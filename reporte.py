#Renombre a pandas como pd y a matplotlib.pyplot co
import pandas as pd
import matplotlib.pyplot as plt

#Leer archivos
df=pd.read_csv("Ventas.csv")
#Eliminar duplicados
df=df.drop_duplicates()
#Guardar archivo limpio
df.to_csv("Ventas_limpio.csv",index=False)
#Crear graficos de ventas por producto
ventas_por_producto=df.groupby("Producto")["Ventas"].sum()
ventas_por_producto.plot(kind="bar")
#Configuracion del grafico
plt.title("Ventas por producto")
plt.ylabel("Total de ventas")
plt.xlabel("producto")


#Guardar grafico como imagen
plt.savefig("grafico.png")
plt.show()

print("Datos limpios guardados en'ventas_limpio.csv'")
print("Grafico generado en 'grafico.png'")