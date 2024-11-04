from setuptools import setup, find_packages

setup(
    name='auto_eda',
    version='0.1.0',
    author='Prajwal C N',
    author_email='prajwalnarayan.work@gmail.com',
    description='Automated Exploratory Data Analysis Library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        'plotly',
        'scikit-learn',
        'pandas-profiling',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
