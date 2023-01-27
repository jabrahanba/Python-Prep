
#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
mi_variable = 8
print(mi_variable)

#2) Imprimir el tipo de dato de la constante 8.5
type(8.5)

#3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(mi_variable))

#4) Crear una variable que contenga tu nombre
mi_variable2 = 'abrahan'

#5) Crear una variable que contenga un número complejo
mi_complejo = 13 + 2j

#6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(mi_complejo))

#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi = 3.1416

#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
variable8_1=True
varianle8_2="True"
#No se tratan de lo mismo, una es una variable booleana y la otra tipo string

#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print("el tipo de variable número 1 es:" , type(variable8_1) , "y el tipo de variable número 2 es:" , type(varianle8_2))

#10) Asignar a una variable, la suma de un número entero y otro decimal
variable9_1= 2 + 2.5

#11) Realizar una operación de suma de números complejos
a = 4 + 2j 
b = 2 + 8j
print(a + b)

#12) Realizar una operación de suma de un número real y otro complejo
c = 5
print (a + c)

#13) Realizar una operación de multiplicación
print(4*4)

#14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente = 27 / 4
print (cociente)

#16) De la división anterior solamente mostrar la parte entera
a16 =27 // 4
print(a16)

#17) De la división de 27 entre 4 mostrar solamente el resto
b17 = 27 % 4
print(b17)

#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(a16 * 4 + b17)

#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print("Hola," + " " + "¿Cómo estás?")

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
"2" == 2
#La respuesta será un booleano, en este caso: falso, estamos comparando un caracter con un número entero.

#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
int("2") == 2

#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = float('3,8') #está usando "," en lugar de "."
a = float('3.8')

#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
a23 = 3
a23-=1
print(a23)

#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
1 << 2
# desplazar los bits del número 1 dos lugares a la izquierda

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
2 + '2' #si los dos fueran del mismo tipo sumaría o concatenaría el resultado.

#26) Realizar una operación válida entre valores de tipo entero y string
print("la masa del objeto es: ", 58)

