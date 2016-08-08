from setuptools import setup

setup(
    name='zyx',
    version='',
    url='https://github.com/wolfhechel/zyn',
    license='',
    author='Pontus Karlsson',
    author_email='pontus@jensenkarlsson.se',
    install_requires=[
        'pyserial<3',
        'xmodem',
        'progressbar2',
        'pyelftools'
    ],
    packages=[
        'zyx',
        'zyx.commands'
    ],
    description='Zyxel utilities',
    entry_points={
        'console_scripts': [
            'zyx = zyx.__main__:main'
        ]
    },
)
