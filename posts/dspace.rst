.. post:: Oct 20, 2023
   :tags: software, open source, repositorio
   :category: Repositorios
   :author: Luis Enrique Lescano Borrego
   :exclude:

   DSpace es un sistema de gestión de repositorios de código abierto diseñado para ayudar a las instituciones, como universidades y bibliotecas, a crear, mantener y gestionar repositorios digitales de contenido académico, científico, cultural y otros tipos de información. DSpace proporciona una plataforma para almacenar, organizar, preservar y proporcionar ...

.. meta::
   :description: DSpace - Sistema de Gestión de Repositorios de Código Abierto y Académicos
   :keywords: DSpace, gestión de repositorios, código abierto, plataforma de repositorio, software bibliotecario, plataforma de código abierto, gestión de contenido digital


**********
DSpace
**********
:bdg-info-line:`software` :bdg-info-line:`open source` :bdg-info-line:`repositorio`

.. admonition:: Dspace Software Logo
    :class: sidebar tip

    .. image:: ../_static/images/dspace.jpg
       :align: center
       :height: 200
       :width: 200

    *Imagen tomada del sitio web oficial*


DSpace es un sistema de gestión de repositorios de código abierto diseñado para ayudar a las instituciones, como universidades y bibliotecas, a crear, mantener y gestionar repositorios digitales de contenido académico, científico, cultural y otros tipos de información. DSpace proporciona una plataforma para almacenar, organizar, preservar y proporcionar acceso a una variedad de materiales digitales, como tesis, artículos de investigación, imágenes, documentos históricos, videos y otros recursos digitales.

En la actualidad, el software ha avanzado a la versión 7.x, lo que representó un significativo cambio en la arquitectura. En este proceso, se produjo una separación entre el backend y el frontend, además de la disociación del servidor de búsquedas SOLR del backend. Como base de datos, ahora se emplea únicamente PostgreSQL.

.. admonition:: Datos técnicos  
   :class: important

   | **Año de creación**: 2002. 
   | **OAI**: Soporta el protocolo OAI-PMH
   | **ORCID**: Se integra con el API de ORCID para la recolección de datos de autores.
   | **URL**: https://dspace.lyrasis.org/download/
 
======================
✨ Caracterísitcas
======================

Las principales funciones y características de DSpace desde su versión 7.x incluyen:

#. **Formulario de envío simplificado**: En esta versión se ha simplificado el proceso de carga de contenido en el repositorio. Con un formulario de envío simplificado, los usuarios pueden cargar sus materiales de una manera más intuitiva y fácil, lo que mejora la experiencia de los contribuyentes y fomenta la contribución de contenido al repositorio.
#. **Entidades configurables**: En la versión 7.x de DSpace, se ha incorporado la notable función de personalización de entidades. Esta capacidad permite a las instituciones adaptar el sistema a sus necesidades específicas. En otras palabras, las instituciones ahora pueden definir y ajustar los tipos de elementos que desean gestionar, como individuos, publicaciones, proyectos y departamentos, y establecer relaciones significativas entre ellos. Este enfoque de personalización ampliada se alinea con los principios de la web semántica, permitiendo una representación más rica y contextual de la información en el repositorio.
#. **Gestión de flujos de trabajo**: DSpace 7.x ofrece una gestión de flujos de trabajo mejorada, lo que significa que las instituciones pueden diseñar, personalizar y automatizar los procesos de revisión y aprobación para el contenido que se envía al repositorio. Esto es especialmente útil para garantizar la calidad y la coherencia de los materiales antes de su publicación.
#. **Tareas de curación**: Esta característica se refiere a la capacidad de DSpace para ayudar en la curación y preservación de los contenidos digitales. Las tareas de curación incluyen la combrobación de integridad, comprobación de metadatos requeridos, comprobación de formatos de archivo y otras actividades destinadas a mantener la integridad y utilidad del contenido a lo largo del tiempo.
#. **Control de versiones**: DSpace 7.x permite un control de versiones para los documentos almacenados en el repositorio. Esto es útil para llevar un registro de las actualizaciones y cambios en los documentos a lo largo del tiempo, lo que es importante en la gestión de contenido académico y científico.
#. **Embargo**: La característica de embargo permite a los administradores del repositorio restringir el acceso a ciertos contenidos durante un período específico. Esto es útil para cumplir con políticas editoriales, acuerdos de publicación y requisitos legales antes de que el contenido se haga completamente público. Después del período de embargo, el contenido se vuelve accesible al público.

.. admonition:: Prueba DSpace 
   :class: tip

   Si deseas probarlo puedes acceder a este servidor de prueba proporcinado por Dspace:

   - **Versión 7.x**: https://demo.dspace.org/home  
   - **Versión 6.x**: https://demo6.dspace.org/

======================
📉 Desvenjatas
======================

#. **Configuración**:  La configuración de módulos y formularios de envío requiere la edición de archivos en el servidor, lo que implica la necesidad de acceso directo al servidor y conocimientos avanzados del sistema para llevar a cabo esta tarea.
#. **URL largas**: En la versión 7.x, las URL creadas para los elementos, colecciones y comunidades se basan en UUID, lo que resulta en direcciones web considerablemente largas y menos legibles en comparación con los handles utilizados en versiones anteriores.
#. **Búsquedas lentas**: En la versión 7.x, se ha observado una disminución en la velocidad de las búsquedas en la plataforma. Por lo tanto, se recomienda contar con un servidor para el frontend que cumpla con las siguientes especificaciones: 8 núcleos de CPU y 32 GB de RAM. Además, es aconsejable configurar Node.js para admitir el procesamiento en múltiples hilos (multi-threading).

.. admonition:: Solventar error 505
    :class: danger
        
    En la versión 7.x, cuando se encuentra un error 505, en la mayoría de los casos, esto se debe a problemas de comunicación entre el backend y el frontend. Para abordar esta situación, es fundamental revisar la configuración del archivo del frontend y asegurarse de que el archivo dspace/config/dspace.cfg contenga las URL del servidor e interfaz de usuario correctamente definidas. 

======================
🔗 Enlaces útiles
======================

#. Documentación oficial: https://wiki.lyrasis.org/display/DSDOC7x
#. Instalación de Dspace 7.x: https://subratiitk.wordpress.com/install-dspace-7-2-on-ubuntu-22-04-lts/

======================
📝 Notas
======================

.. note:: 
   Es posible llevar a cabo integraciones con la API de ORCID para lograr diversas funcionalidades. Entre ellas se incluye la autenticación de usuarios, la recolección de datos del perfil del autor de ORCID y, si se cuenta con una membresía, la actualización de información biográfica y publicaciones desde DSpace.

.. note:: 
   Se permite la utilización de vocabularios controlados para los campos en el formulario de envío en DSpace, lo que habilita la implementación de taxonomías para una organización más efectiva del contenido. Para llevar a cabo esta tarea, es posible emplear software especializado como `TemaTres <https://vocabularyserver.com/web/>`_. Los vocabularios controlados y taxonomías resultan particularmente útiles para estructurar y categorizar los materiales en el repositorio, lo que a su vez mejora la búsqueda, la navegación y la recuperación de información para los usuarios.


======================
➡️ Posts Relacionados
======================

* :doc:`Actualización a Dspace 7 </posts/dspace7-migrations>`




