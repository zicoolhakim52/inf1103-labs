from Product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self._download_size=download_size

    def get_fulfilment_info(self):
        print("Product is delivered digitally")

    def display_information(self):
        super().display_information() 
        print(f"Download size: {self._download_size}")

    def product_information(self):
            product_dict=super().product_information()
            product_dict["Download size"]=self._download_size
            return product_dict