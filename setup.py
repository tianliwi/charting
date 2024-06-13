from setuptools import find_packages, setup

setup(
    name='Live Option Greeks Service',
    version='1.0.0',
    description='Services to update live option greeks.',
    url= 'https://codeup.aliyun.com/612e26644c890db05fc2bef1/mhlib/python_services.git',
    author="Zhanlu Tech",
    author_email="tianliwi@gmail.com",
    include_package_data= False,
    zip_safe= False,
    install_requires=[
        'requests',
        'pywebview',
        'pandas'
    ]
)
