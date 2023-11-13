elif opcion_clientes=="4":
                    while True:
                        print("1. Listado de clientes registrados")
                        print("2. Busqueda por clave")
                        print("3. Busqueda por nombre")
                        print("4. Volver al menu de clientes")
                        print("")
                        
                        opcion_clientes_2 = input("Eliga una opcion:\n")
                        print("")
                        
                        if opcion_clientes_2.strip()=="":
                            print("CAMPO VACIO")
                            print("")
                            continue
                            
                        elif opcion_clientes_2=="1":
                            while True:
                                print("")
                                print("1. Ordenado Por Clave")
                                print("2. Ordenado Por Nombre")
                                print("3. Volver al menu anterior")
                                print("")
                                opcion_clientes_3 = input("Eliga una opcion:\n")
                                if opcion_clientes_3.strip()=="":
                                    print("CAMPO VACIO")
                                    print("")
                                    continue
                                elif opcion_clientes_3=="1":
                                    try:
                                        fecha_actual = datetime.date.today()
                                        fecha_reporte = (f"{fecha_actual}.csv")
                                        
                                        with sqlite3.connect("Taller_Mecanico.db") as conn:
                                            mi_cursor = conn.cursor()
                                            mi_cursor.execute("select id, nombre, rfc, correo from clientes where suspendido = 1 order by id;")
                                            
                                            registro_ordenado_id = mi_cursor.fetchall()
                                            print("Clientes Ordenados por ID")
                                            print("")
                                            print("Claves\tNombre\tRFC\t\tCorreo")
                                            print("*" * 60)
                                            if registro_ordenado_id:
                                                for clave, nombre, rfc, correo in registro_ordenado_id:
                                                    print(f"{clave:^6}{nombre}\t{rfc}\t{correo}")
                                                    print("")
                                            
                
                                    except Error as e:
                                        print(e)
                                        
                                    except Exception:
                                        print(f"Se produjo el siguiente error: {sys.int_info()[0]}")
                                        
                                    else: 
                                        
                                        opcion_decision = input("Desea exportar estos datos a CSV o Excel?(S/N)\n")
                                        print("")
                                        if opcion_decision.upper()=="S":
                                            print("1. CSV")
                                            print("2. Excel")
                                            print("")
                                            opcion_exportar = int(input("Eliga una opcion:\n"))
                                            print("")
                                            if opcion_exportar==1:
                                                encabezados = ["CLAVE", "NOMBRE", "RFC", "CORREO"]
                                                with open(fecha_reporte,"w", newline="") as reporte:
                                                    grabador = csv.writer(reporte)
                                                    grabador.writerow(encabezados)
                                                    for datos in registro:
                                                        grabador.writerow(datos)
                                                    print("DATOS EXPORTADOS EXITOSAMENTE\n")
                                                    
                                            elif opcion_exportar==2:
                                                fecha_actual = datetime.date.today()
                                                fecha_reporte_excel = (f"{fecha_actual}.xlsx")
                                                exportar_excel = registro_ordenado_id
                                                libro = openpyxl.Workbook()
                                                hoja = libro["Sheet"]
                                                encabezado = ["CLAVE", "NOMBRE", "RFC", "CORREO"]
                                                hoja.append(encabezado)
                                                for cliente in exportar_excel:
                                                    hoja.append(cliente)
                                                hoja.title = "ID_ordenado"
                                                libro.save(fecha_reporte_excel)
                                                print("DATOS EXPORTADOS EXITOSAMENTE ")
                                        elif opcion_decision.upper()=="N":
                                            break
                                                        
                                                    
                                elif opcion_clientes_3=="2":
                                    try:
                                        fecha_actual = datetime.date.today()
                                        fecha_reporte = (f"{fecha_actual}.csv")
                                        with sqlite3.connect("Taller_Mecanico.db") as conn:
                                            mi_cursor = conn.cursor()
                                            mi_cursor.execute("select id, nombre, rfc, correo from clientes WHERE suspendido = 1 order by nombre;")
                                            
                                            registro= mi_cursor.fetchall()
                                            print("Clientes Ordenados por ID")
                                            print("")
                                            print("Claves\tNombre\tRFC\t\tCorreo")
                                            print("*" * 60)
                                            if registro:
                                                for clave, nombre, rfc, correo in registro:
                                                    print(f"{clave:^6}{nombre}\t{rfc}\t{correo}")
                                                    print("")
                                    except Error as e:
                                        print(e)
                                    except Exception:
                                        print(f"Se produjo el siguiente error: {sys.int_info()[0]}")
                                        
                                    else:
                                        opcion_decision = input("Desea exportar estos datos a CSV o Excel?(S/N)\n")
                                        print("")
                                        if opcion_decision.upper()=="S":
                                            print("1. CSV")
                                            print("2. Excel")
                                            print("")
                                            opcion_exportar = int(input("Eliga una opcion:\n"))
                                            print("")
                                            if opcion_exportar==1:
                                                encabezados = ["CLAVE", "NOMBRE", "RFC", "CORREO"]
                                                with open(fecha_reporte,"w", newline="") as reporte:
                                                    grabador = csv.writer(reporte)
                                                    grabador.writerow(encabezados)
                                                    for datos in registro:
                                                        grabador.writerow(datos)
                                                    print("DATOS EXPORTADOS EXISTOSAMENTE\n")
                                                    
                                            elif opcion_exportar==2:
                                                fecha_actual = datetime.date.today()
                                                fecha_reporte_excel = (f"{fecha_actual}.xlsx")
                                                exportar_excel = registro
                                                libro = openpyxl.Workbook()
                                                hoja = libro["Sheet"]
                                                encabezado = ["CLAVE", "NOMBRE", "RFC", "CORREO"]
                                                hoja.append(encabezado)
                                                for cliente in exportar_excel:
                                                    hoja.append(cliente)
                                                hoja.title = "NOMBRE_ordenado"
                                                libro.save(fecha_reporte_excel)
                                                print("DATOS EXPORTADOS EXITOSAMENTE ")
                                        elif opcion_decision.upper()=="N":
                                            break
                                        
                                    
                                        
                                        
                                elif opcion_clientes_3=="3":
                                    break
                                
                                
                        elif opcion_clientes_2=="2":
                            while True:
                                clave_buscar=input("Ingrese la clave del cliente:\n")
                                valores = {"clave": clave_buscar}
                                try:
                                    fecha_actual = datetime.date.today()
                                    fecha_reporte = (f"{fecha_actual}.csv")
                                    with sqlite3.connect("Taller_Mecanico.db") as conn:
                                        mi_cursor = conn.cursor()
                                        mi_cursor.execute("SELECT id, nombre, rfc, correo FROM clientes WHERE id = :clave and suspendido = 1", valores)
                                        
                                        registro = mi_cursor.fetchall()
                                        
                                        print("")
                                        print("Claves\tNombre\tRFC\t\tCorreo")
                                        print("*" * 60)
                                        if registro:
                                            for clave, nombre, rfc, correo in registro:
                                                print(f"{clave:^6}{nombre}\t{rfc}\t{correo}")
                                                print("")
                                            
                                        else:
                                            print(f"No se encontro ningun cliente con la clave: {clave_buscar} o se encuentra suspendido\n")
                                            break
                                    
                                except Error as e:
                                    print(e)
                                except Exception:
                                    print(f"Se produjo el siguiente error: {sys.int_info()[0]}")
                                    print("")
                                    
                                else:
                                    opcion_decision = input("Desea exportar estos datos a CSV o Excel?(S/N)\n")
                                    if opcion_decision.upper()=="S":
                                        print("1. CSV")
                                        print("2. Excel")
                                        print("")
                                        opcion_exportar = int(input("Eliga una opcion:\n"))
                                        print("")
                                        if opcion_exportar==1:
                                            encabezados = ["CLAVE", "NOMBRE", "RFC", "CORREO"]
                                            with open(fecha_reporte,"w", newline="") as reporte:
                                                grabador = csv.writer(reporte)
                                                grabador.writerow(encabezados)
                                                for datos in registro:
                                                    grabador.writerow(datos)
                                                print("DATOS EXPORTADOS EXISTOSAMENTE\n")
                                                        
                                        elif opcion_exportar==2:
                                            fecha_actual = datetime.date.today()
                                            fecha_reporte_excel = (f"{fecha_actual}.xlsx")
                                            exportar_excel = registro
                                            libro = openpyxl.Workbook()
                                            hoja = libro["Sheet"]
                                            encabezado = ["CLAVE", "NOMBRE", "RFC", "CORREO"]
                                            hoja.append(encabezado)
                                            for cliente in exportar_excel:
                                                hoja.append(cliente)
                                            hoja.title = "ID_cliente"
                                            libro.save(fecha_reporte_excel)
                                            print("* DATOS EXPORTADOS EXITOSAMENTE *") 
                                            print("")
                                            break
                                            
                                            
                                    elif opcion_decision.upper()=="N":
                                        break
                                    
                               
                            
                                
                        elif opcion_clientes_2=="3":
                            while True:
                                nombre_buscar=input("Ingrese el nombre del cliente:\n")
                                valores = {"nombre": nombre_buscar}
                                try:
                                    fecha_actual = datetime.date.today()
                                    fecha_reporte = (f"{fecha_actual}.csv")
                                    with sqlite3.connect("Taller_Mecanico.db") as conn:
                                        mi_cursor = conn.cursor()
                                        mi_cursor.execute("SELECT id, nombre, rfc, correo FROM clientes WHERE nombre = :nombre and suspendido = 1", valores)
                                        
                                        registro = mi_cursor.fetchall()
                                        
                                        print("")
                                        print("Claves\tNombre\tRFC\t\tCorreo")
                                        print("*" * 60)
                                        if registro:
                                            for clave, nombre, rfc, correo in registro:
                                                print(f"{clave:^6}{nombre}\t{rfc}\t{correo}")
                                                print("")
                                        else:
                                            print(f"No se encontro ningun registro con el nombre: {nombre_buscar} o se encunetra suspendido\n")
                                            break
                                except Error as e:
                                    print(e)
                                except Exception:
                                    print(f"Se produjo el siguiente error: {sys.int_info()[0]}")
                                    print("")
                                else:
                                    opcion_decision = input("Desea exportar estos datos a CSV o Excel?(S/N)\n")
                                    if opcion_decision.upper()=="S":
                                        print("1. CSV")
                                        print("2. Excel")
                                        print("")
                                        opcion_exportar = int(input("Eliga una opcion:\n"))
                                        print("")
                                        if opcion_exportar==1:
                                            encabezados = ["CLAVE", "NOMBRE", "RFC", "CORREO"]
                                            with open(fecha_reporte,"w", newline="") as reporte:
                                                grabador = csv.writer(reporte)
                                                grabador.writerow(encabezados)
                                                for datos in registro:
                                                    grabador.writerow(datos)
                                                print("DATOS EXPORTADOS EXISTOSAMENTE\n")
                                                        
                                        elif opcion_exportar==2:
                                            fecha_actual = datetime.date.today()
                                            fecha_reporte_excel = (f"{fecha_actual}.xlsx")
                                            exportar_excel = registro
                                            libro = openpyxl.Workbook()
                                            hoja = libro["Sheet"]
                                            encabezado = ["CLAVE", "NOMBRE", "RFC", "CORREO"]
                                            hoja.append(encabezado)
                                            for cliente in exportar_excel:
                                                hoja.append(cliente)
                                            hoja.title = "NOMBRE_ordenado"
                                            libro.save(fecha_reporte_excel)
                                            print("* DATOS EXPORTADOS EXITOSAMENTE *")
                                            print("")
                                            break
                                    elif opcion_decision.upper()=="N":
                                        break
                                
                        elif opcion_clientes_2=="4":
                            break
                    
                elif opcion_clientes=="5":
                    break
            
        elif opcion_menu=="3":
            while True:
                print("")
                print("1. Agregar Servicio")
                print("2. Suspender un Servicio")
                print("3. Recuperar un Servicio")
                print("4. Consultas y Reportes")
                print("5. Volver al Menu Principal")
                print("")
                opcion_servcios = input("Eliga una opcion:\n")
                print("")
                if opcion_servcios=="1":
                    nombre = input("Ingresa el nombre del servicio: ")
                    costo = float(input("Ingresa el costo del servicio: "))
                    agregar_servicio(nombre, costo)
                    print("")
                    print("* SERVICIO AGREGADO *")
                elif opcion_servcios == "2":
                    while True:
                        try:
                            with sqlite3.connect("Taller_Mecanico.db") as conn:
                                mi_cursor = conn.cursor()
                                mi_cursor.execute("SELECT id, nombre FROM servicios WHERE suspendido = 1")
                                registro = mi_cursor.fetchall()
                                print("Claves/Nombre")
                                print("*" * 20)
                                if registro:
                                    for clave, nombre, in registro:
                                        print(f"{clave:^7}{nombre}")
                                        print("*" * 20)
                                    servicio_suspender = input("Eliga la clave del cliente a suspender o 0 para salir: ")
                              
                                    print("")
                                    if servicio_suspender == "0":
                                        break
                                    
                                    valores = {"servicio_suspendido": servicio_suspender}
                                    with sqlite3.connect("Taller_Mecanico.db") as conn:
                                        mi_cursor = conn.cursor()
                                        mi_cursor.execute("SELECT id, nombre, costo FROM servicios WHERE id = :servicio_suspendido", valores)
                                        registro = mi_cursor.fetchall()
                                        print("")
                                        print("Datos del Servicio a suspender\n")
                                        print("CLAVE/NOMBRE/COSTO")
                                        print("*" * 50)
                                        for clave, nombre, costo in registro:
                                                print(f"{clave:^6} {nombre} {costo}")
                                                print("*" * 50)
                                                print("")
                                        confirmacion_suspender = input("Desea confirmar esta accion (S) o (N) para regresar al menu anterior: ")
                                        if confirmacion_suspender.upper()=="S":
                                            with sqlite3.connect("Taller_Mecanico.db") as conn:
                                                mi_cursor = conn.cursor()
                                                mi_cursor.execute("UPDATE servicios set suspendido = 0 WHERE id = :servicio_suspendido", valores)
                                                print("")
                                                print("* SERVICIO SUSPENDIDO *")
                                                break
                                        
                                        elif confirmacion_suspender == "N":
                                            break
                                        
                                        else:
                                            print("OPCION INVALIDA\n")
                                            continue
                                            
                        except Error as e:
                            print(e)
                        
                        except Exception:
                            print(f"Se produjo el siguiente error: {sys.int_info()[0]}")
                    
                elif opcion_servcios == "3":
                    while True:
                        print("* SERVICIOS SUSPENDIDOS *")
                        with sqlite3.connect("Taller_Mecanico.db") as conn:
                            mi_cursor = conn.cursor()
                            mi_cursor.execute("SELECT id, nombre FROM servicios WHERE suspendido = 0")
                            registro_servicios_suspendidos = mi_cursor.fetchall()
                            print("CLAVE/NOMBRE")
                            print("*" * 20)
                            if registro_servicios_suspendidos:
                                for clave, nombre, in registro_servicios_suspendidos:
                                            print(f"{clave:^7}{nombre}")
                                            print("*" * 20)
                                print("")
                                servicio_recuperar = input("Seleccione la clave del servicio a recuperar o 0 para regresar: ")
                                if servicio_recuperar == "0":
                                    break
                                
                                if servicio_recuperar:
                                    valores_servicio_recuperar = {"clave_recuperar": servicio_recuperar}
                                    print("Datos del servicio a recuperar\n")
                                    with sqlite3.connect("Taller_Mecanico.db") as conn:
                                        mi_cursor = conn.cursor()
                                        mi_cursor.execute("SELECT id, nombre, costo FROM servicios WHERE suspendido = 0 and id = :clave_recuperar", valores_servicio_recuperar)
                                        datos_servicio = mi_cursor.fetchall()
                                        print("CLAVE NOMBRE COSTO")
                                        print("*" * 60)
                                        for clave, nombre, costo in datos_servicio:
                                            print(f"{clave:^7}{nombre} {costo}")
                                            print("*" * 60)
                                            
                                        confirmacion_recuperar = input("Desea confirmar la recuperacion (S) o (N) para regresar al menu anterior: ")
                                        if confirmacion_recuperar.upper() == "S":
                                            with sqlite3.connect("Taller_Mecanico.db") as conn:
                                                mi_cursor = conn.cursor()
                                                mi_cursor.execute("UPDATE servicios set suspendido = 1 WHERE id = :clave_recuperar", valores_servicio_recuperar)
                                                print("")
                                                print("* SERVICIO RECUPERADO *")
                                                break
                                        else:
                                            if confirmacion_recuperar == "N":
                                                break
                    
                elif opcion_servcios== "4":
                    while True:
                        print("")
                        print("1. Busqueda por clave de servicio")
                        print("2. Busqueda por nombre de servicio")
                        print("3. Listado de Servicios")
                        print("4. Volver al Menu de Servicios")
                        print("")
                        opcion_servcios_2 = int(input("Eliga una opcion:\n"))
                        if opcion_servcios_2 == 1:
                            print("")
                            busqueda_clave_servicios = input("Ingrese la clave del Servicio: \n")
                            valores_servicios = {"clave": busqueda_clave_servicios}
                            try:
                                with sqlite3.connect("Taller_Mecanico.db") as conn:
                                    mi_cursor = conn.cursor()
                                    mi_cursor.execute("SELECT id, nombre, costo FROM servicios WHERE id = :clave and suspendido = 1", valores_servicios)
                                    registro_servicios = mi_cursor.fetchall()
                                    print("")
                                    
                                    if registro_servicios:
                                        print("CLAVE/SERVICIO/\tCOSTO")
                                        print("*" *30)
                                        for clave, nombre, costo in registro_servicios:
                                            print(f"{clave:^6}{nombre}\t{costo}")
                                            print("")
                                    else:
                                        print(f"No se encontrp ningun servicio con la clave: {busqueda_clave_servicios} o se encuentra suspendido")
                            except Error as e:
                                print(e)
                            except Exception:
                                print(f"Se produjo el siguiente errro: {sys.int_info()[0]}")
                                
                        elif opcion_servcios_2 == 2:
                            nombre_servicio = input("Ingrese el nombre del servicio:\n")
                            valores_nombre = {"nombre": nombre_servicio}
                            try:
                                with sqlite3.connect("Taller_Mecanico.db") as conn:
                                    mi_cursor = conn.cursor()
                                    mi_cursor.execute("SELECT id, nombre, costo FROM servicios WHERE nombre = :nombre and suspendido = 1", valores_nombre)
                                    registro_nombre = mi_cursor.fetchall()
                                    
                                    if registro_nombre:
                                        print("CLAVE/NOMBRE/\tCOSTO")
                                        print("*" *30)
                                        for clave, nombre, costo in registro_nombre:
                                            print(f"{clave:^6}{nombre}\t{costo}")
                                            print("")
                                    else:
                                        print(f"No se encontro ningun servicio con el nombre: {nombre_buscar} o se encuentra suspendido")
                            except Error as e:
                                print(e)
                            except Exception:
                                print(f"Se produjo el siguiente error: {sys.int_info()[0]}")

                        elif opcion_servcios_2 == 3:
                            while True:
                                print("")
                                print("1. Ordenado Por Clave")
                                print("2. Ordenado Por Nombre")
                                print("3. Volver al Menu Principal")
                                print("")
                                opcion_servcios_3 = int(input("Eliga una opcion:\n"))
                                
                                if opcion_servcios_3 == 1:
                                    fecha_actual = datetime.date.today()
                                    fecha_reporte = (f"{fecha_actual}.csv")
                                    try:
                                        with sqlite3.connect("Taller_Mecanico.db") as conn:
                                            mi_cursor = conn.cursor()
                                            mi_cursor.execute("SELECT id, nombre, costo FROM servicios WHERE suspendido = 1 Order by id;")
                                            registro_servicios_orden_clave = mi_cursor.fetchall()
                                            if registro_servicios_orden_clave:
                                                print("CLAVE/NOMBRE/\tCOSTO")
                                                print("*" *30)
                                                for clave, nombre, costo in registro_servicios_orden_clave:
                                                    print(f"{clave:^6}{nombre}\t{costo}")
                                                    print("")
                                            else:
                                                print("* Aun no hay servicos *")
                                    except Error as e:
                                        print(e)
                                    except Exception:
                                        print(f"Se produjo el siguiente error: {sys.int_info()[0]}")
                                        
                                    else:
                                        opcion_decision = input("Desea exportar estos datos a CSV o Excel?(S/N)\n")
                                        if opcion_decision.upper()=="S":
                                            print("1. CSV")
                                            print("2. Excel")
                                            print("")
                                            opcion_exportar = int(input("Eliga una opcion:\n"))
                                            print("")
                                            if opcion_exportar==1:
                                                encabezados = ["CLAVE", "NOMBRE", "COSTO", ]
                                                with open(fecha_reporte,"w", newline="") as reporte:
                                                    grabador = csv.writer(reporte)
                                                    grabador.writerow(encabezados)
                                                    for datos in registro_servicios_orden_clave:
                                                        grabador.writerow(datos)
                                                    print("DATOS EXPORTADOS EXISTOSAMENTE\n")
                                        
                                            elif opcion_exportar==2:
                                                fecha_actual = datetime.date.today()
                                                fecha_reporte_excel = (f"{fecha_actual}.xlsx")
                                                exportar_excel = registro_servicios_orden_clave
                                                libro = openpyxl.Workbook()
                                                hoja = libro["Sheet"]
                                                encabezado = ["CLAVE", "NOMBRE", "COSTO"]
                                                hoja.append(encabezado)
                                                for servicio in exportar_excel:
                                                    hoja.append(servicio)
                                                hoja.title = "ID_servicios"
                                                libro.save(fecha_reporte_excel)
                                                print("* DATOS EXPORTADOS EXITOSAMENTE *") 
                                                print("")
                                                break
                                            
                                        elif opcion_decision.upper() == "N":
                                            continue
                                            
                                        
                                elif opcion_servcios_3 == 2:
                                    fecha_actual = datetime.date.today()
                                    fecha_reporte = (f"{fecha_actual}.csv")
                                    try:
                                        with sqlite3.connect("Taller_Mecanico.db") as conn:
                                            mi_cursor = conn.cursor()
                                            mi_cursor.execute("SELECT id, nombre, costo FROM servicios WHERE suspendido = 1 Order by nombre;")
                                            registro_servicios_orden_nombre = mi_cursor.fetchall()
                                            if registro_servicios_orden_nombre:
                                                print("CLAVE/NOMBRE/\tCOSTO")
                                                print("*"*30)
                                                for clave, nombre, costo in registro_servicios_orden_nombre:
                                                    print(f"{clave:^6}{nombre}\t{costo}")
                                                    print("")
                                    except Error as e:
                                        print(e)
                                    except Exception:
                                        print(f"Se produjo el siguiente error: {sys.int_info()[0]}")
                                        
                                    else:
                                        opcion_decision = input("Desea exportar estos datos a CSV o Excel?(S/N)\n")
                                        if opcion_decision.upper()=="S":
                                            print("1. CSV")
                                            print("2. Excel")
                                            print("")
                                            opcion_exportar = int(input("Eliga una opcion:\n"))
                                            print("")
                                            if opcion_exportar==1:
                                                encabezados = ["CLAVE", "NOMBRE", "COSTO", ]
                                                with open(fecha_reporte,"w", newline="") as reporte:
                                                    grabador = csv.writer(reporte)
                                                    grabador.writerow(encabezados)
                                                    for datos in registro_servicios_orden_nombre:
                                                        grabador.writerow(datos)
                                                    print("DATOS EXPORTADOS EXISTOSAMENTE\n")
                                                    
                                            elif opcion_exportar==2:
                                                fecha_actual = datetime.date.today()
                                                fecha_reporte_excel = (f"{fecha_actual}.xlsx")
                                                exportar_excel = registro_servicios_orden_nombre
                                                libro = openpyxl.Workbook()
                                                hoja = libro["Sheet"]
                                                encabezado = ["CLAVE", "NOMBRE", "COSTO"]
                                                hoja.append(encabezado)
                                                for servicio in exportar_excel:
                                                    hoja.append(servicio)
                                                hoja.title = "NOMBRE_servicios"
                                                libro.save(fecha_reporte_excel)
                                                print("* DATOS EXPORTADOS EXITOSAMENTE *") 
                                                print("")
                                                break
                                        elif opcion_decision.upper()=="N":
                                            continue
                                elif opcion_servcios_3 == 3:
                                    break
                                    
                                    
                        elif opcion_servcios_2 == 4:
                            break
                    
                elif opcion_servcios == "5":
                    break