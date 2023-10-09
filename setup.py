from setuptools import setup

name = "GymBro"
version = "1.0.0"
description = "A Gui Application Aimed at storing/using Gym PR's"
author = "Corey Patterson"
author_email = "634morse@gmail.com"
url = "https://github.com/634morse/ShredSheds_GymBro/tree/development"

install_requires = [
    'ttkwidgets'
]

package_dir = {'': 'SHREDSHEDS_GYMBRO'}

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    url=url,
    install_requires= install_requires,
)
