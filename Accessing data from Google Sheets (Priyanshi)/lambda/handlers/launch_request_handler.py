from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.dispatch_components import (AbstractRequestHandler, AbstractExceptionHandler, AbstractRequestInterceptor, AbstractResponseInterceptor)

class LaunchRequestHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):    #Determines whether or not that handler can service the request
        return is_request_type("LaunchRequest")(handler_input)
    
    def handle(self, handler_input):
        #language_prompts = handler_input.attributes_manager.request_attributes["_"]
        #speech_output = random.choice(language_prompts["DEFAULT_MSG"])
        #reprompt = random.choice(language_prompts["DEFAULT_MSG"])
        
        default_msg = "Google Sheets is open, which cell would you like me to read or write to, or would you like to look anything up?"
        speech_output = default_msg
        reprompt = default_msg
        
        return (
            handler_input.response_builder  #This function will help build the response to the user
                .speak(speech_output)
                .ask(reprompt)
                .response
        )