import os
from setuptools import setup, find_packages

version = '6.8'

setup(name='quintagroup.theme.schools',
      version=version,
      description="Free Diazo theme for Plone",
      long_description=open(os.path.join("README.rst")).read() + "\n\n" +
                       open(os.path.join("docs", "INSTALL.rst")).read() + "\n\n"+
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='web zope plone theme diazo quintagroup',
      author='Quintagroup',
      author_email='skins@quintagroup.com',
      url='http://themes.quintagroup.com/product/schools',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['quintagroup', 'quintagroup.theme',],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'plone.app.theming',
                        # -*- Extra requirements: -*-
                        ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
