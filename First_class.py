class Car:
    def __init__(self, model: str, color: str, max_speed: int, is_electric: bool):
        """

        :param model: the model of the car
        :param color: the color of the car
        :param max_speed: the maximum speed the car can achieve
        :param is_electric: True if it is electric, False otherwise
        """
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.is_electric = is_electric

    def print_info(self) -> None:
        """
        A method to print all the info about the car
        :return: None
        """
        print(f"The model of your car is {self.model}, the color is {self.color},\
         the maximum speed is {self.max_speed}. Is the car electric - {self.is_electric}")

    def change_color(self, new_color: str) -> None:
        """
        A method to change the color of the car
        :param new_color: the name of the new color
        :return: None
        """
        self.color = new_color

    def get_max_speed(self) -> int:
        """
        A method to get the maximum speed
        :return: maximum speed
        """
        return self.max_speed


if __name__ == "__main__":
    my_car = Car("Tesla", "White", 300, True)
    my_car.print_info()
