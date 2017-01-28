# -*- coding: utf-8 -*-

import lexi

def lambda_handler(request, context=None):
    intent_name = request['currentIntent']['name']
    return globals()[intent_name](request, context).to_dict()
