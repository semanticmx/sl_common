from setuptools import setup, find_packages

setup(
    name='sl_common',
    version='0.1.0',
    packages=find_packages(where="src", exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    package_dir={"": "src"},
    install_requires=[
    ],
)
