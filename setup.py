from setuptools import setup, find_packages

setup(
    name='SellingPartnerAPISDK',  # Replace with your package's name
    version='1.0.0',         # Replace with your package's version
    # package_dir={
    #     'SellingPartnerAPISDK': '',
    # },  # Replace 'src' as necessary
    packages=find_packages(),
    install_requires=[line.strip() for line in open("SellingPartnerAPISDK/requirements.txt", "r")],
    description='A Python SDK for Amazon Selling Partner API',
    long_description=open('SellingPartnerAPISDK/README.md').read(),
    long_description_content_type='text/markdown',
    url='TBD'
)
