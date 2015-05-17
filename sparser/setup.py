from setuptools import setup

setup(
    name='sparser',
    version='0.1',
    description='URL scraper/text extractor',
    url='https://github.com/voite1/Python300_final_project',
    author='akramer',
    license='GPL',
    packages=['sparser','sparser.test'],
    install_requires=['BeautifulSoup4','joblib','lxml'],
)
