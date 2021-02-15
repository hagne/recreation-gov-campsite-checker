import sys

required_verion = (3,)
if sys.version_info < required_verion:
    raise ValueError('At least python {} needed! You are trying to install under python {}'.format('.'.join(str(i) for i in required_verion), sys.version))

# import ez_setup
# ez_setup.use_setuptools()

from setuptools import setup
# from distutils.core import setup
setup(
    name='recreationdotgov',
    version="0.1",
    packages=['recreationdotgov'],
    author="Hagen Telg",
    author_email="hagen@hagnet.net",
    description="recreation.gov wrapper",
    license="MIT",
    keywords="recreation.gov",
    url="https://github.com/hagne/recreation-gov-campsite-checker",
    scripts=['scripts/recreation_s1', 
             # 'scripts/hrrr_smoke2gml'
             ],
    # install_requires = ['numpy', 'pandas', 'matplotlib', 'mpl_toolkits', 'geopy', 'netCDF4', 'magic', 'gdal'],
    # extras_require={'plotting': ['matplotlib'],
    #                 'testing': ['scipy']},
    # test_suite='nose.collector',
    # tests_require=['nose'],
)