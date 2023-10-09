#include <Python.h>

/**
 * print_python_list_info - a function that prints info about python lists.
 * @p: pointer to PyObject struct.
 *
 * Return: nothing.
 */
void print_python_list_info(PyObject *p)
{
	unsigned int i;
	unsigned long int size = PyList_Size(p);
	PyListObject *q = (PyListObject *)p;

	printf("[*] Size of the Python List = %lu\n", size);

	printf("[*] Allocated = %lu\n", q->allocated);

	for (i = 0; i < size; i++)
		printf("Element %u: %s\n", i, Py_TYPE(q->ob_item[i])->tp_name);
}
