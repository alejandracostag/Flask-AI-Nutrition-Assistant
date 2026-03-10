# Ejemplo con PYTHON FLASK e integración de LLM mediante el API de GROQ


## 1. Objetivo

- Aprender una integración sencilla de un LLM en una aplicación web

## 2. Descripción
La aplicación web es un sistema de recomendación de libros con la siguiente interfaz de usuario:
- ![image](https://github.com/user-attachments/assets/04e4bf67-fa14-4fc1-ae83-f0990f6aba6e)

El usuario selecciona "Género Literario", su "Autor Favorito", "Libros Leídos Recientemente" y su "Nivel de Lectura" y al pulsar en "Obtener recomendación" se llama al servidor y éste usa el API de GROQ para lanzarle un prompt, obtener una respuesta del LLM y mostrársela al usuario.

## 3. Estructura de la aplicación

La aplicación sigue un patrón MVC. Modelo, Vista y Controlador. 

Esta aplicación no tiene **modelo**, que sería la representación de la información en la base de datos. En este caso por sencillez no guardamos nada de forma persistente.

La **vista** es una interfaz web basada en HTML y CSS que permite seleccionar los parámetros deseados y mandarlos al servidor.

El **controlador** ejecuta acciones o la lógica de la aplicación. Se encuentra en el fichero app.py donde se puede ver que hay dos rutas un GET sobre "/" y un POST sobre "/recommend"

## 4. Descargar e instalar el código del proyecto

Abra un terminal en su ordenador y siga los siguientes pasos.

Clone el repositoro de GitHub
```
git clone https://github.com/ging-moocs/MOOC_LLMs_mod2_ejemplo.git
```

Navegue a través de un terminal a la carpeta MOOC_LLMs_mod2_ejemplo.
```
cd MOOC_LLMs_mod2_ejemplo
```

Una vez dentro de la carpeta, se instalan las dependencias. Para ello debe crear un virtual environment de la siguiente manera:

```
[LINUX/MAC] > python3 -m venv venv
[WINDOWS] > py.exe -m venv venv
```

Si no tiene instalado venv, Lo puede instalar de la siguiente manera:

```
[LINUX/MAC] > python3 -m pip install --user virtualenv
[WINDOWS] > py.exe -m pip install --user virtualenv
```

Una vez creado el virtual environment lo activamos para poder instalar las dependencias:

```
[LINUX/MAC] > source venv/bin/activate
[WINDOWS] > .\venv\Scripts\activate
```

Instalamos las dependencias con pip:

```
pip3 install -r requirements.txt 
```

Tenemos que crear un fichero ".env" con el contenido del token de GROQ (sustituyendo XXXXX por tu API key de https://console.groq.com/keys):
```
GROQ_API_KEY=XXXXX
```


Ejecutamos la aplicación:
```
[LINUX/MAC] > python3 app.py
[WINDOWS] > py.exe app.py
```

Abra un navegador y vaya a la url "http://localhost:5000" para ver la aplicación.

**Si el modelo que se desea utilizar ya no está en Groq (deprecated), cámbialo por algún modelo que sí esté disponible:**

![Error al cargar la imagen](imgs/deprecated.png)

```
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="mistral-saba-24b", # modelo a utilizar
            temperature=0.7,
            max_tokens=1000,
        )
```

La lista de modelos disponibles puede consultarse en el Playground de grok:

![Error al cargar la imagen](imgs/playground.png)

