from distutils.core import setup
setup(
  name = 'parfit',
  packages = ['parfit'], # this must be the same as the name above
  version = '0.14',
  description = 'A package for parallelizing the fit and flexibly scoring of sklearn machine learning models, with optional plotting routines.',
  author = 'Jason Carpenter',
  author_email = 'jmcarpenter2@dons.usfca.edu',
  url = 'https://github.com/jmcarpenter2/parFit', # use the URL to the github repo
  download_url = 'https://github.com/jmcarpenter2/parFit/archive/0.14.tar.gz', 
  keywords = ['parallelize', 'sklearn', 'machinelearning','models', 'fit'], # arbitrary keywords
  install_requires = [
    'joblib',
    'matplotlib',
    'sklearn',
    'np'
  ],
  classifiers = [],
)
