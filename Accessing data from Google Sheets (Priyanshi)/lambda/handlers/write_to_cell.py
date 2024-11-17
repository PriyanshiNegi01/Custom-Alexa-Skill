from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.dispatch_components import (AbstractRequestHandler, AbstractExceptionHandler, AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.handler_input import HandlerInput

import json
import gspread

#Accessing the Google Sheets spreadsheet
sheet_url = "https://docs.google.com/spreadsheets/d/1UvI8x9_4c0F_GgKtAwLx9x6P22p7HV0_OfSB2RVel3I"
gc = gspread.service_account(filename = 'credentials.json')
sh = gc.open_by_url(sheet_url)

class AddDataIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AddDataIntent")(handler_input)
    
    def handle(self, handler_input):
        cell_col = handler_input.request_envelope.request.intent.slots['CellCol'].value
        cell_row = handler_input.request_envelope.request.intent.slots['CellRow'].value
        cell = str(cell_col) + str(cell_row)
        
        handler_input.attributes_manager.session_attributes['previous_slot_value'] = cell #storing the slot value
        
        speech_output = "What would you like me to write to " + cell + "?"
        #reprompt = "What would you like me to write to" + cell + "?"
        return (
            handler_input.response_builder
                .speak(speech_output)
                #.ask(reprompt)
                .response
        )

class WriteToCell(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("WriteToCellIntent")(handler_input)
    
    def handle(self, handler_input):
        cell_data = handler_input.request_envelope.request.intent.slots['CellData'].value
        
        
        #cell = handler_input.request_envelope.request.intent.slots['Cell'].value
        #cell_data = handler_input.request_envelope.request.intent.slots['Data'].value
        
        cell = handler_input.attributes_manager.session_attributes.get('previous_slot_value') #retrieving the previous slot value

        worksheet = sh.get_worksheet(0)
        worksheet.update(cell, cell_data)
        speech_output = "Data is written into the sheet. Would you like to do something else? If yes, what is it?"
        reprompt = "Data is written into the sheet. Would you like to do something else? If yes, what is it?"
        
        return (
            handler_input.response_builder
                .speak(speech_output)
                .ask(reprompt)
                .response
        )