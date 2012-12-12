#include <Python.h>


static const char base64_table[] = {
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/', '\0'
};
static const char base64_pad = '=';



 char *base64_encode(const char *str, size_t length, size_t *ret_length, int cut)
{
    const  char *current = str;
     char *p;
     char *result;

    if (length == 0) {
        if (ret_length != NULL) {
            *ret_length = 0;
        }
        return NULL;
    }

    result = (char *) malloc(((length + 2) / 3) * (4 * sizeof(char)));
    p = result;

    while (length > 2) { /* keep going until we have less than 24 bits */
        *p++ = base64_table[current[0] >> 2];
        *p++ = base64_table[((current[0] & 0x03) << 4) + (current[1] >> 4)];
        *p++ = base64_table[((current[1] & 0x0f) << 2) + (current[2] >> 6)];
        *p++ = base64_table[current[2] & 0x3f];

        current += 3;
        length -= 3; /* we just handle 3 octets of data */
    }

    /* now deal with the tail end of things */
    if (length != 0) {
        *p++ = base64_table[current[0] >> 2];
        if (length > 1) {
            *p++ = base64_table[((current[0] & 0x03) << 4) + (current[1] >> 4)];
            *p++ = base64_table[(current[1] & 0x0f) << 2];
            *p++ = base64_pad;
        } else {
            *p++ = base64_table[(current[0] & 0x03) << 4];
            *p++ = base64_pad;
            *p++ = base64_pad;
        }
    }
    if (ret_length != NULL) {
        *ret_length = (int)(p - result);
    }
    *p = '\0';
    return result;
}

static PyObject * ft_base64string(PyObject *self, PyObject *args)
{
    const char *string;
    size_t len_in = 0, len_out = 0;

    if (!PyArg_ParseTuple(args, "s", &string))
        return NULL;

	len_in = strlen(string);
	char *out = base64_encode(string, len_in, &len_out, 1);

    return Py_BuildValue("s#", out, len_out);
}

static PyObject * ft_base64(PyObject *self, PyObject *args)
{
    const char *string;
    size_t len_in = 0, len_out = 0;

    if (!PyArg_ParseTuple(args, "s", &string))
        return NULL;

    len_in = strlen(string);
    char *out = base64_encode(string, len_in, &len_out, 0);

    return Py_BuildValue("s", out);
}


static PyMethodDef ftMethods[] = {
    {"base64string",  ft_base64string, METH_VARARGS, "ft"},
    {"base64",  ft_base64, METH_VARARGS, "ft"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
initft(void)
{
    (void) Py_InitModule("ft", ftMethods);
}
