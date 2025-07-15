from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

extensions = [
    Extension(
        "runner.cy_loader",
        ["runner/cy_loader.pyx"],
    )
]

setup(
    name="shadowseal",
    version="0.1.0",
    description="Secure Python encryptor and loader",
    author="Monarch of Shadows",
    packages=find_packages(),
    ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'shadowseal=shadowseal.cli:main',
        ],
    },
    zip_safe=False,
)
