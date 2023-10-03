from setuptools import setup, find_packages

setup(
    name="pn7150_reader",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # add any dependencies if needed
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package to read from and write to NFC tags using the PN7150/PN7120 NFC modules.",
    keywords="NFC PN7150 PN7120 reader writer",
    url="http://github.com/yourusername/pn7150_reader",   # project home page, if any
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
