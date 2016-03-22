import codecs
import os.path
from setuptools import find_packages, setup


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

tests_require = [
    "flake8",
    "pytest",
    "pytest-cov",
    "tox",
    "tornado",
    "PyYAML"
]

setup(
    name="python_swagger_ui",
    author='Growbots',
    author_email='lukasz.jakobiec@growbots.com',
    url='https://github.com/growbots/python_swagger_ui/',
    #version = '0.1',
    use_scm_version={
        "root": here,
        "write_to": os.path.join(here, "swagger/_version.py"),
    },
    description="Swagger UI displaying swagger YAML definition",
    long_description=long_description,
    packages=find_packages(where=here),
    include_package_data=True,
    package_data={
        '': ['swagger/static/*'],
    },
    install_requires=[
        "tornado",
        "PyYAML"
    ],
    setup_requires=[
        "pytest-runner",
        "setuptools_scm>=1.10.1,<2.0.0",
        "tornado",
        "PyYAML"
    ],
    tests_require=tests_require,
    extras_require={
        "tests": tests_require,
    },

    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
