#ifndef DRIP_PAY_PYTHON_H
#define DRIP_PAY_PYTHON_H

#include <Python.h>

// Function declarations
PyObject *py_initialize_drip_pay(PyObject *self, PyObject *args);
PyObject *py_process_microtransaction(PyObject *self, PyObject *args);
PyObject *py_finalize_drip_pay(PyObject *self, PyObject *args);

#endif // DRIP_PAY_PYTHON_H
