from setuptools import setup, find_packages

name = "GymBro"
version = "1.0.0"
description = "A Gui Application Aimed at storing/using Gym PR's"
author = "Corey Patterson"
author_email = "634morse@gmail.com"
url = "https://github.com/634morse/ShredSheds_GymBro"

install_requires = [
    'ttkwidgets'
]

package_dir = {'': 'ShredSheds_GymBro'}

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    url=url,
    install_requires= install_requires,
    package_dir=package_dir,
    packages=find_packages()
)
