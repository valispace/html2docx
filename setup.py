from setuptools import setup, find_packages

setup(
    name='html2docx',
    version='0.1',
    packages=find_packages(),
    author='valispace',
    description='Convert html to docx for export features',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/valispace/html2docx',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
