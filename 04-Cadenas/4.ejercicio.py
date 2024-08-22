#CREAR jorge.orellana@jeoitservice.com.ar

nombre = 'Jorge Orellana'
nombre_email = nombre.replace(' ', '.')

empresa = 'JeO IT Service'
arroba = "@"
empresa_email = empresa.replace(' ', '')

dominio = '.com.ar'
#dominio_email = empresa_email+dominio
email = nombre_email+arroba+empresa_email+dominio


print(email.lower())
