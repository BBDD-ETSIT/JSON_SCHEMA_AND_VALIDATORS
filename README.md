# JSON_SCHEMA_JS_VALIDATOR

Instrucciones de instalación de cada alternativa:
1. Este repositorio se puede descargar como un zip (con el desplegable que se abre al hacer click en el botón verde "code") y en él vendrán todos los ficheros incluidos.
1.b Alternativamente se puede descargar usando git (en ese caso el paso 2 lo podemos saltar)
2. Descomprimir dicho zip en una carpeta de trabajo
3. Abrir una consola interactiva (un terminal) y hacer cd al directorio donde hemos descomprimido el zip o donde hemos descargado con git. Por ejemplo cd c:/users/enrique/bbdd/jsonschema
4. Comprobar que estoy en el directorio correcto con el comando "ls" o "dir" que están ahí los ficheros y directorios de los ejemplos.


Node - JS:

0. Necesito tener node 16 o 18 instalado en la máquina.
1. Ejecutar "cd js_validator". En dicho directorio (comprobarlo con "dir") deben estar todos los ficheros descomprimidos, incluido el fichero package.json
2. Ejecutar el programa "npm install" que instalará el software necesario para poder validar nuestros JSON Schemas
3. Vamos a probar el programa, para ello ejecutamos el comando "node validator.js" que debería devolver un log diciendo que nuestro JSON es correcto.
4. Ya podemos editar tanto el fichero catalogo.json como catalogo.schema.json con el contenido que queramos o modificar validator.js para que tome otro schema y otro json
5. happy coding




Python:

0. Necesito tener python instalado (preferiblemente actualizado, versión >3) 
1. Ejecutar pip install jsonschema
2. py validator.py
3. happy coding

