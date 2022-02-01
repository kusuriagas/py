
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

