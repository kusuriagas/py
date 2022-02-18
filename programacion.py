
import datetime as dt

print(dt.time(1,30,45)) #Devuelve una hora hh:mm:ss
now=dt.datetime.now() #obtine la fecha del sistema
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

diff=dt.datetime(2022,1,31)-dt.datetime(2022,1,30) # resta de fechas devuelve dias
print(diff)
inc=dt.timedelta(days=2 ,hours=7) # Objeto para agregar 2 dias + horas
print(now+inc)

#String to Datetime:

str_date="30-01-2022"
str_date=dt.datetime.strptime(str_date,"%d-%m-%Y")

str_date="30/01/2022"
str_date=dt.datetime.strptime(str_date,"%d/%m/%Y")
print(str_date)


# Funciones Anidadas

def calculadora(a, b, operacion='sumar'):
    # 1. Definir Función anidada
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    # 2. Llamamos a la función anidada
    if operacion == 'sumar':
        print(f'Resultado sumar: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado restar: {restar(a, b)}')

calculadora(5, 6)
calculadora(4, 3, operacion='restar')

#Manejo de archivos de python
with open('C:\\Users\\user\\Desktop\\FileServer\\Northwind\\Categories.txt','w',encoding='utf8') as archivo:
	archivo.write('agregamos texto al archivo linea 1 \n')
	archivo.write('agregamos texto al archivo linea 2 \n')
	archivo.write('agregamos texto al archivo linea 3 \n')
	archivo.write('agregamos texto al archivo linea 4 \n')
	archivo.write('agregamos texto al archivo linea 5 Televisión')

with open('C:\\Users\\user\\Desktop\\FileServer\\Northwind\\Categories.txt','r',encoding='utf8') as file:
	for linea in file:
		print(linea)
	print(file.readlines())#devuelve una lista




ejercicios numeros primos

for i  in  range(2,51):
	estado=True
	for j in range(2,i):
		if i%j==0:
			estado=False
			break
	if estado:print('primo',i)
    
*********************************************    
    
 class Alumno:


	def __init__(self,CodAlumno,Nombre):
		self.CodAlumno=CodAlumno
		self.Nombre=Nombre
		self.ListaCurso=[]

	def AgregarCurso(self,curso):
		self.ListaCurso.append(curso)



class Alumno:


	def __init__(self,CodAlumno,Nombre):
		self.CodAlumno=CodAlumno
		self.Nombre=Nombre
		self.ListaCurso=[]

	def AgregarCurso(self,curso):
		self.ListaCurso.append(curso)



objalumno=Alumno('c001','kenyo')
objalumno.AgregarCurso('php')
objalumno.AgregarCurso('java')
print(objalumno.CodAlumno)
print(objalumno.ListaCurso)

