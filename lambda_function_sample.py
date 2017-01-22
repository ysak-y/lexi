# -*- coding: utf-8 -*-

import lexi

def lambda_handler(request, context=None):
    intent_name = request['currentIntent']['name']
    globals()[intent_name](request, context)
