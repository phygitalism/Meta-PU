from __future__ import division, absolute_import, with_statement, print_function
from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import glob

_ext_src_root = "pointnet2/_ext-src/"
_ext_sources = glob.glob("{}/src/*.cpp".format(_ext_src_root)) + glob.glob(
    "{}/src/*.cu".format(_ext_src_root)
)

requirements = ["etw_pytorch_utils", "h5py", "enum34", "future"]

setup(
    name="pointnet2",
    version="2.2.2",
    author="Erik Wijmans",
    packages=find_packages(),
    install_requires=requirements,
    ext_modules=[
        CUDAExtension(
            name="pointnet2._ext",
            sources=_ext_sources,
            extra_compile_args={
                "cxx": ["-O2"],
                "nvcc": ["-O2"],
            },
            include_dirs=["{}/include".format(_ext_src_root)],
        )
    ],
    cmdclass={"build_ext": BuildExtension},
    include_package_data=True,
)