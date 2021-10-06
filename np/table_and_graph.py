import numpy as np
import pandas as pd
import data_insert
import matplotlib.pyplot as plt
# Why is stackData() in insert_data.py running when I run create_table.py?!
# You have to add the phase [if __name__ == "__main__": ]
# Then, create_table.py will run without the action of stackData() .

class GetTable():
    def __init__(self):
        print("GetTable Class...\n")
    
    def settingData(self):
        print("setting Data list...")
        self.id = data_insert.GetData()
        self.dataSet = self.id.stackData()
        
        return self.dataSet
    
    def showTable(self):
        self.dataTable = pd.DataFrame(data=self.dataSet, columns = ['input', 'output'])
        print(f"<dataTable>\n{self.dataTable}")
        return self.dataTable
         
class GetGraph(GetTable): # Overiding from GetTable
    def __init__(self):
        print("GetGraph Class...\n")
        
    def settingData(self):
        return super().settingData()
    
    def settingTable(self):
        return super().showTable()
    # I wanted to show graph after inserting data, 
    # get table through pandas, and get inheritane...!
    def showGraph(self):
        self.df = self.settingTable()
        self.df.plot(kind='line', x='input', y='output')
        plt.show()
        
        '''
        Let's consider how to set the float value(decimal point ............)
        (2021.10.07)
        '''
        
    
# Let's think how to fill class  
# I want to set tables n x 2 or n x 3 or n x 4 ....
# I draw architecture of this class from project! (?)

    
if __name__ == "__main__":
    # gt = GetTable()
    # dataList = gt.settingData()
    # dataTable = gt.showTable()
    
    gg = GetGraph()
    dataGraph = gg.settingData()
    dataTable = gg.settingTable()
    gg.showGraph()
    
    print(f"<dataTable>\n{dataTable}")
    print(f"print input datas....\n{dataTable['input']}")
    
    print(f"<dataGraph>\n{dataGraph}")
    print(f"print input datas....\n{dataGraph[0]}")
    
    
    