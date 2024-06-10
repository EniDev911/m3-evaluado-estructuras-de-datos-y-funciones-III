<a href="https://colab.research.google.com/gist/EniDev911/5bd7cc18d605a6cfccc6374cd5abf443/estructuras-de-datos-y-funciones-iii.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>


```python
preguntas_basicas = {
    'pregunta_1': {
        'enunciado':['Enunciado básico 1'],
        'alternativas': [['alt_1', 0],
                     ['alt_2', 1],
                     ['alt_3', 0],
                     ['alt_4', 0]]
    },

    'pregunta_2': {
        'enunciado':['Enunciado básico 2'],
        'alternativas': [['alt_1', 0],
                     ['alt_2', 1],
                     ['alt_3', 0],
                     ['alt_4', 0]]
    },

    'pregunta_3': {
        'enunciado':['Enunciado básico 3'],
        'alternativas': [['alt_1', 0],
                     ['alt_2', 1],
                     ['alt_3', 0],
                     ['alt_4', 0]]
    }
}

preguntas_intermedias = {
    'pregunta_1': {
        'enunciado':['Enunciado intermedio 1'],
        'alternativas': [['alt_1', 0],
                     ['alt_2', 1],
                     ['alt_3', 0],
                     ['alt_4', 0]]},

    'pregunta_2': {
        'enunciado':['Enunciado intermedio 2'],
        'alternativas': [['alt_1', 0],
                     ['alt_2', 1],
                     ['alt_3', 0],
                     ['alt_4', 0]]},

    'pregunta_3': {
        'enunciado':['Enunciado intermedio 3'],
        'alternativas': [['alt_1', 0],
                     ['alt_2', 1],
                     ['alt_3', 0],
                     ['alt_4', 0]]
    }
}

preguntas_avanzadas = {
    'pregunta_1': {
        'enunciado':['Enunciado avanzado 1'],
        'alternativas': [['alt_1', 0],
                     ['alt_2', 1],
                     ['alt_3', 0],
                     ['alt_4', 0]]
    },

    'pregunta_2': {
        'enunciado':['Enunciado avanzado 2'],
        'alternativas': [['alt_1', 0],
                     ['alt_2', 1],
                     ['alt_3', 0],
                     ['alt_4', 0]]
    },

    'pregunta_3': {
        'enunciado':['Enunciado avanzado 3'],
        'alternativas': [['alt_1', 0],
                     ['alt_2', 1],
                     ['alt_3', 0],
                     ['alt_4', 0]]
    }
}

pool_preguntas = {
    'basicas': preguntas_basicas,
    'intermedias': preguntas_intermedias,
    'avanzadas': preguntas_avanzadas
}

if __name__ == '__main__':
    print(pool_preguntas['basicas']['pregunta_1'])
```

    {'enunciado': ['Enunciado básico 1'], 'alternativas': [['alt_1', 0], ['alt_2', 1], ['alt_3', 0], ['alt_4', 0]]}


### Validador

Se solicita crear un programa llamado `validador.py` (que ya viene en el apoyo) el cual permite validar si un valor se encuentra incluido en un conjunto de opciones.

- Se pide crear la función `validate()`, la cual debe aceptar como argumentos una **lista de opciones** y una **elección**.
- En caso que no se ingrese una opción dentro del conjunto, la aplicación debe mostrar `'Opción no válida, ingrese una de las opciones válidas: ` y solicitar el valor hasta que se ingrese uno válido.

> **Tip**: Se puede usar el operador `not in` para determinar si un elemento no es parte de una lista.



```python
def validate(opciones, eleccion):
    # Definir validación de eleccion
    ##########################################################################
    while True:

        if isinstance(eleccion, int) and eleccion not in opciones:
            print('Opción no válida, ingrese una de las opciones válidas:', opciones)
            eleccion = int(input('Ingresa una Opción: '))

        elif isinstance(eleccion, str) and eleccion not in opciones:
            print('Opción no válida, ingrese una de las opciones válidas:', opciones)
            eleccion = input('Ingresa una Opción: ').lower()

        else:
            break
    ##########################################################################
    return eleccion

if __name__ == '__main__':

    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    print(validate(numeros, eleccion))
```

    Ingresa una Opción: 0
    0


### Escoger nivel

Cree un programa llamado `level.py` (que ya viene en el apoyo) que incluya la función `choose_level()` que permite **escoger el nivel de dificultad** de la pregunta a realizar.

Esta función debe aceptar como argumentos el **número de la pregunta**, y la **cantidad de preguntas por nivel**.

El funcionamiento debe ser el siguiente:

- Si se eligen 2 preguntas por nivel
    - Las preguntas **nº1** y **nº2** deben ser de nivel de dificultad básicas.
    - Las preguntas **nº3** y **nº4** de nivel intermedio.
    - Las preguntas **nº5** y **nº6** avanzadas.

- En cambio si se escogen 3 preguntas por nivel
    - Las preguntas **nº1**, **nº2** y **nº3** deben ser de nivel de dificultad básicas.
    - Las preguntas **nº4**, **nº5** y **nº6** deben ser de nivel de dificultad intermedia.
    - Las preguntas **nº7**, **nº8** y **nº9** deben ser de nivel de dificultad avanzadas.

La función debe **retornar el nivel escogido**.


```python
def choose_level(n_pregunta, p_level):

    # Construir lógica para escoger el nivel
    ##################################################
    if n_pregunta <= p_level:
        level = 'basicas'
    elif n_pregunta <= 2*p_level:
        level = 'intermedias'
    else:
        level = 'avanzadas'
    ##################################################
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias
```

    basicas
    intermedias
    avanzadas
    intermedias


### Mezclar alternativas

Crear un programa llamado `suffle.py` (que viene en el apoyo) que contenga la función `shuffle_alt_()`.

- Esta función debe tomar como argumento una pregunta desde el archivo `preguntas.py` (con un nivel y una pregunta definida) y mezclar las alternativas.
- La función debe retornar las alternativas mezcladas.

> **Tip**: considerar la función `random.shuffle()` del módulo **`random`**.



```python
import random

def shuffle_alt(pregunta):
    #mezclar alternativas
    #######################################################################
    random.shuffle(pregunta['alternativas'])
    #######################################################################

    # return pregunta['alternativas']
if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    shuffle_alt(pool_preguntas['basicas']['pregunta_1'])

    print(pool_preguntas['basicas']['pregunta_1'])
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]
```

    {'enunciado': ['Enunciado básico 1'], 'alternativas': [['alt_1', 0], ['alt_3', 0], ['alt_4', 0], ['alt_2', 1]]}


### Escoger una pregunta

Crear un programa llamado `question.py` (que viene en el apoyo) que permita escoger una pregunta que no se haya hecho durante la ejecución del programa dependiendo del nivel de dificultad.

- Cree una función llamada `choose_q()` como único argumento que es la dificultad de la pregunta.
- La función debe tomar las preguntas del archivo `preguntas.py` de acuerdo a la difucultad escogida.
- La función debe escoger una pregunta de las opciones disponibles y eliminar dicha opción para no volverla a escoger.
- La función debe retornar dos elementos separados, **el primero debe ser el enunciado** escogido y el segundo **las alternativas mezcladas** de acuerdo a la tarea anterior.


```python
import random

# Opciones dadas para escoger.
###############################################
opciones = {
    'basicas': ['pregunta_1', 'pregunta_2', 'pregunta_3'],
    'intermedias': ['pregunta_1', 'pregunta_2', 'pregunta_3'],
    'avanzadas': ['pregunta_1', 'pregunta_2', 'pregunta_3'],
}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad
    preguntas = pool_preguntas[dificultad]
    # usar opciones desde ambiente global
    if dificultad not in opciones:
        raise ValueError(f"Dificultad no válida: {dificultad}")
    # escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas[n_elegido]
    shuffle_alt(pregunta)

    return pregunta['enunciado'],pregunta['alternativas']

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')

    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')

    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
```

    El enunciado es: ['Enunciado básico 2']
    Las alternativas son: [['alt_4', 0], ['alt_3', 0], ['alt_1', 0], ['alt_2', 1]]
    El enunciado es: ['Enunciado básico 1']
    Las alternativas son: [['alt_4', 0], ['alt_3', 0], ['alt_2', 1], ['alt_1', 0]]
    El enunciado es: ['Enunciado básico 3']
    Las alternativas son: [['alt_2', 1], ['alt_3', 0], ['alt_1', 0], ['alt_4', 0]]


### Mostrar las preguntas en pantalla

Crear un programa llamado `print_preguntas.py` (*que viene en el apoyo*), el cual permitirá mostrar en la app las preguntas de acuerdo a un formato:

- El programa debe contener la función `print_pregunta()` que tome como argumentos un enunciado y sus alternativas, y que le aplique formato.
- Esta función no debe retornar ningún objeto, sólo imprimir en pantalla.
- El formato a utilizar es imprimir el enunciado, seguido de un salto de línea.
- Luego cada alternativa irá acompañada de una letra, una por cada línea de la siguiente manera:
    - A. Alternativa 1
    - B. Alternativa 2
    - C. Alternativa 3
    - D. Alternativa 4


```python
def print_pregunta(enunciado, alternativas):

    # Imprimir enunciado y alternativas
    ###############################################################
    print("".join(enunciado))


    for i in range(len(alternativas)):
        print(chr(ord('A') + i)+".", alternativas[i][0])
    ###############################################################

if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = pool_preguntas['basicas']['pregunta_1']

    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])

    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4

```

    Enunciado básico 1
    A. alt_3
    B. alt_2
    C. alt_4
    D. alt_1


### Verificar respuesta

Crear un programa llamado `verify.py` (incluido en el apoyo) el cual debe contener la función verificar que permite comprobar si la respuesta entregada por el usuario es correcta.

- El programa debe contener la función `verificar()` que toma como argumento las alternativas y la elección.
- En el caso que la respuesta sea correcta debe imprimir en pantalla `Respuesta Correcta` y **retornar** sólo el valor `True`, en caso contrario debe imprimir en pantalla `Respuesta Incorrecta` y retornar sólo el valor `False`.


```python
def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    correcto = True if alternativas[eleccion][1] == 1 else False

    if correcto:
        print('Respuesta Correcta')
    else:
        print('Respuesta Incorrecta')
    ##########################################################################################
    return correcto

if __name__ == '__main__':

    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = pool_preguntas['basicas']['pregunta_2'] # descomental al final
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)
```

    Enunciado básico 2
    A. alt_4
    B. alt_2
    C. alt_1
    D. alt_3
    Escoja la alternativa correcta:
    > b
    Respuesta Correcta


### Ensamblado de la app

Como se mencionó anteriormente, el programa `main.py` incluye un esqueleto que el Tech Lead desarrolló. Este esqueleto ya incluye mensajes en el caso de acertar a una pregunta, de responder correctamente todas las preguntas o en caso de equivocarse, además de la lógica de pasar preguntas una a una.

El objetivo de esta tarea es poder incluir todas las funcionalidades desarrolladas anteriormente y completar las siguientes tareas:

- Agregar un **validador de opción** (el cual determina el inicio del programa o no)
- En caso de escoger la **opción 0**, agregar el mensaje `Nos vemos pronto!` y finalizar el programa.
- Agregar un validador al número de preguntas por nivel.
- Escoger el nivel de la pregunta dependiendo del contador `n_pregunta` y el número de preguntas por nivel.
- Escoger el enunciado y las alternativas dependiendo del nivel según corresponda.
- Imprimir enunciado y sus alternativas pantalla.
- Validar la respuesta entregada.
- Verificar si la respuesta es correcta o no.
- Validar si desea continuar o no.


```python
import time
import os
import sys

# valores iniciales -
n_pregunta = 0
continuar = 'y'
correcto = True
p_level = 10
op_sys = 'cls' if sys.platform == 'win32' else 'clear'


# ----------------------------------------

os.system(op_sys) # limpiar pantalla

print('Bienvenido a la Trivia')
opcion = input('''Ingrese una opción para Jugar!
        1. Jugar
        0. Salir

    > ''')
# 1. validar opcion
opcion = validate(['0', '1'], opcion)

# 2. Definir el comportamiento de Salir
if opcion == '0':
    print("Saliendo del programa")
    time.sleep(2)
    os.system(op_sys)
    !kill -9 -1
    # finalizar programa

# Funcionamiento de preguntas
while correcto and n_pregunta < 3*p_level:

    if n_pregunta == 0:
        p_level = input('¿Cuántas preguntas por nivel? (Máximo 3): ')
        # 3. Validar el número de preguntas por nivel
        p_level = validate([1, 2, 3], int(p_level))
        print("preguntas por nivel:", p_level)
    if continuar == 'y':
        #contador de preguntas
        n_pregunta += 1
        # 4. Escoger el nivel de la pregunta
        nivel = choose_level(n_pregunta, p_level)
        print(f'Pregunta {n_pregunta}:{nivel}')
        # 5. Escoger el enunciado y las alternativas de una pregunta según el nivel escogido
        enunciado, alternativas = choose_q(nivel)
        #6. Imprimir el enunciado y sus alternativas en pantalla
        print_pregunta(enunciado, alternativas)

        respuesta = input('Escoja la alternativa correcta:\n> ').lower()
        # 7. Validar la respuesta entregada
        respuesta = validate(['a', 'b', 'c', 'd'], respuesta)
        # 8. Verificar si la respuesta es correcta o no
        correcto = verificar(alternativas, respuesta)

        if correcto and n_pregunta < 3*p_level:
            print('Muy bien sigue así!')
            continuar = input('Desea continuar? [y/n]: ').lower()
            #9. Validar si es que se responde y o n
            continuar = validate(['y', 'n'], continuar)
            os.system(op_sys)
        elif correcto and n_pregunta == 3*p_level:
            print(f'Felicitaciones, Has respondido {3*p_level} preguntas correctas. \n Has ganado la Trivia \n Gracias por Jugar, hasta luego!!!')
            time.sleep(3)
            os.system(op_sys)
        else:
            print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas,\n Sigue participando!!')
            time.sleep(3)
            !kill -9 -1
    else:
        print('Nos vemos la proxima vez, sigue practicando')
        time.sleep(3)
        !kill -9 -1
```

    Bienvenido a la Trivia
    Ingrese una opción para Jugar!
            1. Jugar
            0. Salir
    
        > 1
    ¿Cuántas preguntas por nivel? (Máximo 3): 2
    preguntas por nivel: 2
    Pregunta 1:basicas
    Enunciado básico 3
    A. alt_4
    B. alt_2
    C. alt_1
    D. alt_3
    Escoja la alternativa correcta:
    > b
    Respuesta Correcta
    Muy bien sigue así!
    Desea continuar? [y/n]: y
    Pregunta 2:basicas
    Enunciado básico 2
    A. alt_2
    B. alt_4
    C. alt_3
    D. alt_1
    Escoja la alternativa correcta:
    > a
    Respuesta Correcta
    Muy bien sigue así!
    Desea continuar? [y/n]: y
    Pregunta 3:intermedias
    Enunciado intermedio 1
    A. alt_1
    B. alt_3
    C. alt_4
    D. alt_2
    Escoja la alternativa correcta:
    > d
    Respuesta Correcta
    Muy bien sigue así!
    Desea continuar? [y/n]: y
    Pregunta 4:intermedias
    Enunciado intermedio 3
    A. alt_2
    B. alt_4
    C. alt_3
    D. alt_1
    Escoja la alternativa correcta:
    > a
    Respuesta Correcta
    Muy bien sigue así!
    Desea continuar? [y/n]: y
    Pregunta 5:avanzadas
    Enunciado avanzado 3
    A. alt_4
    B. alt_2
    C. alt_3
    D. alt_1
    Escoja la alternativa correcta:
    > b
    Respuesta Correcta
    Muy bien sigue así!
    Desea continuar? [y/n]: y
    Pregunta 6:avanzadas
    Enunciado avanzado 1
    A. alt_2
    B. alt_1
    C. alt_3
    D. alt_4
    Escoja la alternativa correcta:
    > a
    Respuesta Correcta
    Felicitaciones, Has respondido 6 preguntas correctas. 
     Has ganado la Trivia 
     Gracias por Jugar, hasta luego!!!

