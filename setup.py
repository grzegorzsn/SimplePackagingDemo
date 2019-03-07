from setuptools import find_packages, setup


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


def get_requirements():
    return parse_requirements("requirements.txt")


setup(
    name="superscrapper",
    version="0.3",
    author="Grzegorz Skupien",
    author_email="grzegorz.skupien4@orange.com, grzegorz@skupien.net",
    packages=find_packages(),
    install_requires=get_requirements(),
    classifiers=[
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6'
    ],
    entry_points={
        'console_scripts': [
            'scrap = superscrapper.scrapper:main'
        ]
    },
)
