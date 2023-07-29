from setuptools import setup

REQUIRES = [
    'sqlalchemy',
    'structlog',
    'allure-pytest',

]
setup(
    name='orm_client',
    version='0.0.1',
    packages=['orm_client'],
    url='https://github.com/kberezuck/orm_client.git',
    license='MIT',
    author='Ksenia_Berezuck',
    author_email='',
    install_requires=REQUIRES,
    description='orm client with allure and login'
)
