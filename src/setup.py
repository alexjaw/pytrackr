from setuptools import setup, find_packages

setup(name='pytrackr',
      version='0.0.1',
      description='Interface to the Trackr API',
      url='http://github.com/w1ll1am23/pytrackr',
      author='William Scanlon',
      license='MIT',
      install_requires=['requests>=2.0'],
      tests_require=['mock'],
      test_suite='tests',
      packages=find_packages(exclude=["dist", "*.test", "*.test.*", "test.*", "test"]),
      zip_safe=True)
