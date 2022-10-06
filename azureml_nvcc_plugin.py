from v1.v1 import AzureNVCCPlugin as NVCC_V1
from v2.v2 import AzureNVCCPluginV2 as NVCC_V2


def load_ipython_extension(ip):
    azureml_nvcc_plugin = NVCC_V1(ip)
    ip.register_magics(azureml_nvcc_plugin)

    azureml_nvcc_plugin_v2 = NVCC_V2(ip)
    ip.register_magics(azureml_nvcc_plugin_v2)
