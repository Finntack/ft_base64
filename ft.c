#include <Python.h>


static char encoding_table[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                                'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                                'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                                'w', 'x', 'y', 'z', '0', '1', '2', '3',
                                '4', '5', '6', '7', '8', '9', '+', '/'};
static int mod_table[] = {0, 2, 1};


char *base64_encode(const char *data,
                    size_t input_length,
                    size_t *output_length,
                    int cut) {

    *output_length = (size_t) 1 + (4.0 * ceil((double) input_length / 3.0));

    printf("%zi\n", *output_length);

    *output_length += ceil(((double)*output_length / 76.0) * 2.0) * cut;

    printf("%zi\n", *output_length);

    char *encoded_data = malloc(*output_length);
    if (encoded_data == NULL) return NULL;

    int i,j,k;

    for (i = 0, j = 0, k = 0; i < input_length;) {
        k+=4;

        uint32_t octet_a = i < input_length ? data[i++] : 0;
        uint32_t octet_b = i < input_length ? data[i++] : 0;
        uint32_t octet_c = i < input_length ? data[i++] : 0;

        uint32_t triple = (octet_a << 0x10) + (octet_b << 0x08) + octet_c;

        encoded_data[j++] = encoding_table[(triple >> 3 * 6) & 0x3F];
        encoded_data[j++] = encoding_table[(triple >> 2 * 6) & 0x3F];
        encoded_data[j++] = encoding_table[(triple >> 1 * 6) & 0x3F];
        encoded_data[j++] = encoding_table[triple & 0x3F];

        if (cut && k == 76)
        {
            k = 0;
            encoded_data[j++] = '\r';
            encoded_data[j++] = '\n';
        }
    }

    int mtable_index = mod_table[input_length % 3];
    for (i = 0; i < mtable_index; i++)
        encoded_data[j++] = '=';

    encoded_data[j++] = '\0';

    return encoded_data;
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
