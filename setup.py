from setuptools import setup

setup(
    name='lexus',
    version='0.2.1',
    description='Easy development tool for AWS Lex',
    url='https://github.com/ysak-y/lexus-test.git',
    author='Yoshiaki Yamada',
    author_email='yoshiaki.0614@gmail.com',
    license='MIT',
    packages=['lexus'],
    zip_safe=False,
    entry_points={
        'console_scripts': 'lexus = lexus.template_generator:main'
        }
)
