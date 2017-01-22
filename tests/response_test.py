# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.abspath('..'))
from lexi import lex_io as lex

import unittest
from nose.tools import *
from fixtures.responses import DEFAULT_RESPONSE
from fixtures.requests import DEFAULT_REQUEST

class TestResponse(object):
    #def setUp(self):

    #def tearDown(self):
    
    def test_default_response(self):
        eq_(DEFAULT_RESPONSE, lex.lambda_handler(DEFAULT_REQUEST, None))
