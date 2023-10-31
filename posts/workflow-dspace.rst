.. post:: Oct 30, 2023
   :tags: repositorios, Dspace, trabajo
   :category: Repositorios
   :author: Luis Enrique Lescano Borrego
   :exclude:

   En la rutina diaria, bibliotecarios y gestores de repositorios se enfrentan a un constante flujo de solicitudes de publicación en sus repositorios, lo cual puede complicar y ralentizar significativamente su trabajo. Por tanto, la eficaz gestión de contenido se convierte en una estrategia esencial para agilizar los procesos de publicación en colecciones digitales.

.. meta::
   :keywords: DSpace 7, flujos de trabajo, gestión de colecciones digitales, organización, control de calidad, coordinación, grupos de usuarios, permisos, planificación, roles.
   :description: Aprende a crear flujos de trabajo efectivos en DSpace 7 para una gestión eficiente de colecciones digitales. Organiza, controla la calidad y coordina las actividades de remitentes, revisores y editores. Descubre cómo implementarlos y mejora tu experiencia en la colección digital.
   :author: Luis Enrique Lescano Borrego


*******************************************************
Creación de flujos de trabajo efectivos en Dspace 7
*******************************************************

En la rutina diaria, bibliotecarios y gestores de repositorios se enfrentan a un constante flujo de solicitudes de publicación en sus repositorios, lo cual puede complicar y ralentizar significativamente su trabajo. Por tanto, la eficaz gestión de contenido se convierte en una estrategia esencial para agilizar los procesos de publicación en colecciones digitales. En este contexto, DSpace 7, una plataforma de código abierto ampliamente aclamada para la gestión de repositorios digitales, ha introducido una característica crucial en su versión 7: los *flujos de trabajo (workflows)*. Estos flujos de trabajo permiten definir cómo se ingresa, revisa y edita la información en una colección, involucrando a remitentes, revisores y editores. A través de este post, examinaremos la importancia de los flujos de trabajo y cómo implementarlos eficazmente.

📌 Importancia de los Flujos de Trabajo en DSpace 7
========================================================
Los flujos de trabajo en DSpace 7 desempeñan un papel fundamental en la gestión de contenido. Establecer un flujo de trabajo adecuado proporciona numerosos beneficios:

* **Organización y Estructura**: Contribuyen a establecer una definición clara de los procesos de ingreso y revisión de contenido en la colección, lo que resulta en la creación de una estructura organizada. Esto garantiza que todos los recursos sean sometidos a una revisión y edición adecuadas antes de su publicación, involucrando a todas las dependencias que intervienen en el proceso.
* **Control de Calidad:** Permiten establecer puntos de control que garantizan la calidad del contenido. Esto posibilita que los revisores puedan identificar errores o problemas antes de que los recursos estén disponibles para el público, elevando, de este modo, los estándares de calidad.
* **Coordinación Eficiente:** Facilitan una colaboración fluida entre los distintos roles, incluyendo remitentes, revisores y editores. Cada parte puede desempeñar su función de manera más eficaz, con un claro entendimiento de cuándo y cómo deben intervenir.
* **Seguridad de Acceso:**  La definición de roles y permisos asegura que solo las personas autorizadas tengan la capacidad de agregar, revisar o editar contenido, protegiendo así la integridad de la colección.

🛠️ Creación de Flujos de Trabajo en DSpace 7
==============================================

.. blockdiag::
   :caption: Diagrama de flujo de trabajo en una colección de Dspace
   :desctable:

   blockdiag {
      Remitente -> Revisor -> Editor -> Publicación ;
   }

A continuación, se describen los pasos para crear flujos de trabajo efectivos en DSpace 7:

#. **Identificar Roles y Responsabilidades:** El primer paso consiste en identificar a las personas involucradas en la publicación de un documento en la colección, así como definir sus roles, como remitentes, revisores y editores. Cada uno de estos roles desempeña responsabilidades específicas en el proceso de gestión de contenido y es una parte integral del proceso de publicación.

#. **Crear Grupos de Usuarios:** Para facilitar la asignación de permisos, es recomendable crear grupos de usuarios para cada uno de los roles identificados. Por ejemplo, puede establecer un grupo global denominado "Bibliotecarios del Campus de Medicina" (editores) y otro grupo denominado "Analistas de Facultad" (revisores). Posteriormente, incluya a los usuarios en estos grupos de acuerdo a sus respectivas responsabilidades.

   .. dropdown:: Crear un grupo en Dspace 7
      :color: secondary
      :icon: light-bulb
   
      .. figure:: ../_static/images/grupos-dspace.png
          :width: 600
          :align: center

          Selecciona la opción **"Control de Acceso >> Grupos"** y crea o edita un grupo existente.
    
      .. figure:: ../_static/images/usuarios-dspace.png
          :width: 600
          :align: center

          Dentro del grupo creado se puede añadir usuario u otro subgrupos


#. **Definir etapas y establecer permisos:** En DSpace 7, puede definir las etapas del flujo de trabajo, como "Enviado", "Revisión" y "Edición". Cada etapa puede tener asignada una duración máxima, lo que ayuda a controlar el tiempo que un recurso pasa en cada etapa. Utilice los grupos de usuarios creados en el paso 2 para establecer permisos en cada etapa del flujo de trabajo. Esto determina quién puede acceder y realizar acciones en cada etapa. Por ejemplo, los revisores solo pueden acceder a la etapa de revisión.

   .. dropdown:: Crear Roles en comunidades
      :color: secondary
      :icon: light-bulb
   
      .. figure:: ../_static/images/roles-colecciones.png
          :width: 600
          :align: center

          Cuando edites una colecciones selecciona el apartado de **Asignar Roles** y crea los grupos necesarios, una vez creados asignales los subgrupos de usuarios que corresponden a los permisos otorgados

Una vez hayas completado los pasos anteriores, habrás configurado un flujo de trabajo para la colección deseada. De esta manera, tus usuarios solo tendrán que acceder a DSpace y verificar en la sección **Mi DSpace** si tienen tareas pendientes en el flujo de trabajo *(workflow)*.

.. seealso:: 

    Si deseas aprender a realizar aún más tareas en DSpace y aprovechar al máximo esta potente plataforma, te invitamos a explorar nuestro :doc:`curso disponible </cursos/dspace>` . En él, encontrarás una guía completa para dominar las funcionalidades de DSpace 


📝 Conclusión
==============================================

Los flujos de trabajo en DSpace 7 se destacan como una herramienta esencial para lograr una gestión eficiente de las colecciones digitales. Su utilidad radica en la capacidad de organizar, controlar la calidad y coordinar las actividades de remitentes, revisores y editores. La creación de grupos de usuarios y la configuración de permisos aseguran un proceso fluido y seguro. La implementación de flujos de trabajo bien diseñados en DSpace 7 conlleva una mejora significativa en la gestión de contenido y, en última instancia, enriquece la experiencia de los usuarios que acceden a la colección digital. Este enfoque resalta la importancia de que las bibliotecas y encargados de repositorios establezcan una planificación y un control de roles adecuados para optimizar el funcionamiento de los flujos de trabajo.


======================
➡️ Posts Relacionados
======================

* :doc:`Actualización a Dspace 7 </posts/dspace7-migrations>`
* :doc:`Dspace </posts/dspace>`