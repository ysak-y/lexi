# -*- coding: utf-8 -*-
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

# Requestクラス作って、get_sessionでsessionAttributesをいい感じにdicに変換したやつを返すようにする。
#recipe = json.loads(sessionAttributes["Recipe"])

class Response(object):

    def __init__(self, dic):
        self.content = dic

    def with_session_attributes(self, session_attributes):
        self.content['sessionAttributes'] = session_attributes
        return self

class ResponseBuilder(object):

    @classmethod
    def elicit_intent(self, message=None, card=None):
        '''
            Argments

            message:
                Optional. you can build message using MessageBuilder.
                If message is None, Amazon Lex uses one of the bot's
                clarification prompts.(see the Error Handling section in the console.)

            card:
                Optional. you can build card using CardBuilder.
                If card is None, Amazon Lex uses one of the bot's
                clarification prompts.(see the Error Handling section in the console.)
        '''
        response = self._build_response('ElicitSlot', message=message, card=card)
        return Response(response)

    @classmethod
    def elicit_slot(self, intent_name, slot_to_elicit, slots, message=None, card=None):
        '''
            Argments

            # Required

            intent_name:
                Basicaly, set requests['currentIntent']['name']

            slots:
                Slots must include all of the slots configured for the intent.
                If the value of a slot is unknown, it must be explicitly set to null (similar to Lambda function request)

            slot_to_elicit:
                 Informs Amazon Lex that the user is expected to provide a slot value in response.
                 For example, a value for the pizzaSize or pizzaKind slots.

            message:
                Optional. you can build message using MessageBuilder.
                If message is None, Amazon Lex uses one of the bot's
                clarification prompts.(see the Error Handling section in the console.)

            card:
                Optional. you can build card using CardBuilder.
                If card is None, Amazon Lex uses one of the bot's
                clarification prompts.(see the Error Handling section in the console.)
        '''
        response = self._build_response('ElicitSlot', intent_name=intent_name, slot_to_elicit=slot_to_elicit, slots=slots, message=message, card=card)
        return Response(response)

    @classmethod
    def confirm_intent(self, intent_name, slots, message=None, card=None):
        '''
            Argments

            # Required

            intent_name:
                Basicaly, set requests['currentIntent']['name']

            slots:
                Slots must include all of the slots configured for the intent.
                If the value of a slot is unknown, it must be explicitly set to null (similar to Lambda function request)

            # Optional

            message:
                You can build message using MessageBuilder.
                If message is None, Amazon Lex uses one of the bot's
                clarification prompts.(see the Error Handling section in the console.)

            card:
                You can build card using CardBuilder.
                If card is None, Amazon Lex uses one of the bot's
                clarification prompts.(see the Error Handling section in the console.)
        '''
        response = self._build_response('ConfirmIntent', intent_name=intent_name, slots=slots, message=message, card=card)
        return Response(response)

    @classmethod
    def delegate(self, slots):
        '''
            Argments

            # Required

            slots:
                Slots must include all of the slots configured for the intent.
                If the value of a slot is unknown, it must be explicitly set to null (similar to Lambda function request)
        '''
        response = self._build_response('delegate', slots=slots)
        return Response(response)

    @classmethod
    def close(self, fulfillment_state, message=None, card=None):
        '''
            Argments

            # Required

            fulfillment_state:
                Set 'Fulfilled' or 'Failed'.
                Amazon Lex uses this value to set the dialogState in its response to the client.

            # Optional

            message:
                You can build message using MessageBuilder.
                If message is None, Amazon Lex uses one of the bot's
                clarification prompts.(see the Error Handling section in the console.)

            card:
                You can build card using CardBuilder.
                If card is None, Amazon Lex uses one of the bot's
                clarification prompts.(see the Error Handling section in the console.)
        '''
        response = self._build_response('close', fulfillment_state=fulfillment_state, message=message, card=card)
        return Response(response)

    def _build_response(self, response_type, fulfillment_state=None, message=None, intent_name=None, slots=None, slot_to_elicit=None, card=None):

        dic = {
                'dialogAction': {
                        'type': response_type,
                    }
                }

        if fulfillment_state:
            dic['dialogAction']['fulfillmentState'] = fulfillment_state

        if message:
            dic['dialogAction']['message'] = message

        if card:
            dic['dialogAction']['responseCard'] = card

        if intent_name:
            dic['dialogAction']['intentName'] = intent_name

        if slots:
            dic['dialogAction']['slots'] = slots

        if slot_to_elicit:
            dic['dialogAction']['slotToElicit'] = slot_to_elicit

        return dic

class CardBuilder(object):

    def __init__(self, version):
        self.content = {}
        self.content['version'] = version
        self.content['contentType'] = 'application/vnd.amazonaws.card.generic'

class MessageBuilder(object):

    @classmethod
    def build_message(self, content, content_type="PlainText"):
        return {
                'contentType': content_type,
                'content': content
                }
