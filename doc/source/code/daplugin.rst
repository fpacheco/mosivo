*********************************
Plugin de acceso a datos remotos
*********************************
 
El módulo de acceso a datos permite que la información requerida por el
modelo sea obtenida desde fuentes externas a la aplicación.
Estas fuentes pueden ser de cualquier tipo:
 * base de datos remotas;
 * Web Services;
 * planilla de cálculo;
 * etc.

En cada caso, se deberán crear nuevos módulos que obtengan esa información
y los devuelvan en el formato requerido para que puedan ser insertados en
la base de datos del modelo.

En la documentación de la clase IPlugin se declaran los formatos y nombres
de cada uno de ellos.

El diagrama de clases del módulo es el siguiente:

.. inheritance-diagram:: modules.daplugin.ipluginbase modules.daplugin.iplugin modules.daplugin.pluginmanager
    :parts: 3

La documentación de las clases involucradas se presenta a continuación.

:mod:`daplugin` Package
-----------------------

.. automodule:: modules.daplugin.__init__
    :members:
    :undoc-members:
    :show-inheritance:

:mod:`iplugin` Module
---------------------

.. automodule:: modules.daplugin.iplugin
    :members:
    :undoc-members:
    :show-inheritance:

:mod:`ipluginbase` Module
-------------------------

.. automodule:: modules.daplugin.ipluginbase
    :members:
    :undoc-members:
    :show-inheritance:

:mod:`pluginmanager` Module
---------------------------

.. automodule:: modules.daplugin.pluginmanager
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`remotedata` Module
---------------------------

.. automodule:: modules.daplugin.remotedata
    :members:
    :undoc-members:
    :show-inheritance:
