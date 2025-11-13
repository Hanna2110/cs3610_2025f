from FurnitureAbstractfactory import SmallTableClass
from FurnitureAbstractfactory import BigTableClass
from FurnitureAbstractfactory.ITableClass import ITable

from typing import Type
'''
Each concrete factory corresponds to a specific product variant
'''


class TableFactory:  
    '''
    The Concrete Table Factory Class
    '''

    @staticmethod
    def get_table(table:str)-> ITable:
        '''A static method to get a table'''
        try:
            if table == 'BigTable':
                return BigTableClass.BigTable()
            if table == 'SmallTable':
                return SmallTableClass.SmallTable()
            raise Exception('Table Not Found')
        except Exception as _e:
            print(_e)
        return None