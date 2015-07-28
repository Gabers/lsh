try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description' : 'LSH project for mining massive datasets course',
        'author' : 'Gabriel Ryan',
        'author_email' : 'gabriel.ryan11@gmail.com',
        'install_requires': ['nose','numpy'],
        'packages': ['lsh','lsh/cluster'],
        'scripts': ['bin/runlsh'],
        'name': 'lsh'
}

setup(**config)
