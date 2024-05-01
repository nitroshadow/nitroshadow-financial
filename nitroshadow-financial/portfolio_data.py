import sqlite3

class PortfolioData:
    DATABASE_NAME = 'portfolio_data.db'

    def __init__(self):
        print('PortfolioData')
        self.connection = sqlite3.connect('./data/' + self.DATABASE_NAME)
        self.cursor = self.connection.cursor()

    def tableExists(self, name):
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}'"
        result = self.cursor.execute(query)

        if result.fetchone() is None:
            return False
        return True
