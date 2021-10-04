import numpy as np

class GetData():
    def __init__(self):
        print("GetData class...")
        self.dataSet = GetData.insertData(self)
    
    def insertData(self):
        self.dataInput =  float(input("input data: "))
        self.dataOutput = float(input("output data: "))
        
        return np.array([self.dataInput, self.dataOutput])

    def stackData(self):
        while True:
            try:
                # make datapair as numpy.array
                self.dataPair = GetData.insertData(self)
                # dataPair = self.insertData() # Why is this error...
                self.dataSet = np.vstack((self.dataSet,self.dataPair))  

                # print process of dataSet
                print(f"dataSet = \n{self.dataSet}")
                
            except KeyboardInterrupt:
                print("The ctrl + c key is pressed! \nLet's finish the data insert!")
                break
        
        return self.dataSet

if __name__ == "__main__":
    id = GetData()
    # dataList = id.insertData() # initial values
    # print(f"dataList = {dataList}")
    dataList = id.stackData()

    print("final dataSet...")
    print(dataList)
    
    # print(f"dataLisst[1] = {dataList[1]}")
    
    
# a = np.arange(6)
# print(f"a = {a}")
# a2 = a[np.newaxis, :]
# print(f"a2 = {a2}")
# print(f"a2.shape = {a2.shape}")
# print("\n")

# inputText = input("what is x?")
# x = int(inputText)
# print(f"x = {x}")

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(matrix)

# print([[row[i] for row in matrix] for i in range(4)])
# print(matrix)

# insert input and output datas...