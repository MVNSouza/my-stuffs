# importação de city
from dao_city import CityDAO
from modelo import City


# importação de country
from dao_country import CountryDAO
from modelo import Country

# importação de countrylanguage
from dao_country_language import CountryLanguageDAO
from modelo import CountryLanguage

# importação de estado
from dao_estado import EstadoDAO
from modelo import Estado

city_dao = CityDAO()
print(city_dao.buscar_por_id(247))

country_dao = CountryDAO()
print(country_dao.buscar_por_code("BRA"))
print(country_dao.listar_todos())

country_language_dao = CountryLanguageDAO()
print(country_language_dao.buscar_por_pais("BRA"))

estado1 = Estado(1, "sao paulo", "SP", 18927462, "sao paulo")
estado2 = Estado(2, "rio de janeiro", "RJ", 18927462, "rio de janeiro")
estado3 = Estado(1, "ceara", "CE", 18927462, "fortaleza")

estado_dao = EstadoDAO(estados = [])
estado_dao.salvar(estado1)
estado_dao.salvar(estado2)
estado_dao.salvar(estado3)
print(estado_dao.listar_todos())