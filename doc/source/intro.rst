.. sectionauthor:: Fernando Pacheco <fernando.pacheco@ingesur.com.uy>   

************
Introducción
************

En el año 2012 la empresa `InGeSur srl <http://www.ingesur.com.uy/>`_ desarrolla un conjunto de aplicaciones,
a través del `Proyecto InBio <http://www.inbio.org.uy/>`_, para la `Dirección General Forestal <http://www.mgap.gub.uy/>`_
(Ministerio de Ganadería, Agricultura y Pesca de Uruguay) que recolectan, gestionan y procesan la información de seguimiento de los Recursos Forestales del país.

Metodología
###########

El trabajo fue realizado en un entorno abierto y multiplataforma, es decir:

* se utilizaron herramientas libres y estándares abiertos;
* el código fuente de las aplicacioens fue entregada al cliente;
* los sistemas y aplicacioens desarrolladas pueden ejecutarse en sistemas operativos Windows (XP, Vista y 7), GNU/Linux y Mac OSX [1]_.

Herramientas
############

El desarrollo fue realizado utilizando las siguientes herramientas:

* *lenguajes de programación*: en su gran mayoría, Python (versión 2.7) [2]_, complementando con Javascript/jQuery para el desarrollo de páginas web dinámicas;
* *sistemas de gestión de bases de datos*: PostgreSQL [3]_/PostGIS [4]_ (aplicación central) y SQLite [5]_ (para aplicación personal LInFor/LIFN).
* *para desarrollo de aplicacioens web*: web2py [6]_;
* *documentación del código fuente*: docstrings/rst para código python (Sphinx [7]_ para generar salidas a HTML, PDF, etc.).

La última versión de las aplicaciones públicas pueden descargarse desde la página de la Dirección General Forestal (`aquí <http://www.mgap.gub.uy/donde>`_).

El manual de usario de las aplicaciones públicas puede consultarse en el siguiente enlace: manuales.

.. rubric:: Notas al pie
.. [1] Se optó por con utilizar GNU/Linux (Ubuntu Server 12.04) para alojar (en la Dirección General Forestal) los sistemas construidos.
.. [2] Python es un lenguaje de programación orientado a objeto ampliamente utilizado. Por mas información consulte `este <http://www.python.org/>`_  enlace.
.. [3] PostgreSQL es un sistema de gestión de bases de datos objeto-relacional que se distribuye bajo una licencia (Open Source). Por mas información consulte `este <http://www.postgresql.org/>`_  enlace.
.. [4] PostGIS es un módulo de PostgreSQL que permite gestionar datos espaciales directamente sobre el sistema de gestión de bases de datos. Esta certificado al "Simple Feature Specification" del Open Geospatial Consortium. Se distribuye bajo la licencia GPL (Versión 2). Por mas información consulte `este <http://postgis.refractions.net/>`_  enlace.
.. [5] SQLite es un sistema de gestión de bases de datos liviano ampliamente utilizado (el más utilizado en el mundo). Por mas información consulte `este <http://www.sqlite.org/>`_  enlace.
.. [6] web2py es una plataforma de desarrollo de aplicaciones web que utiliza el modelo MVC. Por mas información consulte `este <http://www.web2py.com/>`_  enlace.
.. [7] Sphinx es una herramienta para docuemtnación de proyectos informáticos (orientada a Python, pero capaz de funcionar con C,C++, etc). Por mas información consulte `Sphinx <http://sphinx.pocoo.org/>`_.

