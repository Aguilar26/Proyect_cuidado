# 🌱 APP_PLANTAS - Proyecto Django + SQL Server

Este proyecto es una aplicación web desarrollada en **Django** que permite gestionar un catálogo de plantas con condiciones reales de cuidado y un panel administrativo completamente en español. Utiliza **SQL Server** como base de datos y se conecta mediante **autenticación integrada de Windows (Windows Authentication)**, lo que permite una conexión segura y sin necesidad de credenciales explícitas.

---

## 🔑 Solución de conexión a SQL Server

La solución para establecer la conexión fue usar **Windows Authentication** en lugar de SQL Server Authentication.

### Pasos clave:
- Identificar la instancia correcta: `MSSQLSERVER` (la instancia por defecto).  
- Configurar el `HOST` como `.` (punto), que representa localhost con la instancia local.  
- Activar `Trusted_Connection` con valor `'yes'` para usar las credenciales del sistema operativo.  
- Eliminar los campos `USER` y `PASSWORD`, ya que no se necesitan con Windows Authentication.  

### Configuración final en `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'PlantDB',
        'HOST': '.',  # instancia local por defecto
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
        },
    }
}
```

### Por qué funcionó:
- Windows Authentication es más segura que SQL Authentication para desarrollo local.  
- No requiere credenciales explícitas (usa las del sistema operativo).  
- El punto (`.`) es más confiable que `localhost` o `127.0.0.1` para conectar a SQL Server localmente.  
- Django y `pyodbc` interpretan mejor `Trusted_Connection=yes` que intentar conectar con usuarios SQL.

---

## 📂 Estructura del proyecto

- `manage.py`: archivo principal para ejecutar comandos Django.  
- `automatizacion.py`: script independiente para probar la conexión a SQL Server.  
- `planta/`: app Django que contiene el modelo `Plant` y su configuración administrativa.  
- `Proyect_cuidado/`: carpeta de configuración principal del proyecto Django (settings, urls, etc.).  
- `venv/`: entorno virtual de Python (ignorado en Git).  

---

## ⚙️ Instalación y configuración

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/Aguilar26/Proyect_cuidado.git
   cd Proyect_cuidado
   ```

2. **Crear entorno virtual**  
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instalar dependencias**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Migrar la base de datos**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear superusuario**  
   ```bash
   python manage.py createsuperuser
   ```

---

## 🧪 Probar conexión SQL Server

Ejecuta el script `automatizacion.py` para validar la conexión:

```bash
python automatizacion.py
```

Salida esperada:
```
✅ Conexión establecida correctamente a SQL Server con autenticación de Windows
📂 Tablas en la base de datos:
- django_migrations
- django_session
- planta_plant
```

---

## 🌱 Uso del panel admin

1. Inicia el servidor:  
   ```bash
   python manage.py runserver
   ```
2. Accede a:  
   ```
   http://127.0.0.1:8000/admin/
   ```
3. Ingresa con tu superusuario.  
4. Gestiona las plantas desde la tabla CRUD con filtros, buscador y miniaturas.

---

## 📦 Requisitos

- Python 3.10+  
- Django 5.x  
- SQL Server (local o remoto)  
- ODBC Driver 17 for SQL Server  
- pyodbc  

Ejemplo de `requirements.txt` mínimo:
```
Django==5.0.3
mssql-django==1.3
pyodbc==5.1.0
```

---

## 📌 Próximos pasos

- Añadir más plantas con condiciones reales.  
- Mejorar el formulario de sugerencias para usuarios finales.  
- Documentar una API REST para integrar con frontend.  
- Configurar despliegue en producción (Docker, Azure, etc.).  

---

## 👨‍💻 Autor

Proyecto desarrollado por **Julian Aguilar**  
Arquitecto autodidacta de soluciones técnicas y editoriales, especializado en Python/Django y SQL Server.
