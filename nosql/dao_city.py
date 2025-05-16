from db import get_connection
from modelo import City

class CityDAO:
    def __init__(self):
        self.conn = get_connection()

    def buscar_por_id(self, id: int) -> City | None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name FROM city WHERE id = ?", (id,))

        row = cursor.fetchone()
        return City(id=row[0], name=row[1]).name if row else None

    def listar_todos(self) -> list[City]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name FROM city")
        return [City(id=row[0], name=row[1]).name for row in cursor.fetchall()]