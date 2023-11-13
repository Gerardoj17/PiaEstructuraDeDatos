def servicios_mas_prestados():
    
    cantidad = int(input("Ingrese la cantidad de servicios más prestados a identificar: "))

   
    fecha_inicial_ingresada = input("Ingrese la fecha inicial (dd/mm/aaaa): ")
    fecha_inicial = validar_fecha(fecha_inicial_ingresada)

    fecha_final_ingresada = input("Ingrese la fecha final (dd/mm/aaaa): ")
    fecha_final = validar_fecha(fecha_final_ingresada)

    
    if fecha_final < fecha_inicial:
        print("La fecha final debe ser igual o posterior a la fecha inicial.")
        return

   
    cursor.execute("""
        SELECT servicios.nombre, COUNT(*) as conteo
        FROM detalles
        JOIN notas ON detalles.nota_id = notas.id
        JOIN servicios ON detalles.servicio_id = servicios.id
        WHERE notas.fecha BETWEEN ? AND ?
        GROUP BY servicios.id
        ORDER BY conteo DESC
        LIMIT ?
        """, (fecha_inicial.strftime("%d/%m/%Y"), fecha_final.strftime("%d/%m/%Y"), cantidad))
    servicios = cursor.fetchall()

    
    print("Servicios más prestados en el período especificado:")
    print("{:<15} {:<10}".format('Servicio','Conteo'))
    for servicio in servicios:
        print("{:<15} {:<10}".format(servicio[0], servicio[1]))










def clientes_con_mas_notas():
    
    cantidad = int(input("Ingrese la cantidad de clientes con más notas a identificar: "))

 
    fecha_inicial_ingresada = input("Ingrese la fecha inicial (dd/mm/aaaa): ")
    fecha_inicial = validar_fecha(fecha_inicial_ingresada)

    fecha_final_ingresada = input("Ingrese la fecha final (dd/mm/aaaa): ")
    fecha_final = validar_fecha(fecha_final_ingresada)


    if fecha_final < fecha_inicial:
        print("La fecha final debe ser igual o posterior a la fecha inicial.")
        return


    cursor.execute("""
        SELECT clientes.nombre, COUNT(*) as conteo
        FROM notas
        JOIN clientes ON notas.cliente_id = clientes.id
        WHERE notas.fecha BETWEEN ? AND ?
        GROUP BY clientes.id
        ORDER BY conteo DESC
        LIMIT ?
        """, (fecha_inicial.strftime("%d/%m/%Y"), fecha_final.strftime("%d/%m/%Y"), cantidad))
    clientes = cursor.fetchall()


    print("Clientes con más notas en el período especificado:")
    print("{:<15} {:<10}".format('Cliente','Conteo'))
    for cliente in clientes:
        print("{:<15} {:<10}".format(cliente[0], cliente[1]))









def promedio_montos_notas():
  
    fecha_inicial_ingresada = input("Ingrese la fecha inicial (dd/mm/aaaa): ")
    fecha_inicial = validar_fecha(fecha_inicial_ingresada)

   
    fecha_final_ingresada = input("Ingrese la fecha final (dd/mm/aaaa): ")
    fecha_final = validar_fecha(fecha_final_ingresada)

   
    if fecha_final < fecha_inicial:
        print("La fecha final debe ser igual o posterior a la fecha inicial.")
        return

   
    cursor.execute("""
        SELECT monto_total
        FROM notas
        WHERE fecha BETWEEN ? AND ?
        """, (fecha_inicial.strftime("%d/%m/%Y"), fecha_final.strftime("%d/%m/%Y")))
    montos = cursor.fetchall()


    if montos:
        promedio = sum(monto[0] for monto in montos) / len(montos)
        print(f"El promedio de los montos de las notas en el período especificado es: {promedio}")
    else:
        print("No hay notas en el período especificado.")