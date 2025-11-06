from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='webssh-sh',
    version='22.11.8',
    description='Shell Helpers about WebSSH',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/isontheline/webssh.sh',
    author='Arnaud MENGUS',
    license='MIT',
    packages=['wsh'],
    install_requires=[
        'importlib-metadata>=1.0; python_version<"3.8"',
    ],
    scripts=[],
    entry_points={
        'console_scripts': ['wshcopy=wsh.wshcopy:cli'],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
    python_requires='>=3.8',
)
