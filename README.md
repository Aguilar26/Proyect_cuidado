# 🌱 APP_PLANTAS - Proyecto Django + SQL Server

Este proyecto es una aplicación web desarrollada en **Django** que permite gestionar un catálogo de plantas, con condiciones reales de cuidado y un panel administrativo en español.  
La base de datos está en **SQL Server**, con conexión mediante **Windows Authentication (autenticación integrada)**.

---

## 🚀 Características principales

- **Panel Admin en español** con CRUD completo para plantas:
  - Crear, ver, editar y eliminar plantas.
  - Tabla con filtros, buscador y miniaturas de fotos.
- **Modelo Plant** con campos:
  - `name` (nombre de la planta)
  - `water` (nivel de riego)
  - `light` (tipo de luz)
  - `fertilizer` (frecuencia de fertilizante)
  - `location` (ubicación)
  - `maintenance` (nivel de mantenimiento)
  - `image_url` / `image_file` (foto de la planta)
  - `notes` (notas adicionales)
- **Sugerencias de plantas** según condiciones de cuidado.
- **Conexión automatizada a SQL Server** mediante `pyodbc`.

---

## 📂 Estructura del proyecto

