class Warehouse:

    def __init__(self):
        self.products={}

    def buy (self,product,quantity):
        if product in self.products:
            self.products[product]+=quantity
        else:
            self.products[product]=quantity
    def sell (self,product,quntity):
        if product in self.products and self.products[product]>=quntity:
            self.products[product]-=quntity
            if self.products[product]==0:
                del self.products[product]
        else:
            print( "insufficint stoke")
    def search (self,product):
        if product in self.products:
            print(f"quntity {product} is -->{self.products[product]}")
        else:
            print("not found")
    def show (self):
        for i,j in self.products.items():
            print( f"{i}--->{j}")
    def save (self):
        with open("pro.txt","w") as f:    
            for i,j in self.products.items():
                 f.write(f"{i} - {j}\n")
    def report (self):
        print(f"quntity all products: {len(self.products)} number")
        print(f"stock all :{sum(self.products.values())}")
        max_product = max(self.products, key=self.products.get)
        print(f" max priduct : {max_product}--{self.products[max_product]}")
        min_product = min(self.products, key=self.products.get)
        print(f" min priduct : {min_product}--{self.products[min_product]}")