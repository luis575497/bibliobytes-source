.. post:: Oct 25, 2023
   :tags: migración, dsapce, repositorio
   :category: Repositorios
   :author: Luis Enrique Lescano Borrego
   :exclude:

   La migración o actualización a DSpace 7 es un proceso que requiere una planificación y ejecución cuidadosa. Cada repositorio es único por lo que tiene que examinar cuidadosamente su entorno y evaluar sus capacidades para realizar este proceso de migración o actualización. A continuación, se detallo los pasos clave que considero se debes seguir en las fases en este proceso:

.. meta::
   :description: Descubre los pasos clave para llevar a cabo la migración o actualización a DSpace 7, un proceso que requiere una cuidadosa planificación y ejecución. Asegúrate de preparar tu servidor, hacer una copia de seguridad de la base de datos, migrar el backend de DSpace 7 y más. Además, conoce los requisitos y la documentación útil para una actualización exitosa.
   :keywords: DSpace 7, migración a DSpace 7, actualización de repositorio, preparación para DSpace 7, requisitos del repositorio, copia de seguridad, indexación de contenidos, actualización de software, documentación DSpace, actualización exitosa, migración de repositorios


=================================
Actualización a Dspace 7
=================================
:bdg-info-line:`Dspace` :bdg-info-line:`repositorio`

La migración o actualización a DSpace 7 es un proceso que requiere una planificación y ejecución cuidadosa. Cada repositorio es único por lo que tiene que examinar cuidadosamente su entorno y evaluar sus capacidades para realizar este proceso de migración o actualización. A continuación, se detallo los pasos clave que considero se debes seguir en las fases en este proceso:

.. warning:: 
    La migración a DSpace 7 es un proceso complejo que involucra actualizar múltiples componentes y configuraciones. Es importante realizar pruebas en un entorno de desarrollo antes de llevar a cabo la migración en producción para asegurarse de que todo funcione correctamente y minimizar el impacto en los usuarios y el contenido del repositorio. Asegúrese de seguir la documentación de DSpace y contar con la asistencia de profesionales de TI si es necesario para llevar a cabo la migración de manera exitosa.


🛠️ Fase de Preparación
-------------------------
Se deben actualizar los requsitos del servidor con la finalidad de que los softwares sean compatibles con la nueva versión a instalar 

1. **Actualizar Java:** Asegúrese de que su sistema esté utilizando la versión de Java compatible con DSpace 7. Consulte la documentación de DSpace para conocer la versión recomendada.
2. **Actualizar PostgreSQL:** Actualice su base de datos PostgreSQL a la versión requerida por DSpace 7. Consulte la documentación de DSpace para conocer la versión recomendada.
3. **Actualizar Solr:** Asegúrese de que Solr esté actualizado y configurado correctamente para DSpace 7. Solr es esencial para la búsqueda y el descubrimiento de contenido.
4. **Actualizar Apache Maven y Apache Ant:** Asegúrese de que Maven y Ant estén actualizados para facilitar la compilación y construcción de DSpace 7.
5. **Actualizar Tomcat:** Actualice su servidor Tomcat a la versión recomendada por DSpace 7. Tomcat es el contenedor web utilizado para ejecutar DSpace.

.. seealso:: 
    Para más detalles consulte la `documentación oficial de Dspace <https://wiki.lyrasis.org/display/DSDOC7x/Installing+DSpace#InstallingDSpace-BackendRequirements>`_

🚀 Fase de Migración
---------------------------------
Durante esta fase se migrará la información hacia el nuevo sistema de manera que se minimice la pérdida de datos.

1. **Hacer backup de la base de datos:** Realice una copia de seguridad completa de su base de datos PostgreSQL y de las estadísiticas proporcionadas por SOLR para garantizar que los datos estén seguros durante el proceso de migración.
2. **Compilación de Dspace**: Descargue del reopisotrio oficial la última versión estable y siga el proceso de compilación para llevar a cabo una instalación fresca..
3. **Migrar el backend DSpace 7:** Utilice el proceso de migración proporcionado por DSpace 7, que incluye el uso de FlywayDB para actualizar la estructura de la base de datos y adaptarla a la nueva versión.
4. **Actualizar la configuración del servidor del handle:** Asegúrese de que la configuración del servidor de manejo de identificadores (handle) esté actualizada y sea compatible con DSpace 7.
5. **Reindexar todos los contenidos:** Después de la migración, es esencial volver a indexar todos los contenidos en Solr para que estén disponibles en la nueva versión de DSpace.

.. seealso:: 
    Puede consultar la guía oficial ofrecida por Dspace para la migración: `Actualizando a Dspace 7 <https://wiki.lyrasis.org/display/DSDOC7x/Upgrading+DSpace>`_

✅ Requisitos del Repositorio
----------------------------------
Con la finalidad de poder emplear todas las caracterísitcas del sofware considero que los repositorios deberían cumplir con los siguientes requisitos

1. **Establecer permisos y grupos de usuarios:** Defina y establezca los permisos y grupos de usuarios en DSpace 7 según sus necesidades y políticas de acceso.
2. **Crear flujos de trabajo para colecciones:** Configure los flujos de trabajo para las colecciones que los requieran. DSpace 7 permite definir flujos de trabajo personalizados.
3. **Definir políticas de embargo y tiempos:** Establezca las políticas de embargo para los objetos y defina los plazos de acceso restringido según sus requisitos.
4. **Preparar el esquema de metadatos:** Asegúrese de que el esquema de metadatos esté configurado de acuerdo con el perfil de aplicación seleccionado (Dublin Core, OpenAire 3.0 o Driver 2.0) y se ajuste a sus necesidades de catalogación.


➡️ Documentación útil
----------------------------------

#. `Experiencias en la migración de un repositorio - ISTEC <https://submissions.istec.org/index.php/biredial-istec/article/download/183/23/623>`_
#. `Experiencias en la migración de repositorios institucionales DSpace <http://sedici.unlp.edu.ar/bitstream/handle/10915/153314/Documento_completo.pdf-PDFA.pdf?sequence=1>`_
#. `Upgrade to DSpace 7 <https://zenodo.org/records/8074863>`_
#. `Recomendaciones técnicas para la migración a Dspace 7 <https://repositorio.concytec.gob.pe/bitstream/20.500.12390/2912/1/SIRDAA2021_TimalJulian.pdf>`_
#. `Análisis de estrategias de actualización de repositorios digitales a DSpace 7 <https://revistas.um.es/analesdoc/article/view/567401>`_
#. `Desarrollo del método automático para la actualización de repositorios institucionales basados en DSpace <https://revistas.utp.ac.pa/index.php/memoutp/article/view/1843/html>`_
#. `Experiencias en la migración de un repositorio - ISTEC <https://submissions.istec.org/index.php/biredial-istec/article/download/183/23/623>`_

.. update:: 26-10-2023

    Se actualizaron y agregaron links en la Sección de **➡️ Documentación útil**