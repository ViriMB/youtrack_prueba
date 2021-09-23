# Prueba MB

### Version de Python.
```python
python 3.6.7
```
### Actulizar pip.

```python
Linux y OS X
pip install -U pip

Windows
python -m pip install -U pip
```

### Crear entorno en virtualenv.
```python
sudo pip3 install virtualenv
virtualenv env -p python3
```
### Activar entorno.
```python
source env/bin/activate
```
### Instalar dependecias del pip.
```python
pip install -r requerimientos.txt
```
### El docuento "requerimientos.txt" tiene estas librerias.
```python
Django
djangorestframework
```

### Para hacer las migraciones corra estos comandos.
```python
python manage.py makemigrations
python manage.py migrate
```

### Para correr el programa utilice el siguiente comando.
```python
python manage.py runserver 0.0.0.0:8000
```


### API de persona.
```
GET
http://localhost:8000/api/persona/list

