# if

existe una variable X
si, X es menor o igual a 10, imprime "menor", sal del programa
si, X es mayor a 11, imprime "mayor", sal del programa
si, X es igual a 5, imprime "igual", sal del programa

x = 5
if (x == 5)
    echo 'igual'
    exit
if (x<=10)
    echo 'menor'
    exit
if (x >=10)
    echo 'mayor'
    exit

# for

existe una variable X
imprime "hola" X => 5 veces, sal del programa

x=5
for{

while(x => 5)
     echo 'hola'
     exit
} 

x = 5
while x == 5:
    echo "hola"
    x = 6

i = 0
for i until X:
    echo "hola"
    i mas 1

# funciones
crea una funcion con parametros a y b, sumalos
existe la variable, a y b
imprime la suma de a + b

a = 1
b = 2
echo a + b


def suma(a, b):
    return a + b

suma(7, 5)

def escribe_la_fecha(archivo):
    abrir_archivo
    pedirle_fecha_a_la_pc
    escribir_fecha_en_archivo
    cerrar_archivo