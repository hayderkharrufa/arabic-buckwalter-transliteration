from setuptools import setup, find_packages

setup(
    name='arabic_buckwalter_transliteration',
    version='0.1.0',    # your package version
    description='A Python package to convert Arabic text to Buckwalter transliteration and vice versa',
    author='Your Name',    # your name
    author_email='your.email@example.com',    # your email
    packages=find_packages(),
    install_requires=[],  # any libraries that your module depends on
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)