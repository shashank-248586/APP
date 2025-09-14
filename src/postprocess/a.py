import example
import numpy as np

#command for compiling a cpp file into .so file
#c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` example.cpp -o example`python3-config --extension-suffix`
result = example.add(3, 5)
print(f"The result is: {result}")
array = np.array([1 , 3 , 4 , 5])
result = example.scale_array(array  , 4.0)
print(result)
