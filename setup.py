from setuptools import setup, find_packages

setup(
    name = 'pantsu',
    packages = find_packages(exclude=['tests']),
    version = '0.2',
    description = 'Pythons NyaaPantsu API wrapper',
    author = 'Juanjo Salvador',
    author_email = 'juanjosalvador@netc.eu',
    url = 'https://github.com/juanjosalvador/pantsu', # use the URL to the github repo
    download_url = 'https://github.com/juanjosalvador/pantsu/archive/0.1.tar.gz', # I'll explain this in a second
    keywords = ['nyaa', 'nyaa-pantsu', 'torrent', 'anime'], # arbitrary keywords
    classifiers = [],
)