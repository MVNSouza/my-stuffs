from db import get_connection
from modelo import Country

class CountryDAO:
    def __init__(self):
        self.conn = get_connection()

    def buscar_por_code(self, code: str) -> Country | None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT code, name FROM country WHERE code = ?", (code,))

        row = cursor.fetchone()
        return Country(code=row[0], name=row[1]).name if row else None

    def listar_todos(self) -> list[Country]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT code, name FROM country")
        return [Country(code=row[0], name=row[1]).name for row in cursor.fetchall()]