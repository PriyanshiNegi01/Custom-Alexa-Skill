from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.dispatch_components import (AbstractRequestHandler, AbstractExceptionHandler, AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.handler_input import HandlerInput

import json
import gspread

#Accessing the Google Sheets spreadsheet
sheet_url = "https://docs.google.com/spreadsheets/d/1UvI8x9_4c0F_GgKtAwLx9x6P22p7HV0_OfSB2RVel3I"
gc = gspread.service_account(filename = 'credentials.json')
sh = gc.open_by_url(sheet_url)

class ReadCellIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):    #Determines whether or not that handler can service the request
        return is_intent_name("ReadCellIntent")(handler_input)
        
    def handle(self, handler_input):
        # Accessing the slot value
        cell = handler_input.request_envelope.request.intent.slots['Cell'].value
        
        cell = str(cell)
        worksheet = sh.get_worksheet(0)
        cell_data = worksheet.get(cell)[0][0]
        
        #speech_output = f"The data of {slot_value} is {cell_value}."
        speech_output = cell_data
        reprompt = cell_data

        return (
            handler_input.response_builder
                .speak(speech_output)
                .ask(reprompt)
                .response
        )
