class City:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def get_city_info(self) -> str:
        return f"Город - {self.name}. Население = {self.population}"


first_city = City("Saint-Petersburg", 5000000)
print(first_city.name)

second_city = City("Yaroslavl", 598000)
print(second_city.get_city_info())
