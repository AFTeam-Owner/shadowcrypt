from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

def read_long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()

extensions = [
    Extension(
        "runner.cy_loader",
        ["runner/cy_loader.pyx"],
    )
]

setup(
    name="shadowseal",
    version="1.0.0",
    description="Secure Python encryptor and loader",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    author="Monarch of Shadows",
    author_email="farhanbd637@gmail.com",
    url="https://github.com/AFTeam-Owner/shadowseal",
    packages=find_packages(),
    ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'shadowseal=shadowseal.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7',
    zip_safe=False,
    options={
        'bdist_wheel': {'universal': '1'}
    }
)
