import uuid
from model.model import Product

class DatabaseMock:
    def __init__(self, session): # 1
        self.session = session # 2

    def get_product(self, id:uuid):
        self.session.execute('SELECT * FROM Product WHERE _id=?', (id,))
        return self.session.fetchone()

    def save_status(self,Product):
        self.session.execute('INSERT INTO Product VALUES (?, ?,?, ? , ?,?)', (Product.id, Product.nome,Product.type,Product.qtde,Product.cost,Product.status))
        self.session.connection.commit()

    def generate_report(self):
        self.session.execute('SELECT COUNT(*) FROM numbers')
        count = self.session.fetchone()
        self.session.execute('SELECT COUNT(*) FROM numbers WHERE existing=1')
        count_existing = self.session.fetchone()
        return count_existing[0]/count[0]