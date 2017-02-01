# -*- coding: utf-8 -*-

from lexi import lex

def lambda_handler(request, context=None):
    intent_name = request['currentIntent']['name']
    req = lex.Request(request).to_dict 
    if intent_name in globals():
        return globals()[intent_name](req, context).to_dict()
    else:
        return lex.ResponseBuilder.elicit_intent("Can't find intent name's function in lambda.")
