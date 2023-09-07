from setuptools import setup, find_packages

setup(
    name='githubactiontesting',
    version='0.0.6',
    packages=find_packages('githubaction', exclude=['test']),
    url='https://github.com/dievalcorentin/Githubaction_test',
    license='',
    author='Corentin Dieval',
    author_email='corentin@graphmytech.fr',
    description='Testing GitHub Action and creation of package'
)
