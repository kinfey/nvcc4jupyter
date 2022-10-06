from v1.v1 import AzureNVCCPlugin as NVCC_V1
from v2.v2 import AzureNVCCPluginV2 as NVCC_V2


def load_ipython_extension(ip):
    azure_ml_nvcc_plugin = NVCC_V1(ip)
    ip.register_magics(azure_ml_nvcc_plugin)

    azure_nvcc_plugin_v2 = NVCC_V2(ip)
    ip.register_magics(azure_ml_nvcc_plugin)
