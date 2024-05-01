import sqlite3

class PortfolioData:
    DATABASE_NAME = 'portfolio_data.db'

    def __init__(self):
        print('PortfolioData')
        connection = sqlite3.connect('./data/' + self.DATABASE_NAME)
        cursor = connection.cursor()
