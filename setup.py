from distutils.core import setup, Extension

module1 = Extension('ft',
                    sources = ['ft.c'])

setup (name = 'ft',
       version = '1.0',
       description = 'This is a package that provides fast base64',
       ext_modules = [module1])
