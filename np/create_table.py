import numpy as np
import pandas as pd
import insert_data
import matplotlib.pyplot as plt
# Why is stackData() in insert_data.py running when I run create_table.py?!
# You have to add the phase [if __name__ == "__main__": ]
# Then, create_table.py will run without the action of stackData() .

class GetTable:
    def __init__(self, init1, init2):
        print("GetTable Class...\n")
        self.init1 = init1
        self.init2 = init2
        self.initSet = [init1, init2]
    def showInitSet(self):
        print(f"initial set is ... {self.initSet}")
    
# Let's think how to fill class  
# I want to set tables n x 2 or n x 3 or n x 4 ....
# I draw architecture of this class from project! (?)

    
if __name__ == "__main__":
    initdata=GetTable(1, 2)
    initdata.showInitSet()
    dataList = np.zeros((1, 2))
    dataList = insert_data.stackData(dataList)
    print(dataList)
    
    dataTable = pd.DataFrame(data=dataList, columns=['input', 'output'])
    
    print(f"<dataTable>\n{dataTable}")
    print(f"print input datas....\n{dataTable['input']}")
    
    
    
    