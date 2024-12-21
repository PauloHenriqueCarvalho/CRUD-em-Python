class Clientes:
    def __init__(self, db_cursor):
        self.db_cursor = db_cursor
        self.table = 'clientes' 

    def login(self, nome, senha):
        self.db_cursor.execute('SELECT * FROM clientes WHERE nome = ? AND senha = ?', (nome, senha))
        cliente = self.db_cursor.fetchone() 
        return cliente 
