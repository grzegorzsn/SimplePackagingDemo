from setuptools import find_packages, setup

setup(
    name="superscrapper",
    version="0.2",
    author="Grzegorz Skupien",
    author_email="grzegorz.skupien4@orange.com, grzegorz@skupien.net",
    packages=find_packages(),
    install_requires=["requests>=2"],
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
