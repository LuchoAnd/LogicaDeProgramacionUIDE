def main():
    # 1. Inicio
    print("¡Bienvenido al Juego de la Serpiente!")
    
    # 2. Ingrese su nombre
    nombre = input("Por favor, ingresa tu nombre: ")
    print(f"Hola, {nombre}. ¡Prepárate para jugar!")
    
    # 3. Empezar juego
    print("El juego está empezando...")
    serpiente = ["Cuerpo"]  # La serpiente empieza con un cuerpo
    comida = True           # Hay comida disponible en el juego
    jugando = True          # El juego se encuentra activo
    
    while jugando:
        # 4. Mover la serpiente
        print("Moviendo la serpiente...")
        
        # 5. Cabeza tocó comida
        if comida:  # Simulación de que la cabeza tocó comida
            print("¡La cabeza tocó la comida!")
            
            # 6. Agregar comida y agregar segmento
            serpiente.append("Segmento")  # Agregar un segmento a la serpiente
            print(f"La serpiente ahora tiene {len(serpiente)} segmentos.")
            comida = False  # Simulación de que la comida se consume
        
        # 7. Análisis de colisión
        colision = input("¿La serpiente chocó contra algo? (s/n): ").lower()
        if colision == "s":
            print("¡La serpiente colisionó!")
            jugando = False  # Fin del juego
        else:
            comida = True  # Reaparece la comida para la próxima iteración

    # 8. Fin del Juego
    print(f"¡Juego terminado, {nombre}! La serpiente tuvo {len(serpiente)} segmentos.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
