from models.product import Product
from models.sale import Sale
from models._return import Return


class Inventory:
    def __init__(self):
        self.product= {} # initializers products as empty dictionary to store products using id as their key and product obj as their value
        self. sales = [] # initializing as an empty list to store all recorded transactions
        self.returns = [] # initializes returns as an empty list to store all recorded product returns.

    def add_product(self,product): # Method add_product adds a product to the inventory class. method takes one argument product which is an insatnce of inventory class
        self.product[product.id] = product

    def update_product(self,product_id,quantity): #Method called update product that updates the quantity of product in the inventory.It takes two agruments product_ id(to identify the product) and quantity new value
        if product_id in self.product:# if the product exists, it updates the product quantity to thenew values provided by quantity argument. this directly modifies the quantity attribute of the product stored is dictionary 
            self.product[product_id].quantity = quantity 
        else:
            print("product not found.")

    def dalete_product(self,product_id):
        if product_id in self.product:
            del self.product[product_id]
        else:
            print("product not found")

    def view_product(self):
        for product in self.product.values():
            print(product)

    def get_product(self,product_id):
        return self.product.get(product_id)
    
    def record_sale(self,product_id,quantity,price): # product_id (to identify the product has been sold) quantity (how many units of prodcts has beeen sold ) price (the selling price perunit)
        product = self.get_product(product_id)
        if product:
            if product.quantity >= quantity: # check if there is enough stock in inventory to fulfill the sale. it compares the current quantity of product with requested quantity for sale
              sale = sale(len(self.sales)+1,product_id,quantity,price)
              product.quantity-=quantity
              self.sales.append(sale)
              return sale
            else:
                print("Not enough quantity in stock")
        else:
            print("product not found")
        



    def record_return(self,product_id,quantity,reason): # product_id to identify the product quantity the number of units returned reason the return for reason
        product = self.get_product(product_id)
        if product:
            return_obj = Return(len(self.returns)+1,product_id,quantity,reason)
            product.quantity +=quantity
            self.rturns.append(return_obj)
        else:
            print("product not found.....")


    def view_sales(self):
        for sale in self.sales:
            print(sale)

    def view_return(self):
        for return_obj in self.returns:
            print(return_obj)