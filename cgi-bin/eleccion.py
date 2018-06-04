#!/usr/bin/python

'''
nombre: Franlin Colque S.
ident: isx1535386
data:04/06/2018
M04 extraordinaria
descrip: scrip cgi de procesar un formulario de elecciones .
'''

import sys
import cgi

# Debug
#import cgitb; cgitb.enable()

write = sys.stdout.write

form = cgi.FieldStorage()

# headers
write("Content-Type: text/plain; charset=UTF-8\r\n") # or "text/html"...
write("\r\n")
#obtenemos una lista de los candidatos seleccionados
candidatos = form.getvalue("Candidato")
#creamos un diccionarios con los partidos existenetes en nuestro formulario
d = {1:'1 PSOE',2:'2 PP',3:'3 PDeCAT',4:'4 PODEMOS',5:'5 Cs',6:'6 CUP'}
#guerdamos los candidatos en cada partido correspondiente
l = { k: [v, candidatos[k - 1]] for k, v in d.items() }
#mostramos al cliente las opciones que ha elegido el
for k1 in l:
	print 'Partido :',l[k1][0]
	print '----------------->Rep. Elegido:' ,l[k1][1] 
#salimos
sys.exit(0)


