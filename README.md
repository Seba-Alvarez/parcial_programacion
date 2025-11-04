# parcial_programacion

Sistema de Gestión en Python con Tkinter, SQLite y Pytest


El Proyecto fue creado usando la estructura clásica de capas lógicas.
Estas son:
La capa de persistencia, donde fue usado SQLite3.
La capa lógica, de negocios o backend que fue manejada clases de python.
La capa presentación, ui o frontend que fue manejada con con Tkinter.
Finalmente, los testeos que fueron creados con con Pytest


Para conocer los requisitos de instalación, referirse al requirements.txt dentro del mismo repositorio.
Para instalarlos usar:
pip install -r requirements.txt


Para ejecutar el programa hay que correr el siguiente comando en la consola:
python -m gui.main


Para ejecutar las pruebas automáticas hay que correr el siguiente comando en la consola:
pytest -s -v


Cada test:
Crea la tabla correspondiente, luego inserta un registro, lo modifica y lo elimina.
Verificando los resultados de cada operación.


Fundamentación de diseño:
Debido al scope que trae realizar una app como esta, siempre se pueden agregar más cosas. Pero como es un proyecto educativo, decidimos dejar los cruds funcionando para que sea la base del proyecto y en un futuro poder continuar avanzando.
Las principales decisiones de diseño vinieron a la hora de elegir las librerías a usar. Decidimos usar tkinter para la interfaz y SQLite3 para el manejo de base de datos. La primera decisión fue porque un compañero nos proporcionó una lista de videos sobre como usar tkinter. La segunda fue por la familiaridad de uno de los integrantes con la creación de bases de datos en SQL.


Como hitos, se inició el programa haciendo las clases sobre consola. Luego agregamos persistencia a la misma. El tercer paso fue pasar lo local a una interfaz de escritorio. Finalmente le agregamos la persistencia a la interfaz.
Cabe aclarar que originalmente se buscaba hacer que la ventana fuera igual a windows xp, pero no pudimos hacer funcionar dicha funcionalidad, por lo cual quedó vanilla.


Fundamentación didáctica.
Como trabajo final de programación hemos elegido crear una app de escritorio en la cual los docentes suben problemas para que los alumnos las resuelvan. En un futuro nos gustaría completarla para poder corregir y evaluar las respuestas.
El proyecto está inspirado en el libro de nuestro profesor, 1001 problemas en la cual él sube problemas para que sus alumnos los vayan resolviendo. Creemos que este modus operandi encaja con la fundamentación didáctica planteada por George Polya que reconoce la necesidad de contar con un entorno digital estructurado para la práctica de resolución de problemas.
Nosotros, desde nuestra perspectiva de alumnos, hemos intentado emular el modelo exitoso de nuestro profesor para ofrecer una herramienta focalizada y accesible, que si bien es más modesta, también puede centralizar la práctica de la resolución de problemas en un contexto informático o de programación.
Por lo que al enfoque didáctico respecta, como ya hemos mencionado anteriormente, la aplicación se alinea con la didáctica de resolución de problemas, un enfoque central en la enseñanza de la informática. Este enfoque subraya que el aprendizaje significativo ocurre cuando el estudiante se enfrenta a un desafío y debe diseñar activamente una estrategia para superarlo.
El uso de la aplicación, al igual que el libro diseñado por Domingo y Blanca, intenta promover las siguientes competencias:
Práctica frecuente: ofreciendo un repositorio constante y accesible de problemas.
Organización y trazabilidad: centrando las tareas y soluciones, facilitando al docente la asignación y seguimiento.
Habilidades de programación: la resolución de problemas de programación como herramienta para introducir a los alumnos a la materia.
Feedback (en un futuro): al incluir la corrección y evaluación, se cerrará el ciclo de aprendizaje, proporcionando una devolución al alumno para que pueda seguir mejorando.
George Polya fue un matemático cuyo trabajo sentó las bases de la didáctica moderna en este ámbito, especialmente relevante en disciplinas como la matemática y la informática por lo que consideramos que encaja bien con nuestro proyecto. Durante sus longevos 102 años de vida entre otras, desarrolló una obra fundamental; How to Solve It (1945, que describe un método de cuatro fases para abordar cualquier problema, lo que es aplicable directamente a los desafíos de programación que los docentes subirán a nuestra app.:
Comprensión del problema: identificando la meta, los datos y las condiciones.
Concebir un plan: buscando una estrategia, como un algoritmo o un patrón similar.
Ejecutar el plan: llevando a cabo la estrategia, comprobando cada paso.
Examinar la solución: verificando el resultado y reflexionando sobre la estrategia.
La aplicación actúa como la herramienta tecnológica que facilita al docente la gestión de las fases a la 3, siendo que el docente sube el problema, el alumno elabora el plan y aplica la solución para generar una respuesta final y la sube a la aplicación. En el futuro, con la implementación de las correcciones, podremos llegar a la fase 4.
Al centrarse en la actividad del alumno para encontrar la solución, la aplicación promueve la heurística, es decir, el arte de descubrir como procedimiento práctico y no riguroso para resolver problemas, que es el eje central de la propuesta de Polya.
Características clave de la heurística:
Estrategias generales: no son reglas fijas sino guías flexibles para aumentar la probabilidad de encontrar la resolución del problema.
Enfoque en el proceso: proceso de descubrimiento y camino hacia la solución, más que respuesta final en sí misma.
No algorítmicas: las heurísticas son métodos intuitivos y creativos que aplican cuando el algoritmo no existe o es demasiado complejo.
Aprendizaje y meta-cogniición: su uso fomenta la reflexión sobre cómo se piensa resolver un problema, permitiendo al estudiante transferir esa habilidad a nuevos desafíos.
Para George Polya, la heurística es la disciplina que estudia los métodos y las reglas del descubrimiento y la invención. Él la conectó en su famoso método de cuatro pasos para la resolución de problemas: comprensión, planificación, ejecución y revisión.
Nuestra aplicación promueve la heurística porque el alumno debe descubrir el mejor algoritmo o estructurar datos para resolver el problema, utilizando estrategias como buscar un problema análogo, simplificación del problema en partes más pequeñas y la retrospección en busca de un programa similar resuelto anteriormente por él mismo.
La heurística, es por tanto, el motor cognitivo que nuestra aplicación, al igual que el libro de nuestro profesor en el cual nos inspiramos, busca desarrollar; el alumno no solo aplica una fórmula, sino que inventa el camino para llegar a la solución.


Licencia
Este proyecto se distribuye bajo licencia MIT.