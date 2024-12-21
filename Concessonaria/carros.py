class Carros:
    def __init__(self, db_cursor):
        self.db_cursor = db_cursor
        self.table = 'carros' 

    def adicionarCarro(self, marca, modelo,preco):
        self.db_cursor.execute('INSERT INTO carros (marca, modelo,preco) VALUES (?, ?, ?)', (marca, modelo,preco))
        self.db_cursor.connection.commit() 

    def removerCarro(self, marca, modelo):
        self.db_cursor.execute('DELETE FROM carros WHERE marca = ? AND modelo = ?', (marca, modelo))
        self.db_cursor.connection.commit()

    def listarCarro(self):
        self.db_cursor.execute('SELECT marca, modelo FROM carros')
        carros = self.db_cursor.fetchall() 
        return carros
