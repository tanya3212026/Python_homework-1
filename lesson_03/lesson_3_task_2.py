from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S24", "+79161234567"),
    Smartphone("Apple", "iPhone 15", "+79262345678"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79373456789"),
    Smartphone("Google", "Pixel 8", "+79484567890"),
    Smartphone("Huawei", "P60 Pro", "+79595678901"),
]

for phone in catalog:
    print(phone.info())
