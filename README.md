# Proyecto del curso de python-django

## requerientos
* sistema operativo windows, linux, mac
* python 3.5+
* tener instalado pip
* tener instalado virtualenv
  
  ```bash
  pip install virtualenv
  ```
  
## implementacion 
* clonar el proyecto

    ```bash
    git clone git@github.com:neotrons/syscoffe-project.git
    ```
 
* crear el entorno vistual
    ```bash
    cd syscoffe-project
    virtualenv env
    source env/Scripts/active
    ```
* Instalar requerimientos
    ```bash
    pip install -r requirements.txt
    ```
## Configurar proyecto
* copiar archivo de configuracion por ambiente 
    ```bash
    cd syscoffe/syscoffe/settings
    cp -ra example_enviroment.py local.py
    ```

