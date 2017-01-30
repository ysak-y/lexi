# -*- coding: utf-8 -*-

from lexi import lex

def lambda_handler(request, context=None):
    intent_name = request['currentIntent']['name']
    req = lex.Request(request).to_dict 
    return globals()[intent_name](req, context).to_dict()
