#include <Python.h>
#include "drip_pay_lib.h"

// Example function
static PyObject *example_func(PyObject *self, PyObject *args)
{
  const char *input;
  if (!PyArg_ParseTuple(args, "s", &input))
  {
    return NULL;
  }
  return Py_BuildValue("s", input);
}

// Method definitions
static PyMethodDef DripPayMethods[] = {
    {"example_func", example_func, METH_VARARGS, "Example function"},
    {NULL, NULL, 0, NULL}};

// Module definition
static struct PyModuleDef drippaymodule = {
    PyModuleDef_HEAD_INIT,
    "drippay",
    NULL,
    -1,
    DripPayMethods};

// Module initialization function
PyMODINIT_FUNC PyInit_drippay(void)
{
  return PyModule_Create(&drippaymodule);
}
