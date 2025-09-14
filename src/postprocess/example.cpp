#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
// Define the function
int add(int a, int b) {
    return a + b;
}

namespace py = pybind11;

// ----------------------
// scale_array (for testing)
// ----------------------
py::array_t<float> scale_array(py::array_t<float> arr, float factor) {
    auto buf = arr.request();
    float* ptr = (float*) buf.ptr;
    for (ssize_t i = 0; i < buf.size; i++) {
        ptr[i] *= factor;
    }
    return arr;
}
// Create the Python module
PYBIND11_MODULE(example, m) {
    m.doc() = "Example module created with pybind11"; // Optional module docstring
    m.def("add", &add, "A function that adds two numbers");
    m.def("scale_array" , &scale_array , "A function that aiosjfjs");
}
