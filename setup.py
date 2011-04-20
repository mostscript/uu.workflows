from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='uu.workflows',
      version=version,
      description="UPIQ.org workflows for CMF/Plone (DCWorkflow).",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Framework :: ZODB",
        "Framework :: Plone",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        ],
      keywords='',
      author='Sean Upton',
      author_email='sean.upton@hsc.utah.edu',
      url='http://teamspace.upiq.org/trac',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uu'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.DCWorkflow',
          'Products.CMFCore',
          'z3c.autoinclude',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
