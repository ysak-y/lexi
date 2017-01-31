# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.abspath('..'))
from lexi import lex

import unittest
from nose2.tools import params
from fixtures.responses import DEFAULT_RESPONSE
from fixtures.requests import DEFAULT_REQUEST

class TestResponse(unittest.TestCase):
    def test_raise_elicit_slot_without_intent_name(self):
        slots = ['2', '3', '4']
        with self.assertRaises(TypeError):
            lex.ResponseBuilder.elicit_slot(slots=slots)

#class TestResponse(object):
    #def setUp(self):

    #def tearDown(self):
    
#    def test_default_response(self):
#        eq_(DEFAULT_RESPONSE, lex.lambda_handler(DEFAULT_REQUEST, None))

    #def test_elicit_slot_response(self):

    #def test_confirm_intent_response(self):

    #def test_
