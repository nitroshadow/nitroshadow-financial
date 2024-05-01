import sqlite3

class PortfolioData:
    DATABASE_NAME = 'portfolio_data.db'

    def __init__(self):
        print('PortfolioData')
        self.connection = sqlite3.connect('./data/' + self.DATABASE_NAME)
        self.cursor = self.connection.cursor()
