try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Pyload Clipboard Monitor for linux',
    'author': 'Francois Billant',
    'url': 'https://github.com/francois-learnings/pcm.git',
    'download_url': 'https://github.com/francois-learnings/pcm.git',
    'author_email': 'fbillant@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['pcm'],
    'scripts': [],
    'name': 'pcm'
}

setup(**config)

