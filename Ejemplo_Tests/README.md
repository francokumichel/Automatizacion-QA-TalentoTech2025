# Ejemplo test

En este ejemplo la idea es ver como se realiza un test básico con `pytest`. A continuación se describirán una seríe de pasos a seguir para preparar el entorno y ejecutar las pruebas.

1. Crear entorno virtual

    En la carpeta raiz del proyecto, creamos un entorno virtual. Acá por ejemplo usamos `venv`

    ``` bash
    python -m venv venv
    ```

    Si sale todo bien, esto genera una carpeta con el nombre `venv`.

2. Activar el entorno virtual
    
    Esto es depende que sistema operativo utilices.

    - Linux/Mac
        
        ``` bash
        source venv/bin/activate
        ```
    - Windows

        ``` cmd
        .\venv\Scripts\Activate
        ```

    Si está activo, deberías ver el prefijo (venv) en la consola

3. Instalar `pytest`

    Con el entorno activo, instalamos `pytest`

    ```
    pip install pytest pytest-html
    ```

    Se agrega `pytest-html` como un plugin para generar reportes HTML.

    Es mucho muy importante una vez que instalamos dependencias, actualizar el archivo `requirements.txt` de la siguiente manera:

    ``` bash
    pip freeze > requirements.txt
    ``` 

4. Estructura del proyecto

    Hay que tener en cuenta que por covención, pytest busca:

    - Archivos que empiezan con `_test` o terminan con `_test.py`.
    - Funciones que empiezan con `_test`.

    Por lo tanto, para una mejor organización, los tests se alojarán en el directorio `tests/`.

    ``` bash
        proyecto/
        │
        ├── calculadora.py
        └── tests/
            │
            ├── test_calculadora.py
            ├── test_calculadora_avanzado.py
    ```

4. Ejecución de los tests

    - Ejecución simple

        ``` bash
        pytest
        ```
    
    - Ejecución tipo "verbose" (más detallado)

        ``` bash
        pytest -v
        ```

