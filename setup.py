#! /usr/bin/python

import sys
from distutils.core import setup
import glob
import os
import operator
try:
  import py2exe
except:
  pass

## A few pre-setup hacks
#if os.name != 'posix':
#  sys.path.insert( 0, 'bkchem')

# the setup itself

set = setup(
  name = 'oasa',
  version = '0.12.0',
  description = "OASA is a free cheminformatics library written in Python",
  author = "Beda Kosata",
  author_email = "beda@zirael.org",
  url = "http://bkchem.zirael.org/oasa_en.html",
  license = "GNU GPL",
  platforms = ["Unix", "Windows", "hopefully other OSes able to run Python"],
  long_description = "OASA is a free cheminformatics library written in Python",
  
  packages=[ 'oasa', 'oasa/graph'],

  #data_files=[ ('oasa', glob.glob( 'oasa/templates/*.cdml')+glob.glob('templates/*.xml')),

  #windows=['oasa'],
  #options = {"py2exe": {"packages": ["encodings"]}}
  )

