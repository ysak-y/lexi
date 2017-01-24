# lexi

## OverView

lexi is a library to create lambda function for AWS Lex.

## Install

```
pip install lexi
```

## Get Start

First, you must define function called as `handler` bellow.

```
e.g.

def lambda_handler(request, context=None):
    intent_name = request['currentIntent']['name']
    globals[intent_name](request, context)
```

Second, define functions same name to `intent` in Lex.

```
def StartIntent(request, context):
    """
        Some code here.
    """

def NextIntent(request, context):
    """
        Some code here.
    """
```

then, execute function when `intent` is called by Lex.
