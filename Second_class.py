class Shop:
    def __init__(self, name: str, products: dict, number_of_customers: int, position: str):
        """

        :param name: The name of the shop
        :param products: A dictionary with all the products. Keys - products, values - prices
        :param number_of_customers: The number of customers in the shop
        :param position: Where the shop is located
        """
        self.name = name
        self.products = products
        self.number_of_customers = number_of_customers
        self.position = position

    def check_product(self, product: str) -> bool:
        """
        A method to check if the product is in the shop
        :param product: the name of the product
        :return: True if the product is in the shop or False if the product is not in the shop
        """
        return product in self.products

    def add_customers(self, new_customers: int) -> None:
        """
        A method to add the number of new customers
        :param new_customers:
        :return: None
        """
        self.number_of_customers += new_customers

    def change_position(self, new_position) -> None:
        """
        A method to change the location of the shop
        :param new_position: the string with the new location
        :return: None
        """
        self.position = new_position

    def get_product_price(self, product) -> int:
        """
        A method to get the price of the product
        :param product: the name of the product
        :return: The price of the product, if it is in the shop or an exception otherwise
        """
        if self.check_product(product):
            return self.products[product]
        raise Exception


if __name__ == "__main__":
    products = {"Milk": 120, "Bread": 90, "Chocolate": 100}
    my_shop = Shop("Very good shop", products, 300, "Prospekt Bolshevikov 22")
