class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        # result = []
        # for item in self.products:
        #     if item[0] == first_letter:
        #         result.append(item)
        # return result
        return [el for el in self.products if el.startswith(first_letter)]

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        # for item in sorted(self.products):
        #     result += f"{item} \n"
        result += "\n".join(sorted(self.products))
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
