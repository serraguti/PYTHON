import pyodbc
servidor = 'localhost'
nombre_bd = 'HOSPITAL'
nombre_usuario = 'sa'
password = 'MCSD2021'
# print("Introduzca un departamento: ")
# deptno = input()
conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          servidor + ';DATABASE=' + nombre_bd + ';UID=' 
                          + nombre_usuario)

cursor = conexion.cursor()
# consulta = ("SELECT emp_no, apellido FROM emp "
#             " where dept_no=" + deptno)
# consulta = ("SELECT emp_no, apellido FROM emp "
#             " where dept_no=?")
# consulta = ("SELECT emp_no, apellido FROM emp "
#             " where dept_no=? or dept_no=?")            
# cursor.execute(consulta, (deptno, 20))
#cursor.execute(consulta, (deptno))
#cursor.execute(consulta, (deptno, 20))
#consulta = "{ CALL empleadosdepartamento (?) }"
#cursor.execute(consulta, (deptno))
# consulta = "insert into dept values(?,?,?)"
# params = (50, 'I+D', 'SEVILLA')
# cursor.execute(consulta, params)
# cursor.commit()
# print("Dato insertado")
# cursor.close()
sql = "select * from dept"
cursor.execute(sql)
print(cursor.rowcount)
# for c in cursor.columns():
#     print(c)
for row in cursor:
    #print(row["DNOMBRE"])
    #print(row[1])
    print(row.DNOMBRE)
cursor.close()    
# print("Lista de empleados:")
# print("---------------------------------------")

# for numero, ape in cursor:
#     print("Número empleado:", numero, "Apellido:", ape)


conexion.close()