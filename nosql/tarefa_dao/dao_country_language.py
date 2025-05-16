from db import get_connection
from modelo import CountryLanguage

class CountryLanguageDAO:
    def __init__(self):
        self.conn = get_connection()

    def buscar_por_pais(self, countrycode: str) -> list[CountryLanguage]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT countrycode, language FROM countrylanguage WHERE countrycode = ?", (countrycode,))
        return [CountryLanguage(countrycode=row[0], language=row[1]).language for row in cursor.fetchall()]

    def listar_todos(self) -> list[CountryLanguage]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT countrycode, name FROM countrylanguage")
        return [CountryLanguage(countrycode=row[0], language=row[1]).language for row in cursor.fetchall()]