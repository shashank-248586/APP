import numpy as np
#output is a list of numpy objects
def convert(l):
    result = []
    for single in l:
        temp_result = []
        for index , i in enumerate(single):
            if (i.size != 0):
                temp = np.reshape(i , (1 , 5))
                temp = temp * 640
                temp = np.append(temp , index)
                temp_result.append(temp)
        temp_result = np.array(temp_result)
        result.append(temp_result)
    
    return result