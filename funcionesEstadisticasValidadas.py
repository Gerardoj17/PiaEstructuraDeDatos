def servicios_mas_prestados():
    try:
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de servicios más prestados a identificar: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        print("")

        fecha_inicial_ingresada = input("Ingrese la fecha inicial (dd/mm/aaaa): ")
        print("")
        fecha_inicial = validar_fecha(fecha_inicial_ingresada)

        fecha_final_ingresada = input("Ingrese la fecha final (dd/mm/aaaa): ")
        print("")
        fecha_final = validar_fecha(fecha_final_ingresada)

        if fecha_final < fecha_inicial:
            print("La fecha final debe ser igual o posterior a la fecha inicial.")
            return

        mi_cursor.execute("""
            SELECT servicios.nombre, COUNT(*) as conteo
            FROM detalles
            JOIN notas ON detalles.nota_id = notas.id
            JOIN servicios ON detalles.servicio_id = servicios.id
            WHERE notas.fecha BETWEEN ? AND ?
            GROUP BY servicios.id
            ORDER BY conteo DESC
            LIMIT ?
            """, (fecha_inicial.strftime("%d/%m/%Y"), fecha_final.strftime("%d/%m/%Y"), cantidad))
        servicios = mi_cursor.fetchall()

        print("Servicios más prestados en el período especificado: ")
        print("{:<15} {:<10}".format('Servicio','Conteo'))
        print("*" * 30)
        for servicio in servicios:
            print("{:<15} {:<10}".format(servicio[0], servicio[1]))
    except Exception as e:
        print(f"Ocurrió un error: {e}")




def clientes_con_mas_notas():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de clientes con más notas a identificar: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número positivo. Inténtalo de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
    
    while True:
        fecha_inicial_ingresada = input("Ingrese la fecha inicial (dd/mm/aaaa): ")
        fecha_inicial = validar_fecha(fecha_inicial_ingresada)
        if fecha_inicial is None:
            print("Fecha inicial inválida. Inténtalo de nuevo.")
        else:
            break

    while True:
        fecha_final_ingresada = input("Ingrese la fecha final (dd/mm/aaaa): ")
        fecha_final = validar_fecha(fecha_final_ingresada)
        if fecha_final is None:
            print("Fecha final inválida. Inténtalo de nuevo.")
        elif fecha_final < fecha_inicial:
            print("La fecha final debe ser igual o posterior a la fecha inicial. Inténtalo de nuevo.")
        else:
            break


    mi_cursor.execute("""
        SELECT clientes.nombre, COUNT(*) as conteo
        FROM notas
        JOIN clientes ON notas.cliente_id = clientes.id
        WHERE notas.fecha BETWEEN ? AND ?
        GROUP BY clientes.id
        ORDER BY conteo DESC
        LIMIT ?
        """, (fecha_inicial.strftime("%d/%m/%Y"), fecha_final.strftime("%d/%m/%Y"), cantidad))
    clientes = mi_cursor.fetchall()

    print('')
    print("Clientes con más notas en el período especificado:")
    print('*' * 40)
    print("{:<15} {:<10}".format('Cliente','Conteo'))
    print("*" * 40)
    for cliente in clientes:
        print("{:<15} {:<10}".format(cliente[0], cliente[1]))
        print('*' * 40)
    




def promedio_montos_notas():
    while True:
        fecha_inicial_ingresada = input("Ingrese la fecha inicial (dd/mm/aaaa): ")
        fecha_inicial = validar_fecha(fecha_inicial_ingresada)
        if fecha_inicial is None:
            print("Fecha inicial inválida. Inténtalo de nuevo.")
        else:
            break

    while True:
        fecha_final_ingresada = input("Ingrese la fecha final (dd/mm/aaaa): ")
        fecha_final = validar_fecha(fecha_final_ingresada)
        if fecha_final is None:
            print("Fecha final inválida. Inténtalo de nuevo.")
        elif fecha_final < fecha_inicial:
            print("La fecha final debe ser igual o posterior a la fecha inicial. Inténtalo de nuevo.")
        else:
            break

  
    mi_cursor.execute("""
        SELECT monto_total
        FROM notas
        WHERE fecha BETWEEN ? AND ?
        """, (fecha_inicial.strftime("%d/%m/%Y"), fecha_final.strftime("%d/%m/%Y")))
    montos = mi_cursor.fetchall()

   
    if montos:
        promedio = sum(monto[0] for monto in montos) / len(montos)
        promedio = round(promedio, 2)  
        print('')
        print(f"El promedio de los montos de las notas en el período especificado es: ${promedio} pesos")
        print('')
    else:
        print("No hay notas en el período especificado.")
            

