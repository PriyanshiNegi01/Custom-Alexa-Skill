from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.dispatch_components import (AbstractRequestHandler, AbstractExceptionHandler, AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.handler_input import HandlerInput

import json
import gspread

#Accessing the Google Sheets spreadsheet
sheet_url = "https://docs.google.com/spreadsheets/d/1UvI8x9_4c0F_GgKtAwLx9x6P22p7HV0_OfSB2RVel3I"
gc = gspread.service_account(filename = 'credentials.json')
sh = gc.open_by_url(sheet_url)

'''
class SearchIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("SearchIntent")(handler_input)

    def handle(self, handler_input):
        search_query = handler_input.request_envelope.request.intent.slots['SearchQuery'].value
        search_query = str(search_query)

        worksheet = sh.get_worksheet(0)
        flag = 0
        for i in range(0, 1000, 1):   #row
            for j in range(0, 26, 1):  #column
                val = worksheet.cell(i+1, j+1).value    #getting a cell value
                val = str(val)
                
                cell_col = chr(65+j)
                cell_row = i+1
                finalcell = str(cell_col) + str(cell_row)
                
                if (val == search_query):   #Case sensitive search with no shortform
                    speech_output = search_query + " is in " + finalcell
                    reprompt = search_query + " is in " + finalcell
                    flag = 1
                    
                elif (val != search_query): #Case insensitive search with shortform
                    val_lower = val.lower()
                    sq_lower = search_query.lower()
                    sq_lower = sq_lower.replace('. ','')
                    
                    if (val_lower == sq_lower):
                        speech_output = search_query + " is in " + finalcell
                        reprompt = search_query + " is in " + finalcell
                        flag = 1
                
                if flag==1:
                    break
            if flag==1:
                break
        if flag == 0:
            speech_output = search_query + " is not in the sheet. "
            reprompt = search_query + " is not in the sheet. "
        return (
                handler_input.response_builder
                    .speak(speech_output)
                    .ask(reprompt)
                    .response
            )
'''
class SearchIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("SearchIntent")(handler_input)

    def handle(self, handler_input):
        search_query = handler_input.request_envelope.request.intent.slots['SearchQuery'].value
        search_query = str(search_query)
        #search_query_withshortform = search_query.replace('. ','')

        worksheet = sh.get_worksheet(0)
        
        if worksheet.find(search_query):
            cell = worksheet.find(search_query)
            cell_col = chr(64+cell.col)
            cell_row = cell.row

            finalcell = str(cell_col) + str(cell_row)
            speech_output = search_query + " is in " + finalcell
            reprompt = search_query + " is in " + finalcell

            return (
                handler_input.response_builder
                    .speak(speech_output)
                    .ask(reprompt)
                    .response
            )

        else:
            speech_output = search_query + " is not in the sheet. "
            reprompt = search_query + " is not in the sheet. "

            return (
                handler_input.response_builder
                    .speak(speech_output)
                    .ask(reprompt)
                    .response
            )