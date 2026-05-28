# Gamekey

Tienda de videojuegos online desarrollada con Django REST Framework en el backend y HTML, CSS y JavaScript vanilla en el frontend.

<img width="1024" height="1024" alt="gamekey" src="https://github.com/user-attachments/assets/db421e64-3356-4179-bf66-ba307e2d74c6" />
---

## Requisitos previos

- [Python 3.10 o superior](https://www.python.org/downloads/) — marcar la opción **"Add Python to PATH"** durante la instalación
- Un navegador (Chrome, Firefox, Edge...)
- Git (para clonar el repositorio)

---

## Instalación paso a paso


### 1. Clonar el repositorio

```bash
git clone https://github.com/AldanVillar/ProyectoIntermodular_DAW2.git
cd ProyectoIntermodular_DAW2
```
O descargarlo como ZIP desde GitHub y descomprimirlo.

### 2. Instalar las dependencias de Python

```bash
cd backend
pip install -r requirements.txt
```
Esto instala Django, Django REST Framework y django-cors-headers.

### 3. Aplicar las migraciones de la base de datos

```bash
python manage.py migrate
```

### 4. Poblar la base de datos con datos de ejemplo (yo lo probe en el ordenador de casa y la base de datos ya estaba subida en el repositorio, pero en caso de que no funcione se puede hacer esto)

```bash
python manage.py poblar_datos
```
Esto crea automáticamente los juegos, géneros, plataformas y noticias de ejemplo.

### 5. Arrancar el servidor

```bash
python manage.py runserver
```
El servidor quedará corriendo en http://127.0.0.1:8000

### 6. Abrir el frontend
Con el servidor en marcha, abre el archivo frontend/html-css/GamekeyInicio.html directamente en el navegador.
