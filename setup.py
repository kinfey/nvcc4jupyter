from distutils.core import setup

setup(
    name='AzureNVCCPlugin',
    version='0.0.7',
    py_modules=['azureml_nvcc_plugin', 'v2.v2', 'v1.v1', 'common.helper'],
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA C/C++ code',
    # long_description=open('README.md').read(),
)
