#include <Python.h>
#include <stdio.h>
#include <string.h>


void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t mysize, i;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	str = PyBytes_AsString(p);
	mysize = PyBytes_Size(p);
	printf("size: %ld\n", mysize);
	printf("trying string: %s\n", str);
	printf("first 6 bytes: ");
	for (i = 0; i < mysize && i < 9; i++)
	{
		printf("%02hhx ", str[i]);
	}
	if (i == 9)
	{
		printf("%02hhx\n", str[i]);
	}
	else
	{
		printf("%02hhx\n", '\0');
	}
}

void print_python_list(PyObject *p)
{
	Py_ssize_t i, list_size;
	const char *mytype;

	list_size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)(p))->allocated);
	for (i = 0; i < list_size; i++)
	{
		mytype = ((PyListObject *)(p))->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, mytype);
		if (!strcmp(mytype, "bytes"))
		{
			print_python_bytes(PyList_GetItem(p, i));
		}
	}
}