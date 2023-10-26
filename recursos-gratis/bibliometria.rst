=====================
📊 Bibliometría
=====================
La bibliometría es una disciplina que se dedica a medir y analizar la producción, difusión y uso de la información científica y académica, permitiendo cuantificar la actividad científica, evaluar la calidad de la investigación, analizar la difusión de la misma y medir su impacto a través de métodos estadísticos y matemáticos, siendo fundamental en la evaluación de investigadores, instituciones y la toma de decisiones académicas y políticas de investigación.


🖥️ Softwares
=====================

Publish or Perish
-------------------------
Publish or Perish es una herramienta ampliamente utilizada para analizar la producción académica y el impacto de los investigadores. Esta herramienta se basa en datos obtenidos de diversas fuentes, como Google Scholar, Scopus, Web of Science, OpenAlex, Crossref, entre otras, y proporciona métricas bibliométricas, como el índice H, el número de citas y otros indicadores clave. Los usuarios pueden buscar y analizar la literatura científica, identificar tendencias en la investigación y evaluar la influencia de autores, revistas y documentos específicos. La información resultante se puede exportar a un documento CSV, Excel o a formtatos de gestores bibliográficos (RIS).

**Descarga:** https://harzing.com/resources/publish-or-perish

VOSviewer
-------------------------
VOSviewer es un software de visualización bibliométrica que habilita a los investigadores a representar gráficamente redes de colaboración, co-citación y co-palabras clave a partir de datos bibliográficos. Esta herramienta simplifica la identificación de relaciones entre autores, instituciones y temas de investigación. VOSviewer emplea técnicas de análisis de datos y visualización para crear mapas que facilitan la comprensión de la estructura y la dinámica de un campo de investigación. Para instalarlo, es necesario contar con el entorno virtual de Java previamente configurado

**Descarga:** https://www.vosviewer.com/download

Bibliometrix
-------------------------
Bibliometrix es una extensión de R, un lenguaje de programación estadística, que se utiliza para llevar a cabo análisis bibliométricos y evaluaciones de la producción científica. Permite a los usuarios importar y procesar datos bibliográficos desde archivos exportados de Scopus, Web of Science, PubMed, entre otros, así como conectarse a varias APIs. Con esta herramienta, es posible calcular métricas bibliométricas, crear gráficos y generar informes detallados. Bibliometrix muestra y representa gráficamente las relaciones de co-citación, mapas temáticos, autores y documentos más relevantes, además de las redes de colaboración, etc. Esta herramienta resulta especialmente útil para investigadores y bibliotecarios que buscan realizar análisis bibliométricos personalizados.

**Descarga:** https://www.bibliometrix.org/home/

.. seealso:: 
    Para poder ejecutar este software tiene que descargar e instalar `R <https://www.r-project.org/>`_ y `RStudio <https://www.bibliometrix.org/home/index.php/download>`_

CiteSpace
-------------------------
CiteSpace es un software diseñado específicamente para analizar y visualizar la evolución de campos de investigación a lo largo del tiempo. Utiliza datos de citas y co-citaciones para identificar patrones emergentes en la literatura científica. CiteSpace crea mapas y gráficos que muestran las tendencias, los hitos y las áreas de concentración en una determinada disciplina. Es útil para investigadores interesados en el desarrollo de un campo de estudio. Dispone de la versión básica gratuita y varias opciones de pago.

**Descarga:** https://citespace.podia.com/download

BibExcel
-------------------------
BibExcel es una herramienta que se utiliza principalmente para analizar y visualizar datos bibliométricos a partir de hojas de cálculo de Excel. Permite realizar análisis de co-ocurrencia de palabras clave, generar gráficos de red y calcular diversas métricas bibliométricas básicas. Aunque es menos sofisticado que otros software bibliométricos, es fácil de usar y adecuado para aquellos que desean realizar análisis bibliométricos de manera sencilla.

**Descarga:** https://homepage.univie.ac.at/juan.gorraiz/bibexcel/

.. warning:: 
    Este software no se actualiza desde 2017 y carece de una interfaz moderna y amigable

🔍 Fuentes de Datos
=====================

Scopus y Web of Science
-------------------------
`Scopus <https://www.scopus.com/search/form.uri?display=basic>`_ y `Web of Science <https://www.webofscience.com/wos>`_ son bases de datos bibliográficas académicas que incluyen una amplia variedad de publicaciones científicas, revistas y conferencias. Proporcionan información detallada sobre artículos, autores, citas y afiliaciones. Son fuentes confiables para la realización de análisis bibliométricos, ya que ofrecen datos precisos y actualizados.

Dimensions
-------------------------
`Dimensions <https://www.dimensions.ai/>`_ es una plataforma de datos de investigación que combina información bibliográfica, financiamiento de investigación y métricas de impacto. Ofrece una amplia gama de datos para el análisis bibliométrico, incluyendo información sobre publicaciones, autores, financiamiento y colaboraciones de investigación. Dimensions también proporciona una API pagada para acceder a sus datos, permitiendo a los investigadores y desarrolladores extraer información específica de manera programática.


🔄 API para la extracción de datos
====================================

Crossref API
-------------------------
La API de Crossref brinda acceso a una extensa colección de datos bibliográficos, incluyendo metadatos de artículos, citas y DOIs. Tanto investigadores como desarrolladores pueden aprovechar esta API de forma gratuita para extraer información específica de la literatura académica. Los siguientes enlaces te llevarán a la documentación y a las últimas actualizaciones de la AP

**API:** https://api.production.crossref.org/swagger-ui/index.html


PubMed API
-------------------------
La API de PubMed, mantenida por la Biblioteca Nacional de Medicina de los Estados Unidos, proporciona acceso a una amplia colección de literatura científica en el campo de la medicina y ciencias afines. Permite la búsqueda y extracción de información detallada sobre artículos, autores y temas médicos.

**API:** https://www.ncbi.nlm.nih.gov/home/develop/api/


JSTOR Data
-------------------------
JSTOR ofrece soporte para minería de texto, lo que permite a los investigadores acceder a contenido textual de su extensa colección de revistas académicas y libros. Esto es valioso para la investigación bibliométrica que involucra análisis de contenido textual. La plataforma JSTOR Data proporciona acceso a estos recursos para la extracción y análisis de datos.  

**API:** https://about.jstor.org/whats-in-jstor/text-mining-support/


OpenAlex API
-------------------------
El API de OpenAlex es una valiosa fuente de datos que proporciona información sobre la accesibilidad abierta de la literatura científica. Ofrece detalles sobre si un artículo científico está disponible en acceso abierto, así como datos relacionados con instituciones, autores, publicaciones y más. Esta información resulta fundamental para analizar la disponibilidad y accesibilidad de la investigación, permitiendo una evaluación más completa de la disponibilidad de recursos académicos y fomentando la promoción del acceso abierto a la literatura científica

**API:** https://docs.openalex.org/
