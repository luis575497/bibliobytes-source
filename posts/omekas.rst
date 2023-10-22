.. post:: Oct 13, 2023
   :tags: software, open source, repositorio
   :category: Repositorios
   :author: Luis Enrique Lescano Borrego
   :exclude:

   Omeka S (Semantic) es un sistema de gestión de contenidos de software libre diseñado para satisfacer las necesidades de diversas instituciones culturales, tales como bibliotecas, archivos, museos y universidades, permitiéndoles desarrollar una amplia gama de proyectos digitales...

**********
Omeka-S
**********
:bdg-info-line:`software` :bdg-info-line:`open source` :bdg-info-line:`repositorio`

.. admonition:: Omeka-S Software Logo
    :class: sidebar tip

    .. image:: ../_static/images/omekas.jpg
       :align: center
       :height: 200
       :width: 200

    *Imagen tomada del sitio web oficial*

Omeka S (Semantic) es un sistema de gestión de contenidos de software libre diseñado para satisfacer las necesidades de diversas instituciones culturales, tales como bibliotecas, archivos, museos y universidades, permitiéndoles desarrollar una amplia gama de proyectos digitales. 
Este proyecto es impulsado por la Corporation for Digital Scholarship del Roy Rosenzweig Center de la George Mason University, reconocida por su trayectoria en proyectos destacados en el ámbito digital, como Omeka Classic o el reconocido sistema de gestión de referencias bibliográficas Zotero, entre otros. Con Omeka S, se busca ofrecer una plataforma versátil y poderosa que propicie la creación, organización y presentación efectiva de recursos digitales de manera accesible y estructurada.

.. admonition:: Datos técnicos  
   :class: important

   | **Año de creación**: 2012. 
   | **OAI**: Soporta el protocolo OAI-PMH
   | **URL**: https://omeka.org/s/download/
 
======================
✨ Caracterísitcas
======================

Las características y funcionalidades clave de Omeka S incluyen:

#. **Relaciones**: Permite crear relaciones entre elementos, conjuntos de elementos y medios para organizar y estructurar recursos en el repositorio.
#. **Recursos compartidos**: Facilita compartir eficientemente recursos entre diferentes sitios y usuarios, fomentando la colaboración e intercambio de información.
#. **Metadatos**: Ofrece la elección entre tres vocabularios de metadatos y la posibilidad de agregar vocabularios adicionales según las necesidades del proyecto.
#. **Plantillas personalizadas**: Permite crear plantillas de contenido personalizadas, extrayendo de varios vocabularios de metadatos y compartiéndolas en la web.
#. **Personalización**: Proporciona temas listos para dispositivos móviles para personalizar la apariencia de cada sitio, asegurando una experiencia óptima en diferentes dispositivos.
#. **Sitios**:Facilita la creación de sitios para publicar y contextualizar elementos, exhibiciones o historias digitales, brindando flexibilidad en la presentación de contenidos.
#. **Configuración de sitios**:Permite la gestión de configuraciones específicas para adaptarse a las necesidades de cada sitio, con control detallado sobre la apariencia y comportamiento.
#. **Módulos**: Facilita la extensión del sitio mediante módulos que amplían las funcionalidades y posibilidades de la plataforma para adaptarse a requisitos específicos. 
#. **Actualización**: Facilita la actualización de múltiples sitios desde una sola instalación, garantizando una gestión eficiente y actualizada del contenido y funcionalidades.
#. **Interoperatividad**: Facilita la conexión con repositorios externos como Fedora y DSpace para la actualización periódica del contenido desde estos repositorios.

.. admonition:: Prueba Omeka S  
   :class: tip

   Si deseas probarlo puedes acceder a este servidor de prueba proporcinado por Omeka: http://dev.omeka.org/omeka-s-sandbox/login  

   - usuario: omekasdemo1@example.com  
   - password: omekasdemo1  

======================
📉 Desvenjatas
======================

#. **Módulos**: Al tener numerosos módulos, la instalación de estos puede volverse complicada, ya que en algunos casos es necesario descargar y compilar sus dependencias. Si no se realiza este proceso correctamente, puede ocasionar un error 503 en el servidor.
#. **Personalización limitada**: Aunque Omeka S ofrece opciones de personalización, los usuarios menos técnicos pueden encontrar limitaciones en la personalización avanzada de la apariencia y funcionalidades sin conocimientos de programación, por lo que para poder personalizar un tema son necesarios conocimientos de SASS, CSS, HTML y PHP

.. admonition:: Solventar error 503
    :class: danger
        
    Si se encuentra con un error 503 al instalar un módulo, simplemente debe eliminar la carpeta correspondiente al módulo dentro de la carpeta modules en el directorio de Omeka y eliminar su entrada en la sección de módulos de la base de datos.

======================
🔗 Enlaces útiles
======================
git 
#. Listado de módulos actualizados de Omeka S: https://daniel-km.github.io/UpgradeToOmekaS/omeka_s_modules.html
#. Listado de temas para Omeka S: https://daniel-km.github.io/UpgradeToOmekaS/omeka_s_themes.html


======================
📝 Notas
======================
.. note:: 
   Las capacidades de Omeka S se pueden aumentar con el uso de módulos, se recomienda usar los módulos oficiales y los creados por  https://gitlab.com/Daniel-KM, pues son muy estables y no tienen conflictos.

.. note:: 
   Recomiendo los siguientes módulos para transformar Omeka S en una biblioteca Digital:

   #. https://github.com/omeka/omeka-s-enduser/edit/master/docs/modules/customvocab.md
   #. https://gitlab.com/Daniel-KM/Omeka-S-module-Guest
   #. https://gitlab.com/Daniel-KM/Omeka-S-module-IiifServer
   #. https://github.com/biblibre/omeka-s-module-Ldap
   #. https://gitlab.com/Daniel-KM/Omeka-S-module-Mirador
   #. https://gitlab.com/Daniel-KM/Omeka-S-module-OaiPmhRepository
   #. https://github.com/ManOnDaMoon/omeka-s-module-RestrictedSites
   #. https://gitlab.com/Daniel-KM/Omeka-S-module-SearchHistory
   #. https://gitlab.com/Daniel-KM/Omeka-s-module-Selection
   #. https://gitlab.com/Daniel-KM/Omeka-S-module-UniversalViewer
   #. https://gitlab.com/Daniel-KM/Omeka-S-module-AdvancedSearchPlus