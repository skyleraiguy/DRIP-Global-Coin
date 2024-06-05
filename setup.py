from setuptools import setup, Extension

module = Extension('drippay',
                   sources=['Python.c', 'drip_pay_lib.c'],
                   include_dirs=['/usr/include/python3.10', './crypto-env/Include'])

setup(name='DripPay',
      version='1.0',
      description='DripPay Microtransaction Library',
      ext_modules=[module])
