import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

setup(name='ajaplugin_plone',
      version='0.1.0',
      description='',
      long_description="%s\n%s" % (README, CHANGES),
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
      ],
      author='Jukka Ojaniemi',
      author_email='jukka.ojaniemi@gmail.com',
      url='https://github.com/pingviini/ajaplugin_plone',
      keywords='aja deploy plone buildout',
      package_dir={"": "src"},
      packages=find_packages('src'),
      include_package_data=True,
      test_suite="ajaplugin_plone.tests",
      zip_safe=False,
      install_requires=[
          'setuptools',
          'aja',
          'path.py',
      ],
      entry_points={
          'aja.plugins.deploy': 'plone = ajaplugin_plone.deploy:PloneDeploy',
      },
      )
