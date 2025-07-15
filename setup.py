from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
from pathlib import Path

def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text(encoding='utf-8')

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
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Monarch of Shadows",
    author_email="farhanbd637@gmail.com",
    url="https://github.com/AFTeam-Owner/shadowseal",
    license="MIT",
    python_requires=">=3.8",
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
        "Programming Language :: Cython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
    ],
    zip_safe=False,
)
