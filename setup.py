from setuptools import setup, find_packages

setup(
    name='arabic_buckwalter_transliteration',
    version='1.0.2',
    description='A Python package to convert Arabic text to Buckwalter transliteration and vice versa',
    author='Hayder Kharrufa',
    author_email='',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
