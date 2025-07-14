from setuptools import setup, find_packages

setup(
    name='shadowcrypt',
    version='1.0.0',
    description='A Python package to securely encrypt and run Python files with custom encryption and anti-debug features.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/AFTeam-Owner/shadowcrypt',
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'shadowcrypt=shadowcrypt.cli:main',
            'shadowcrypt-encrypt=encryptor.encrypt:main',
            'shadowcrypt-run=runner.loader:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
