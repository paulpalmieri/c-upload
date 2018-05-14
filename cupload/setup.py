from setuptools import setup

setup(
    name = 'cupload',
    version = '0.1',
    install_requires = ['selenium'],
    entry_points='''
        [console_scripts]
        cupload=cupload:main
    '''
)