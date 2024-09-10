from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        list_of_products = file.read()
        file.close()
        return list_of_products

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for i in products:
            list_of_products = self.get_products()
            if i.name in list_of_products:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                file.write(f'{i}\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)

print(s1.get_products())