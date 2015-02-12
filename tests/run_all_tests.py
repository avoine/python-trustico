#!/usr/bin/env python
# coding: utf-8

import os
import sys

POSSIBLE_TOPDIR = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                   os.pardir,
                                   os.pardir))

if os.path.exists(os.path.join(POSSIBLE_TOPDIR, 'TrusticoAPI', '__init__.py')):
   sys.path.insert(0, POSSIBLE_TOPDIR)


import unittest
from constraints import TestConstraint


if __name__ == '__main__':
    unittest.main()

