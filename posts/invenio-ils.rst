.. post:: Oct 31, 2023
   :tags: software, open source, catalogación
   :category: Sistema de Gestión Bibliotecaria
   :author: Luis Enrique Lescano Borrego
   :exclude:

   Koha es un sistema integrado de gestión de bibliotecas (SIGB) de código abierto utilizado para administrar bibliotecas y sus recursos. Permite gestionar catálogos, préstamos, adquisiciones, inventarios, y otros aspectos ...

.. meta::
   :description: Koha - Sistema de Gestión de Bibliotecas de Código Abierto | Catálogo en Línea y Préstamo de Materiales
   :keywords: Koha, gestión de bibliotecas, software de código abierto, catálogo en línea, préstamo de materiales, biblioteca open source


***************
Invenio ILS
***************
:bdg-info-line:`software` :bdg-info-line:`open source` :bdg-info-line:`catalogación`

.. admonition:: Invenio ILS Logo
    :class: sidebar tip

    .. image:: ../_static/images/invenio-ils-logo.png
       :align: center
       :height: 200
       :width: 260
      
    *Creado por el CERN*


Invenio ILS es un sistema de gestión de bibliotecas de código abierto diseñado para optimizar y simplificar la administración de recursos bibliográficos, así como facilitar el acceso y la búsqueda de información en entornos bibliotecarios y de gestión de colecciones. Su nombre "ILS" proviene de *"Integrated Library System"* o *"Sistema Integrado de Biblioteca"*, lo que refleja su capacidad para unificar una amplia gama de tareas y servicios en una sola plataforma.

Invenio ILS fue desarrollado por el Centro Europeo de Investigación Nuclear (CERN), una organización internacional de investigación en física de partículas con sede en Ginebra, Suiza. El desarrollo de Invenio comenzó como parte de un esfuerzo por parte del CERN para gestionar y compartir su vasta cantidad de información científica y técnica de manera más efectiva.

.. admonition:: Datos técnicos  
   :class: important

   | **Año de creación**: 2020. 
   | **Lanzamientos**: Todavía no tiene una versión estable. 
   | **URL**: https://inveniosoftware.org/products/ils/ 
 
======================
✨ Caracterísitcas
======================

Invenio ILS ofrece una variedad de funcionalidades clave:

#. **Catalogación:** Invenio ILS proporciona un modelo de datos basado en JSON Schema con registros bibliográficos estructurados, como Documentos, Series, Elementos, Elementos Electrónicos y más. Esto facilita la catalogación y organización de la colección de la biblioteca de manera eficiente.

   .. warning:: 

       La clasificación se basa en el uso de una estructura de JSON en lugar de emplear un formato de descripción como MARC. Esto es muy interesante, ya que simplifica significativamente el proceso de descripción.

#. **Circulación:** El flujo de trabajo de circulación es configurable y extensible. Administre las solicitudes y préstamos de los usuarios con facilidad a través de simples clics. Utilice los paneles de control disponibles para obtener una visión general rápida de las tareas pendientes.
#. **Adquisiciones e ILL (Préstamo interbibliotecario):** Módulos de adquisiciones e ILL simples que permiten llevar un registro de los elementos recién adquiridos. Esto es fundamental para gestionar la expansión de la colección y facilitar el acceso a recursos de otras bibliotecas.
#. **Potente Backoffice:** Herramientas de backoffice fáciles de usar que incluyen listas, herramientas de búsqueda y detalles de cada registro bibliográfico. Además, proporciona una gestión sencilla del flujo de trabajo de circulación, lo que mejora la eficiencia en la gestión de recursos de la biblioteca.
#. **Interfaz de Usuario Moderna:** Una atractiva interfaz de usuario diseñada pensando en los usuarios, lo que facilita la búsqueda de contenido y el proceso de préstamo de libros. Los usuarios encontrarán una experiencia más amigable y accesible.
#. **API REST:** Invenio ILS también ofrece una API REST que permite recuperar o incorporar contenido de manera eficiente y facilita la integración con otros sistemas. Esto potencia la conectividad y la expansión de las funcionalidades del sistema en un entorno de gestión de bibliotecas.

.. admonition:: Servidores de prueba

    Si desea probar este sofware puede acceder a su versión demo en el siguiente link: https://invenioils.web.cern.ch/

======================
📉 Desvenjatas
======================

#. **Falta de Interoperabilidad mediante OAI:** Invenio ILS carece hasta el momento de la capacidad de interoperabilidad a través del Protocolo OAI-PMH, lo que limita la capacidad de compartir datos y recursos con otras bibliotecas o repositorios que utilizan este protocolo como estándar. Esto puede dificultar la colaboración y la ampliación de las colecciones entre instituciones.
#. **Descripción no basada en Estándares de Catalogación:** La descripción de los recursos no se base en estándares de catalogación ampliamente reconocidos, como MARC (Formato de Registro de Autoridad y Catálogo). Esto puede dificultar la consistencia y la interoperabilidad de los registros bibliográficos, lo que es esencial para el intercambio de información entre bibliotecas y sistemas.
#. **Falta de una Versión Estable:** La falta de estabilidad puede dar lugar a problemas de funcionamiento, errores y limitaciones en la funcionalidad. Los usuarios pueden enfrentar dificultades al implementar y mantener el software en sus bibliotecas debido a la falta de una versión sólida y probada en la que confiar.


======================
🔗 Enlaces útiles
======================

#. Aprenda más sobre Invenio ILS visitando su documentación oficial: https://invenioils.docs.cern.ch/
#. Para comunicaciones más directas puede visitar su canal de Discord: https://discord.gg/8qatqBC


======================
📝 Notas
======================
.. note:: 
   Invenio ILS se puede instalar localmente con Docker para fines de prueba y evaluación. Esto te permite explorar sus características en un entorno controlado antes de una implementación completa. Asegúrate de consultar la documentación de Invenio para obtener instrucciones detalladas sobre la instalación a través de Docker. La instalación de esta manera puede llegar generar problemas.

.. note:: 
     Invenio ILS no solo permite la gestión de libros electrónicos en acceso abierto y restringido, sino que también facilita la realización de préstamos de estos recursos, ofreciendo a las bibliotecas una solución integral para la administración y el acceso a colecciones digitales.
