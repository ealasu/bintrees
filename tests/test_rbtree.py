#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: test RBTrees
# Created: 28.04.2010

import unittest2 as unittest
from tree_test import TestTreeMixin

from bintrees import RBTree

class TestRBTree(TestTreeMixin, unittest.TestCase):
    @property
    def TREE(self):
        return RBTree

if __name__=='__main__':
    unittest.main()