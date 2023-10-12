.. post:: Oct 11, 2023
   :tags: sgb, catalogación
   :category: Sistema de Gestión Bibliotecaria
   :author: Luis Enrique Lescano Borrego
   :language: es

**********
Koha
**********

Koha es un sistema integrado de gestión de bibliotecas (SIGB) de código abierto utilizado para administrar bibliotecas y sus recursos. Permite gestionar catálogos, préstamos, adquisiciones, inventarios, y otros aspectos relacionados con la gestión de una biblioteca.

Las funciones principales de Koha incluyen el registro y catalogación de materiales bibliográficos, gestión de préstamos, generación de informes, automatización de procesos, administración de suscriptores, y facilitar el acceso a la información de la biblioteca para usuarios. Al ser de código abierto, se puede personalizar y adaptar según las necesidades específicas de cada biblioteca, lo que lo convierte en una herramienta flexible y escalable para diferentes entidades bibliotecarias.

.. admonition:: Datos técnicos  
   :class: important

   | **Año de creación**: 2000. 
   | **Lanzamientos**: Versiones de mantenimiento mensuales y versiones de funciones semestrales. 
   | **OAI**: Soporta el protocolo OAI-PMH
   | **URL**: https://koha-community.org/download-koha/ 
 
======================
Caracterísitcas
======================

Koha, como software de gestión de bibliotecas de código abierto, presenta diversas características clave:

#. **Cumplimiento de estándares bibliotecarios**: Koha adhiere a importantes estándares bibliotecarios, como MARC21, Z39.50, SIP2, SRU, UNIMARC, y otros, asegurando la interoperabilidad y compatibilidad con otras bibliotecas y sistemas.
#. **Personalización del OPAC**: Modificación de hojas de estilo CSS (Cascading Style Sheets) para ajustar la apariencia visual del OPAC. Esto incluye la personalización de colores, fuentes, tamaños de texto y diseños. Edición de plantillas HTML para cambiar la estructura y disposición de elementos en las páginas del OPAC, como la página de resultados de búsqueda, la página de detalles de un ítem, etc.
#. **Reglas de circulación y préstamos**: Define reglas detalladas para los préstamos y circulación de materiales, como periodos de préstamo, límites de préstamos, renovaciones, multas, políticas de acceso, entre otros. Estas reglas se pueden adaptar a políticas institucionales y de servicio.
#. **Hojas de trabajo configurables**: Permite la personalización de campos de catalogación y definir etiquetas y subcampos específicos según los tipos de materiales que maneja la biblioteca. Esta flexibilidad es fundamental para garantizar la adecuada catalogación de los recursos y facilitar su búsqueda y recuperación.

======================
Desvenjatas
======================

#. **Soporte y mantenimiento**: Aunque existe una comunidad activa de usuarios y desarrolladores, algunos usuarios pueden enfrentar desafíos para obtener soporte técnico y mantenimiento adecuados, especialmente en comparación con sistemas comerciales que ofrecen asistencia dedicada y contratos de servicio. Además de tener que configurar en un inicio todas las tareas de mantenimiento en el servidor cóm indexación de la base de datos, etc. 
#. **Actualizaciones y compatibilidad**: Las actualizaciones de software y la compatibilidad con nuevas versiones pueden requerir tiempo y esfuerzo considerables, especialmente si se han realizado personalizaciones extensas. La transición a nuevas versiones puede presentar desafíos de integración.



======================
Enlaces útiles
======================

#. Aprenda más sobre Koha visitando el sitio web oficial: http://koha-community.org  
#. Listado de complementos actualizados para KOHA: https://gitlab.com/thekesolutions/plugins


======================
Notas
======================
.. note:: 
   Para la personalización del OPAC he utilizado el complemento Galadriel OPAC Theme Plugin diponible en https://github.com/bywatersolutions/koha-plugin-opac-theme-galadriel. Es un complemento muy sencillo que permite arreglar el estilo del OPAC de manera sencilla y rápida.

.. note:: 
   Se puede implementar las normas de catalogación RDA (Resource, Description, Access) para realizar la descripción bibliográfica.