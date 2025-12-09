import pyodbc

def conectar_sql_server():
    try:
        # Ajusta el nombre de tu instancia si no es SQLEXPRESS
        server = r'localhost\SQLEXPRESS'   # o simplemente 'localhost' si usas la instancia por defecto
        database = 'PlantDB'               # tu base de datos

        # Conexión usando autenticación de Windows
        conexion = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'Trusted_Connection=yes;'
        )

        print("✅ Conexión establecida correctamente a SQL Server con autenticación de Windows")
        return conexion

    except Exception as e:
        print("❌ Error al conectar a SQL Server:", e)
        return None


if __name__ == "__main__":
    conn = conectar_sql_server()
    if conn:
        cursor = conn.cursor()
        # Prueba: listar las tablas disponibles
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES;")
        tablas = cursor.fetchall()
        print("📂 Tablas en la base de datos:")
        for t in tablas:
            print("-", t[0])
        conn.close()
