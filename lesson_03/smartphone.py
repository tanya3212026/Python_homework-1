class Smartphone:
    def __init__(self, brand, model, number):
        self.brand_phone = brand
        self.model_phone = model
        self.number = number

    def info(self):
        return f"{self.brand_phone} - {self.model_phone}. {self.number}"
