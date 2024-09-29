from models.transaction import Transaction
from datetime import datetime

class Return(Transaction):
    def __init__(self,id,product_id,quantity,price,reason):
        super().__init__(id,product_id,quantity,price)
        self.reason = reason
        self.date=datetime.now()

    def to_dict(self):
        return{
            "id":self.product_id,
            "product_id":self.quantity,
            "price":self.price,
            "reason":self.reason,
            "date":self.date
        }