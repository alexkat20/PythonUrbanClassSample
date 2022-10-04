class House:
    THIS_YEAR = 2022

    def __init__(self, location: str, people: list, year: int, number_of_apartments: int):
        """
        :param location: the place where the house is located
        :param people: the number of people in the house
        :param year: when the house was built
        :param number_of_apartments: the number of apartments in the house
        """
        self.location = location
        self.people = people
        self.year = year
        self.number_of_apartments = number_of_apartments

    def add_new_resident(self, resident: str) -> None:
        """
        A method to add one new resident
        :param resident: the name of a new resident
        :return: None
        """
        self.people.append(resident)

    def add_new_residents(self, residents: list) -> None:
        """
        A method to add new residents to the list of residents
        :param residents: a list of new residents
        :return: None
        """
        for resident in residents:
            self.add_new_resident(resident)

    def count_people_per_apartment(self) -> float:
        """
        A method to count the mean number of people in an apartment
        :return: the mean number of people in an apartment
        """
        return len(self.people) / self.number_of_apartments

    def check_age(self) -> str:
        """
        A method to check if the house is old, new or normal
        :return: string with the characteristics of the house' age
        """
        if (self.year - self.THIS_YEAR) < 10:
            return "New house"
        elif (self.year - self.THIS_YEAR) < 20:
            return "Normal house"
        return "Old house"


if __name__ == "__main__":
    people = ["Mark, John, Lucy, Anna"]
    my_house = House("Prospekt Bolshevikov", people, 2015, 50)
    my_house.add_new_residents(["Alex", "Olesya"])
    print(my_house.people)
    my_house.add_new_resident("Peter")
    print(my_house.people)

