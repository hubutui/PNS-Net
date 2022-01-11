import sys
from os.path import join

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

project_root = 'PNS_Module'
sources = [join(project_root, file) for file in ['sa_ext.cpp',
                                                 'sa.cu','reference.cpp']]


nvcc_args = [
    '-gencode', 'arch=compute_60,code=sm_60',
    '-gencode', 'arch=compute_61,code=sm_61',
    '-gencode', 'arch=compute_62,code=sm_62',
    '-gencode', 'arch=compute_70,code=sm_70',
    '-gencode', 'arch=compute_72,code=sm_72',
    '-gencode', 'arch=compute_75,code=sm_75',
    '-gencode', 'arch=compute_80,code=sm_80',
    '-gencode', 'arch=compute_86,code=sm_86'
]

if sys.platform == "linux":
    cxx_args = ['-std=c++14']
elif sys.platform == "win32":
    cxx_args = ['/std:c++14', '/utf-8']
else:
    raise RuntimeError(f"Unsuported platform: {sys.platform}")

setup(
    name='self_cuda',
    ext_modules=[
        CUDAExtension('self_cuda_backend',
                      sources, extra_compile_args={'cxx': cxx_args,'nvcc': nvcc_args})
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
