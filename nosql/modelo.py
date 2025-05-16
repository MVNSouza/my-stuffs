
class City:
    def __init__(self,
                 id: int = 0,
                 name: str = "",
                 country_code: str = "",
                 district: str = "",
                 population: int = 0):
        self.id = id
        self.name = name
        self.country_code = country_code
        self.district = district
        self.population = population

class Country:
    def __init__(self,
                 code: str = "",
                 name: str = "",
                 continent: str = "",
                 region: str = "",
                 surface_area: float = 0.0,
                 indep_year: int = 0,
                 population: int = 0,
                 life_expectancy: float = 0.0,
                 gnp: float = 0.0,
                 gnp_old: int = 0,
                 local_name: str = "",
                 government_form: str = "",
                 head_of_state: str = "",
                 capital: str = "",
                 code2: str = ""):
        self.code = code
        self.name = name
        self.continent = continent
        self.region = region
        self.surface_area = surface_area
        self.indep_year = indep_year
        self.population = population
        self.life_expectancy = life_expectancy
        self.gnp = gnp
        self.gnp_old = gnp_old
        self.local_name = local_name
        self.government_form = government_form
        self.head_of_state = head_of_state
        self.capital = capital
        self.code2 = code2

class CountryLanguage:
    def __init__(self,
                 countrycode: str = "",
                 language: str = "",
                 is_official: bool = "",
                 percentage: float = 0.0):
        self.countrycode = countrycode
        self.language = language
        self.is_official = is_official
        self.percentage = percentage

class Estado:
    def __init__(self,
                 id: int = 0,
                 nome: str = "",
                 sigla: str = "",
                 populacao: int = 0,
                 capital: str = ""):
        self.id = id
        self.nome = nome
        self.sigla = sigla
        self.populacao = populacao
        self.capital = capital