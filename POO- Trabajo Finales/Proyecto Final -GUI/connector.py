import mysql.connector

class Database:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="local", 
            database="tienda"
        )
        self.cursor = self.conexion.cursor()

    def insertar(self, codigo, descripcion, precio):
        # Ahora el código se pasa como parámetro manual
        sql = "INSERT INTO articulos (codigo, descripcion, precio) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (codigo, descripcion, precio))
        self.conexion.commit()

    def consultar(self, codigo):
        sql = "SELECT descripcion, precio FROM articulos WHERE codigo = %s"
        self.cursor.execute(sql, (codigo,))
        return self.cursor.fetchone()

    def listar_todos(self):
        self.cursor.execute("SELECT * FROM articulos")
        return self.cursor.fetchall()