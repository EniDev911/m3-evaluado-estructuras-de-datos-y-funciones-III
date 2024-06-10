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