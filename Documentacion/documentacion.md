**Documentación del html**

nombre del html: eleccion.html

**1.** Hacemos un formulario que redirige a un script a ejecutar.

&lt;form action="cgi-bin/eleccion.py" method="get"
enctype="aplication/x-www-form-urlencoded"&gt;

&lt;div&gt; --→ para crear un contenedor de los apartados del
formulario.

2\. Hacemos diferentes listas.

&lt;ol&gt; –→ Lo utilizamos para tener una lista ordenada de cada
apartado.

&lt;ol type="a"&gt;--→ Para tener una lista del tipo (a,b,c,d,….,etc).

&lt;li&gt; --&gt;representa a un ítem en una lista, ya sea ordenada o no
, en nuestro caso es ordenada

para distinguir los diferentes representates de cada partido político.

3\. Hacemos inputs para verificar las 

&lt;input type="checkbox" name="Candidato" value="Manuel j."/&gt;

&lt;input &gt; --→ Representa un campo de datos que normalmente se
asocia con un control que nos permite editar su valor. Este elemento es
capaz de proveer muchos tipos diferetes de campos, de acuerdo al valor
que presente en el atributo “*TYPE”*.

&lt;input **type="checkbox"** &gt; → Es para la verificación de la
opción a escoger .

En contraste con los botones de opción que pueden conformar grupos donde
solo una opción puede ser seleccionada a la vez, las casillas de
verificación son independientes.

&lt;input **type="hidden"**&gt; → representa cualquier cadena de texto
arbitraria que no está pensada para ser vista o editada por el usuario.

&lt;button **type="submit"**&gt; → representa el envio de opciones
seleccionadas anteriormente.

Documentacion scritp: **eleccion.py**

1\. Hacemos un imput del cgi y sys.

2\. Hacemos un getlist del formulario para obtener los nombres de los
candidatos seleccionados.

candidatos = form.getvalue("Candidato")

3\. Creamos un diccionario con los partidos que tenemos a disposición.

d = {1:'1 PSOE',2:'2 PP',3:'3 PDeCAT',4:'4 PODEMOS',5:'5 Cs',6:'6 CUP'}

4\. Luego guardamos cada representante al diccionario con su partido
correspondiente.

5\. Mostramos por cada partido , el representante elegido

for k1 in l:

print 'Partido :',l\[k1\]\[0\]

print '-----------------&gt;Rep. Elegido:' ,l\[k1\]\[1\]
