from distutils.core import setup

setup(
    name='AzureNVCCPlugin',
    version='0.0.51',
    author='Andrei Nechaev',
    author_email='lyfaradey@yahoo.com',
    py_modules=['nvcc_plugin', 'v2.v2', 'v1.v1', 'common.helper'],
    url='https://github.com/andreinechaev/nvcc4jupyter',
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA C/C++ code',
    # long_description=open('README.md').read(),
)
