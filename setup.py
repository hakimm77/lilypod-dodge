from setuptools import setup

setup(
    name='LilypodDodge',
    version='1.1.7',
    packages=['lilypod_dodge', 'lilypod_dodge/resources'],

    license='MIT',
    long_description='My first game',
    install_requires=[
                    'pygame',
                     ],
    include_package_data=True,
    author='Gabriel Petersson',
    author_email='gabriielpetersson@gmail.com',
    url='https://github.com/gabrielpetersson/lilypod_dodge'
)
