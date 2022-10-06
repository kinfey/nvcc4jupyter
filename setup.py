from distutils.core import setup

setup(
    name='AzureMLNVCCPlugin',
    version='0.1.2',
    py_modules=['azureml_nvcc_plugin', 'v2.v2', 'v1.v1', 'common.helper'],
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA C/C++ code',
    # long_description=open('README.md').read(),
)
