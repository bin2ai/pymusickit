from setuptools import setup, find_packages
import pathlib

# The directory containing this file
here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='pymusickit',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'librosa==0.9.2',
        'matplotlib==3.7.0',
        'numpy==1.23.5'
    ],
    entry_points={
        'console_scripts': [
            'key_finder=pymusickit.key_finder:main',
        ],
    },
    description='A Python package for music analysis.  Keyfinder Forked from "https://github.com/jackmcarthur/musical-key-finder"',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='bin2ai',
    url='https://github.com/bin2ai/pymusickit',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
