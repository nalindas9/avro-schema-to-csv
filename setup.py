from setuptools import setup, find_packages

setup(
    name='avro-schema-to-csv',
    version='0.1.0',
    description='Convert Avro schema to CSV.',
    author='Nalin Das',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)