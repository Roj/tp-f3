---
title: "Informe: difracción de electrones"
toc: yes
author:
- Agustín Santiago Zuretti (95605)
- Fabrizio Sebastián Graffe (93158)
- Joaquin Torré Zaffaroni (98314)
---

## Introducción

La primera persona en proponer que la materia tiene comportamiento tanto 
ondulatorio como corpuscular fue Louis de Broglie, en 1924. Así como se sabía que 
la luz tiene propiedades ondulatorias y corpusculares, postuló que la materia 
también tendría una dualidad en su comportamiento.

Los primeros en observar el fenómeno de difracción fueron Davisson y Germer en 
los laboratorios de Bell Telephone. Ellos se encontraban estudiando la dispersión
de un haz de electrones contra un blanco de níquel. Luego de un largo periodo 
de bombardeo de electrones notaron sobre la placa receptora máximos y mínimos 
de intensidad, en función del ángulo y la tensión de aceleración.

De esta manera encontraron evidencia de un comportamiento de la materia que
no corresponde al modelo de partícula sino a un modelo de onda; es decir,
la materia también presentaba una dualidad onda-partícula en su comportamiento.

![Difracción de electrones.](difraccion.png)

![Dispositivo experimental de Davisson y Germer.](experimento.png)

## Método experimental  

   ![Dispositivo experimental](geometria_experimento.png)

Para llevar a cabo la experiencia se utilizó un bulbo en el cual electrones 
acelerados mediante un potencial atraviesan un policristal de grafito y son 
difractados con cierto ángulo, finalmente chocando contra una placa de fósforo.

Cada uno de los potenciales que se ven en la figura cumple una función. G1 es 
un potencial de frenado que detiene a los electrones más débiles. G2 y G4 
enfocan y coliman el haz de electrones y G3 se encarga de acelerarlos.

El fenómeno de difracción se manifiesta en el bulbo mediante anillos que 
varían su radio dependiendo del potencial que acelera los electrones.

Las herramientas utilizadas en la experiencia fueron un multímetro para medir 
el potencial de aceleración y un vernier para medir el diámetro de los anillos 
de difracción.

Para lograr mayor precisión se midió el diámetro exterior e interior de cada 
anillo y luego se calculó su promedio.

### Instrumentos utilizados
-   Fuente de alta tensión
-   Tubo de difracción de electrones
-   Pantalla de fósforo
-   Cables conductores
-   Resistencias (10M )
-   Fuente VDC
-   Calibre
-   Divisor de tensión para lectura del altimetría
-   Altímetro

### Procedimiento de medición
1.  Se arma el banco de medición con los dispositivos ya nombrados como se ve en la figura. Además se usa un divisor de tensión para obtener una lectura más precisa.
2.  Se va variando la tensión de la fuente y se fija.
3.  Se miden los diámetros internos y externos de los anillos de Debye-Scherrer con un calibre. Se miden solo los anillos más intensos que se observan (para todo V).
4.  Se repiten los pasos (2) y (3) hasta los 9kV.


Como se ve en la figura, sobre la pantalla de fósforo se observan anillos concéntricos denominados anillos de Debye-Scherrer. Este patrón de interferencia se produce como ya se mencionó por la estructura del material utilizado como red espacial de difracción, que al tener variedad de planos con disposiciones angulares diferentes, hacen que aparezcan circunferencias en la pantalla perpendicular a la dirección de incidencia. En cuanto a la manera de medir los anillos, decidimos medir su diámetro, disminuyendo el error que se cometería queriendo ubicar el eje central de los círculos

Al tener todas las mediciones de los anillos, podemos calcular los ángulos de Bragg para tales. Viendo la figura, se ve claramente que se puede determinar con la siguiente relación trigonométrica (cuya demostración se puede ver en el apéndice)

$$\theta = \frac{1}{4} \arcsin\left (\frac{r}{R} \right )$$


siendo $\theta$ el ángulo de Bragg, $r$ el diámetro del anillo y $R$ el 
diámetro del bulbo.


## Resultados y análisis

En la siguiente tabla podemos ver los resultados obtenidos en las mediciones. En
tipo de anillo, G significa anillo grande y C anillo chico.

### Resultados obtenidos
En la siguiente tabla podemos ver los resultados obtenidos en las mediciones. En la columna "Anillo", G significa anillo grande y C anillo chico.


| $T[keV]$     | $\Delta T[keV]$ |  $d_{int}[\AA]$ |  $d_{ext}[\AA]$ |  Anillo|
|---------|------------|-------|-------|-------|
| 4.07    |  0.04      |  3.71 |  4.30 |  G    |
| 4.07    |  0.04      |  2.11 |  2.50 |  C    |
| 4.99    |  0.04      |  3.40 |  3.92 |  G    |
| 4.99    |  0.04      |  1.88 |  2.23 |  C    |
| 6.05    |  0.06      |  3.19 |  3.55 |  G    |
| 6.05    |  0.06      |  1.75 |  2.00 |  C    |
| 6.99    |  0.06      |  2.91 |  3.28 |  G    |
| 6.99    |  0.06      |  1.71 |  1.90 |  C    |
| 8.04    |  0.06      |  2.87 |  3.17 |  G    |
| 8.04    |  0.06      |  1.64 |  1.87 |  C    |

### Análisis de los resultados


   ![Resultados experimentales.](resultados_experimentales.png)

En el gráfico superponemos los resultados experimentales y los valores de
los diámetros en función de la tensión para algunas distancias interplanares
conocidas.  
A partir del gráfico de los resultados podemos ver que los anillos medidos
(que, a diferencia de las líneas que representan los anillos teóricos 
calculados antes, *sí* tienen espesor) encierran en su parte brillante a más
de una curva de distancia interplanar.

En el caso del anillo grande, vemos que se encierra al anillo de nivel $1$ del
plano con $d = 1.16\AA$ y del mismo nivel $d = 1.2340\AA$. En el chico, vemos
que los anillos encerrados son $d = 2.0390\AA$ y $d = 2.1386$ del nivel $1$.  

Postulamos, entonces, que no sólo una distancia interplanar contribuye al 
patrón de interferencia que observamos con los anillos, sino que son múltiples.

Estas observaciones se cumplen para todas las mediciones excepto la de 
$\mathrm{Tension} = (8.04 \pm 0.06)kV$, en la que en ambos anillos sólo queda
una distancia interplanar adentro. En ambos casos hay un aumento del valor que
logra esto. Esto puede ser una sobre-estimación del valor, y puede deberse
a un error bajo en la medición del diámetro. Para definirlo, sólo tomamos el 
error de apreciación del instrumento ($e_{ap} = 0.1mm$), pero las condiciones
de medición aumentan el error: el hecho de que se mida el punto en el que la luz
deja de ser brillante y que no sea una línea tan definida, la medición en la 
oscuridad, la curvatura del bulbo. 

Teniendo en cuenta estos factores que aumentan el error, podríamos tomar
el hecho de que en la última medición se descarte una distancia interplanar 
en cada anillo es debdio a una sub-estimación del error. Esto cobra especial
importancia en el caso del anillo chico, donde se ve que la diferencia es
mínima.

Utilizando los postulados de De Broglie y la hipótesis no relativista 
(que en el apéndice se ve que tiene un error menor al $1\%$ en este orden
de energías) podemos calcular las longitudes de onda de las funciones de onda
asociadas a los electrones, con la siguiente relación:
$$\lambda = \frac{h}{\sqrt{2m_e T}}$$
donde $h$ es la constante de Planck, $m_e$ la masa del electrón y $T$ la tensión
con la cual se acelera a los electrones.
Los resultados obtenidos se pueden ver en la tabla siguiente.

| $T[keV]$ | $\Delta T [keV]$ |  $\lambda [\AA]$ |  $\Delta \lambda [\AA]$ |
|---------|------------|-------|-------
| 4.07    |  0.04      |  0.1922     |       
| 4.99    |  0.04      |  0.1736     |       
| 6.05    |  0.06      |  0.1576     |       
| 6.99    |  0.06      |  0.1467     |       
| 8.04    |  0.06      |  0.1367     |      

Para calcular $\Delta \lambda$ utilizamos propagación lineal de variables.
Usamos la siguiente expresión:

$$\Delta \lambda(T, \Delta T) =
\left |
	\frac{\partial}{\partial T} \left (
		\frac{h}{\sqrt{2m_e T}}
	\right )(T) \times \Delta T
\right | = \frac{h}{2\sqrt{m_e}\ T^{3/2}} \Delta T$$

## Conclusiones

En el presente experimento se trabajó los postulados de De Broglie y se
replicaron los resultados del experimento de Davisson-Germer (con un esquema
experimental distinto). Se observó el comportamiento ondular de los electrones
y, bajo los postulados de De Broglie, se calculó la longitud de onda de la 
función de onda asociada.

En base al comportamiento de difracción de la materia se determinaron
propiedades del material de grafito utilizado.

## Apéndice - cuestionario

### Experimento de Davison-Germer y la Ley de Bragg

El experimento de Davisson y Germer demostró que los objetos corpusculares presentaban un carácter ondulatorio, corroborando la hipótesis de Louis-Victor de Broglie, en la que expone que toda la materia, (electrones, átomos o moléculas), presenta características tanto corpusculares como ondulatorias.

En este experimento, un monocristal es bombardeado con electrones acelerados por un potencial eléctrico V. Suponiendo que  los electrones presentan un comportamiento ondulatorio, la onda incidente se refleja en cada uno de los planos atómicos, existiendo una interferencia constructiva de las ondas reflejadas en planos paralelos consecutivos descritos por la Ley de Bragg.

Lo que se observa es que estos son reflejados mayoritariamente en aquellas direcciones privilegiadas para las que exista interferencia constructiva, lo cual demuestra la hipótesis de de broglie.


Cuando los rayos X alcanzan un átomo interactúan con sus electrones exteriores. Estos reemiten la radiación electromagnética incidente en diferentes direcciones y con la misma frecuencia (en realidad debido a varios efectos hay pequeños cambios en su frecuencia). Este fenómeno se conoce como dispersión de Rayleigh (o dispersión elástica). Los rayos X reemitidos desde átomos cercanos interfieren entre sí constructiva o destructivamente. Este es el fenómeno de la difracción.

![ley de bragg.](bragg.png)

La radiación incidente llega a átomos consecutivos con un ligero desfase (izquierda). La radiación dispersada por los átomos (círculos azules) interfiere con radiación dispersada por átomos adyacentes. Las direcciones en las que los círculos se superponen son direcciones de interferencia constructiva.

La interferencia es constructiva cuando la diferencia de fase entre la radiación emitida por diferentes átomos es proporcional a 2 pi. Esta condición se expresa en la ley de Bragg:

$$\ n \lambda = 2 d \sin(\theta)$$

### Relación entre longitud de onda y energía cinética  

La ecuación que nos va a permitir relacionar la longitud de onda y la energía
cinética principalmente será la de de Broglie: $\lambda = \frac{h}{p}$,
y dependiendo de las condiciones del problema, podemos usar la ecuación de la
energía cinética de la mecánica clásica o deberemos usar la de la mecánica
relativista.   

En el caso clásico, donde la energía cinética del electrón es relativamente
pequeña respecto a la energía asociada a la masa en reposo, podemos usar la
asociación entre energía cinética y cantidad de movimiento lineal:   

$$\ n \lambda = \frac{h}{\sqrt{2m_e 10keV}} = 0,1226 \AA$$

$$\mathrm{E}_c = \frac{p^2}{2m}$$ 

Al reemplazar la cantidad de movimiento $p$ por $\frac{h}{p}$
obtenemos: 

$$ \lambda = \frac{h}{\sqrt{2m\mathrm{E}_c}} $$

En el caso que la aproximación clásica no se pueda utilizar dadas las
condiciones del problema, será necesario usar las ecuaciones de la mecánica
relativista. En este caso tenemos el par de ecuaciones:

$$
\left\{\begin{matrix}
	\mathrm{E} = mc^2 + \mathrm{E}_c + \mathrm{E}_p\\
	\mathrm{E}^2 = (pc)^2 + (mc^2)^2
\end{matrix}\right.
$$

Para este experimento, nos interesa analizar el estado del electrón en el
instante que sale del tubo. Si definimos el potencial eléctrico en ese punto
como el cero de referencia podemos considerar $\mathrm{E}_p = 0$. En el viaje
desde la expulsión desde el electrón hasta el choque contra la pantalla de
fósforo no hay es necesario considerar ningún campo eléctrico o gravitatorio.

Sustituyendo la primera ecuación en la segunda, y aplicando la misma sustitución
de cantidad de movimiento por las variables asociadas a la onda de la materia,
terminamos con la siguiente expresión:

$$\lambda = \frac{hc}{\sqrt{\mathrm{E}_c(\mathrm{E}_c + 2mc^2)}}$$

### Cambio de la longitud de onda de los electrones

Como $\lambda = \frac{h}{p}$ (de los postulados de de Broglie), se debe campiar
el impulso de los electrones para cambiar su onda. Esto lo podemos lograr
controlando la tensión del circuito acelerador.

Si $V_{max} = 10 kV$, entonces $\mathrm{E}_c^{max} = 10 keV$.   

Utilizando la hipótesis no relativista obtenemos:  

$$\lambda_{clasico} = \frac{h}{\sqrt{2m_e 10keV}} = 0,1226 \AA$$   

Utilizando las ecuaciones de la mecánica relativista logramos:

$$\lambda_{relativista} = \frac{hc}{\sqrt{10keV(10keV + 2m_ec^2)}}
= 0,1220 \AA$$  

Lo cual nos da un error porcentual de $e_r \approx 0,5\%$.


### Aparición de anillos en el bulbo

Dado que el policristal que se utiliza en el experimento fue molido, 
la orientación de las estructuras regulares del cristal se vuelve aleatoria, y
esto le termina dando una simetría de revolución a la dispersión de las ondas de
los electrones.

### Ángulo de dispersión

   ![Dispersión de las ondas bajo hipótesis de Bragg](cuestionario_e.svg.png)


### Minimización del error de medición  

El calibre es un instrumento bastante sencillo con un error de apreciación bajo
($e_{ap} = 0.1\mathrm{mm}$). Una opción sería medir directamente el espesor de cada
anillo, pero entonces el error de apreciación será relativamente alto respecto
al mensurando.    

Una manera mejor es medir los radios internos y externos por separado, para
medir de manera indirecta el espesor. Si bien el error absoluto se duplicará
(por propagación lineal, el error de la suma es la suma de los errores),
relativamente a la magnitud que se mide será mucho menor.

### Cálculo del $\theta$ sin aproximación  

En la Figura 3 podemos ver la geometría del dispositivo experimental. Esto nos
permite ver cómo se relaciona el ángulo de dispersión (y en definitiva el ángulo
de Bragg) con las dimensiones del bulbo y de los anillos que se observan en la
pantalla de fósforo.

   ![Geometría del experimento](geometria_experimento.png)

Usando la notación del gráfico, observamos que: 

$$\sin (2\alpha) = \frac{r}{R} \Rightarrow \theta = \frac{1}{4}
\arcsin\left (\frac{r}{R} \right )$$

Y esto nos da un método sin aproximaciones para calcular el ángulo de Bragg, ya
que $r$ es lo que medimos (el radio del anillo) y $R$ es conocido (el radio del
bulbo).

### Tablas de $\theta$ para distintos $n, v, d$  

   ![Diámetro de los anillos para distintos $d$ en respuesta a distinta tensión, n = 1](nivel_1.png)
   ![Diámetro de los anillos para distintos $d$ en respuesta a distinta tensión, n = 2](nivel_2.png)
