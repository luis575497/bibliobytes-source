.. post:: Nov 24, 2023
   :tags: software, open source, investigación, Gestión de la Investigación
   :category: Repositorios
   :author: Luis Enrique Lescano Borrego
   :exclude:

   DSpace-CRIS representa una extensión evolutiva de DSpace, un sistema de repositorio de código abierto que encuentra su principal aplicación en el ámbito académico y de investigación. Este sistema se dedica a almacenar, gestionar y brindar acceso a una amplia gama de recursos digitales, tales como artículos científicos ...

.. meta::
   :description: DSpace CRIS, software, open source, Gestión de la Investigación
   :keywords: DSpace-CRIS representa una extensión evolutiva de DSpace, un sistema de repositorio de código abierto dedicado al almacenamiento, gestión y acceso a recursos digitales en el ámbito académico y de investigación


*************
DSpace CRIS
*************
:bdg-info-line:`software` :bdg-info-line:`open source` :bdg-info-line:`Gestión de la Investigación`

.. admonition:: Dspace CRIS Logo
    :class: sidebar tip

    .. image:: ../_static/images/dspace-cris.png
       :align: center
       :height: 200
       :width: 200

    *Imagen tomada del sitio web oficial*


DSpace-CRIS representa una extensión evolutiva de DSpace, un sistema de repositorio de código abierto que encuentra su principal aplicación en el ámbito académico y de investigación. Este sistema se dedica a almacenar, gestionar y brindar acceso a una amplia gama de recursos digitales, tales como artículos científicos, tesis, documentos y conjuntos de datos. Se originó en el año 2009 bajo el auspicio de la empresa 4Science y ha experimentado una serie de actualizaciones y modificaciones hasta alcanzar su versión actual, la 7.

La esencia de la extensión DSpace-CRIS, abreviatura de Current Research Information System, radica en su capacidad para expandir y potenciar las funcionalidades originales de DSpace, orientándose hacia la gestión y exposición de datos vinculados con la actividad investigativa en instituciones académicas. Diseñado de manera específica para la administración de información relacionada con la investigación, DSpace-CRIS facilita la integración de datos provenientes de diversas fuentes. Esto permite una gestión más eficiente de detalles concernientes a proyectos de investigación, publicaciones, autores, financiamiento, patentes y otros elementos clave dentro del ámbito de la investigación académica.

.. admonition:: Datos técnicos  
   :class: important

   | **Año de creación**: 2009 
   | **OAI**: Soporta el protocolo OAI-PMH
   | **Integraciones**: ORCID, Scopus, WOS, Dimensions, Google Shoolar, Crossref, Pubmed
   | **URL**: https://github.com/4Science/DSpace
 
======================
✨ Caracterísitcas
======================

Las principales funciones y características de DSpace CRIS desde su versión 7 incluyen:

#. **Gestión de Entidades CRIS:** DSpace-CRIS proporciona una gestión completa de entidades fundamentales en la investigación. Esto abarca la habilidad de crear y administrar entidades preconfiguradas, ajustando sus propiedades y características para adaptarlas exactamente a las necesidades específicas de cada contexto. Desde investigadores, publicaciones, proyectos y unidades organizativas, esta funcionalidad permite una personalización detallada para asegurar una representación completa y precisa de la actividad investigativa.

#. **Vínculos entre Entidades:** La plataforma facilita la creación de relaciones significativas entre diversas entidades. Esto posibilita una visión conectada y comprehensiva de la red de información investigativa. Al establecer vínculos entre una o más entidades, se logra una comprensión más profunda y contextualizada de cómo interactúan investigadores, proyectos, publicaciones y otras unidades dentro del ecosistema de investigación.

#. **Componentes Dinámicos Contextualizados:** DSpace-CRIS ofrece una experiencia de navegación optimizada con índices de navegación personalizables para las entidades específicas de DSpace. Cada entidad cuenta con una página de detalle organizada en pestañas y secciones, brindando un acceso claro y estructurado a la información detallada y relevante de cada elemento.

#. **Evaluación, Informes y Análisis:** La plataforma proporciona herramientas poderosas para la evaluación y análisis de datos a diferentes niveles de la jerarquía, desde estadísticas globales del repositorio hasta métricas detalladas de entidades individuales. Esto incluye visualizaciones de descargas y vistas, recuentos de citas, análisis geográficos y alertas automatizadas, ofreciendo una perspectiva completa de la actividad investigativa.

#. **Gestión y Promoción de Perfiles:** DSpace-CRIS facilita la gestión y promoción de perfiles de investigadores. Desde la creación y gestión de CVs de investigadores hasta la posibilidad de mostrar u ocultar elementos específicos manualmente, la plataforma ofrece herramientas para mantener perfiles precisos y actualizados. Además, la funcionalidad de red de colaboración fomenta la interacción entre investigadores, fortaleciendo la colaboración y la sinergia en el ámbito académico y científico.

.. admonition:: Prueba DSpace CRIS
   :class: tip

   Si deseas probarlo puedes acceder a este servidor de prueba proporcinado por la empresa **4Science**:
   
   - https://dspacecris7.4science.cloud/home

======================
📉 Desvenjatas
======================

#. **Configuración compleja:** La configuración inicial de DSpace-CRIS puede presentar complicaciones al requerir la adaptación de la plataforma según las necesidades específicas de la institución. Este proceso implica la personalización de entidades, flujos de trabajo y ajustes técnicos, lo que puede ser desafiante, especialmente para usuarios menos familiarizados con la plataforma. Además, la creación y configuración de nuevas entidades demandan un conocimiento básico del desarrollo de ontologías RDF.

#. **Requerimientos de recursos:** Implementar y mantener DSpace-CRIS requiere una inversión sustancial en términos de recursos. Esto abarca la necesidad de hardware adecuado para albergar el sistema, recomendándose servidores independientes para el backend, frontend, SOLR y la base de datos. Además, se requiere personal capacitado para su administración, configuración y brindar soporte continuo. La falta de recursos apropiados puede obstaculizar el rendimiento óptimo del sistema.

#. **Actualizaciones y mantenimiento continuo:** Mantener DSpace-CRIS actualizado y en pleno funcionamiento puede requerir esfuerzos constantes. Las actualizaciones regulares para mejorar la plataforma pueden afectar la estabilidad o la compatibilidad con personalizaciones existentes, lo que requiere ajustes técnicos y puede generar interrupciones temporales en el servicio si no se administran adecuadamente.

.. admonition:: Consideraciones
    :class: danger
        
    La implementación de este sistema se recomienda únicamente para instituciones dedicadas a la investigación o universidades que busquen presentar sus resultados de investigación de manera más atractiva y efectiva.

======================
🔗 Enlaces útiles
======================

#. Documentación oficial: https://wiki.lyrasis.org/display/DSPACECRIS/DSpace-CRIS+Home
#. Instalación de Dspace CRIS: https://wiki.lyrasis.org/display/DSPACECRIS/Installation

======================
📝 Notas
======================

.. note:: 
   Se pueden realizar integraciones con la API de ORCID para acceder a diversas funcionalidades. Estas incluyen la autenticación de usuarios, la recopilación de datos del perfil del autor de ORCID y, en caso de tener una membresía, la capacidad de actualizar información biográfica y publicaciones directamente desde DSpace.

.. note:: 
   Desde la configuración de DSpace CRIS, es posible configurar integraciones en cualquier momento para recuperar datos bibliométricos, como el recuento de citas, desde PubMed, Scopus, Web of Science (WOS) y Almetrics.

======================
➡️ Posts Relacionados
======================

* :doc:`Dspace 7 </posts/dspace>`
* :doc:`Actualización a Dspace 7 </posts/dspace7-migrations>`




