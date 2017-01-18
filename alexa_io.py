
"""
Request sample
{
  "messageVersion": "1.0",
  "invocationSource": "FulfillmentCodeHook or DialogCodeHook",
  "userId": "user-id specified in the POST request to Amazon Lex.",
  "sessionAttributes": { 
     "key1": "value1",
     "key2": "value2",
  },
  "bot": {
    "name": "bot-name",
    "alias": "bot-alias",
    "version": "bot-version"
  },
  "outputDialogMode": "Text or Voice, based on ContentType request header in runtime API request",
  "currentIntent": {
    "name": "intent-name",
    "slots": {
      "slot-name": "value",
      "slot-name": "value",
      "slot-name": "value"
    },
    "confirmationStatus": "None, Confirmed, or Denied (intent confirmation, if configured)"
  }
}

Response sample

{
  "sessionAttributes": {
    "key1": "value1",
    "key2": "value2"
    ...
  },
  "dialogAction": {
    "type": "ElicitIntent, ElicitSlot, ConfirmIntent, Delegate, or Close",
    "fulfillmentState": "Fulfilled or Failed",
    "message": {
      "contentType": "PlainText or SSML",
      "content": "message to convey to the user"
    },
   "intentName": "intent-name",
   "slots": {
      "slot-name": "value",
      "slot-name": "value",
      "slot-name": "value"  
   },
   "slotToElicit" : "slot-name",
   "responseCard": {
      "version": integer-value,
      "contentType": "application/vnd.amazonaws.card.generic",
      "genericAttachments": "[
          {
             "title":"card-title",
             "subTitle":"card-sub-title",
             "imageUrl":"URL of the image to be shown",
             "attachmentLinkUrl":"URL of the attachment to be associated with the card",
             "buttons":[ 
                 {
                    "text":"button-text",
                    "value":"value sent to server on button click"
                 }
              ]
           } 
       ]"  
     }
  }
}
"""

class Request(object):

    def __init__(self, request_dict, metadata=None)
