import numpy as np

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


def stackData(dataSet):
    while True:
        try:
            # insert input and output datas...
            dataInput =  float(input("input data: "))
            dataOutput = float(input("output data: "))
        
            # make datapair as numpy.array
            dataPair = np.array([dataInput, dataOutput])
            
            # reset [[0. 0.]] and replace the first dataPair array
            if dataSet.shape == (1,2):
                dataSet = dataPair
            # stack vertically
            else:
                dataSet = np.vstack((dataSet,dataPair))
            
            # print process of dataSet
            print(dataSet)
            
        except KeyboardInterrupt:
            print("The ctrl + c key is pressed! \nLet's finish the data insert!")
            break
    
    return dataSet

if __name__ == "__main__":
    dataList = np.zeros((1, 2)) # initial values
    print(f"dataList = {dataList}")        

    dataList = stackData(dataList)

    print("final dataSet...")
    print(dataList)
    
    # print(f"dataLisst[1] = {dataList[1]}")