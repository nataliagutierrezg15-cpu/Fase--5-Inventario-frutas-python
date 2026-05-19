#Nombre: Natalia Granobles Gutierrez
#Grupo: 213022_803
#Programa: Fundamentos de programación
#Codigo fuente: Autoria propia

#Matriz inventario frutas
inventario = [
    ["Código", "Nombre_Fruta", "Stock_Actual", "Stock_Mínimo_Requerido"],
    [101, "Manzana", 8, 15],
    [102, "Banano", 20, 18],
    [103, "Pera", 5, 10],
    [104, "Uva", 12, 12],
    [105, "Mango", 3, 8]
]

#Función para calcular el stock de las frutas
def calcular_stock(stock_actual, stock_minimo_requerido):
    
    #Calcular si stock actual es menor al mínimo requerido
    if stock_actual < stock_minimo_requerido:

        #Calcular la diferencia entre el stock mínimo requerido y el stock actual
        return stock_minimo_requerido - stock_actual
        
    #Si el stock actual es suficiente, no se necesita reponer
    else:
        return 0

#Lista de frutas
print("Lista de frutas: ")

#Recorrer la matriz y mostrar las frutas
for articulo in inventario[1:]:

    #Guardar datos en variables
    codigo = articulo[0]
    nombre_fruta = articulo[1]
    stock_actual = articulo[2]
    stock_minimo_requerido = articulo[3]
    
    #Datos en variable
    print("codigo: ", codigo,
    "nombre: ", nombre_fruta,
    "stock actual: ", stock_actual,
    "stock mínimo requerido: ", stock_minimo_requerido)
    
    #Calcular el stock necesario para reponer
    stock_necesario = calcular_stock(stock_actual, stock_minimo_requerido)
    
    #Mostrar el stock para reponer
    print(nombre_fruta, "- Reponer fruta: ", stock_necesario, " unidades")