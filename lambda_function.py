from __future__ import print_function

# --------------- Helpers that build all of the responses ----------------------
count=0
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def answer_response():
    session_attributes = {}
    card_title = "answer"
    speech_output = "Great!Here we go!"\
    "Some questions will be asked to you and you need to answer in one word only!"\
    "What is your age?"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def age_response(intent_request):
    global count
    print("age=",intent_request["intent"]["slots"]["age"]["value"])
    session_attributes = {}
    card_title = "age"
    answer=intent_request["intent"]["slots"]["age"]["value"]
    answer=int(answer)
    if answer >= 1 and answer <= 25:
        count=count+0
    elif answer > 25 and answer <= 40:
        count = count+1
    elif answer > 40 and answer <= 50:
        count = count+2
    else:
        count = count+3
    speech_output = "please, tell me your gender"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def gender_response(intent_request):
    global count
    session_attributes = {}
    print(intent_request)
    card_title = "gender"
    answer=intent_request["intent"]["slots"]["gender"]["value"]
    if answer:
        count=count+1
    speech_output = "tell me about your body tempreture!please choose any one option!High fever or normal body tempreture?"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def body_temp_response(intent_request):
    global count
    print(intent_request)
    session_attributes = {}
    card_title = "bodyTemp"
    answer=intent_request["intent"]["slots"]["fever"]["value"]
    if answer == "high fever":
        count=count+1
    else:
        count=count+0
    speech_output = "Are you experiencing any of the disease symptoms?please choose any one option!coughing,snezzing,body weakness or just alright?"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def disease_response(intent_request):
    global count
    print(intent_request)
    session_attributes = {}
    card_title = "disease"
    answer=intent_request["intent"]["slots"]["disease"]["value"]
    if answer == "alright":
        count=count+0
    else:
        count=count+1
    speech_output = "Do you have any serious symptoms?please choose any one option!severe coughing,difficulty in breathing,pressure in chest or just none?"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def severe_response(intent_request):
    global count
    print(intent_request)
    session_attributes = {}
    card_title = "severe"
    answer=intent_request["intent"]["slots"]["severe"]["value"]
    if answer == "none":
        count=count+0
    else:
        count=count+2
    speech_output = "have you travelled anywhere in past few days, within a week or period of fortnight?please choose any one option! i did or i did not."
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def past_response(intent_request):
    global count
    print(intent_request)
    session_attributes = {}
    card_title = "past"
    answer=intent_request["intent"]["slots"]["travel"]["value"]
    if answer == "i did":
        count=count+2
    else:
        count=count+0
    speech_output = "Do you have history of any disease?please choose any one option! diabetes,blood pressure,heart disease,lung disease or kidney disease! or just say nothing?"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def status_response(intent_request):
    global count
    print(intent_request)
    session_attributes = {}
    card_title = "status"
    answer=intent_request["intent"]["slots"]["past"]["value"]
    if answer == "nothing":
        count=count+0
    else:
        count=count+2
    speech_output = "How have your symptoms progressed over the last 48 hours!please choose any one option! improved,stable or getting wrost?"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def final_response(intent_request):
    global count
    print(intent_request)
    session_attributes = {}
    card_title = "final"
    answer=intent_request["intent"]["slots"]["status"]["value"]
    if answer == "improved":
        count=count-1
    elif answer == "stable":
        count=count+0
    else:   
        count=count+2
        
    if count < 5:
        speech_output = "You are totally safe!"/
        "Please stay home and be safe."
        reprompt_text = speech_output    
    elif count >=5 and count <=10:
        speech_output = "You are safe but you need to be safe."/
        "Please stay home and be safe."
        reprompt_text = speech_output
    elif count > 10 and count <= 13:
        speech_output = "Yor risk level is nearly high."/
        "Please stay home and be safe."
        reprompt_text = speech_output
    else:
        speech_output = "Yor risk level too high"/
        "Please stay home and be safe."
        reprompt_text = speech_output
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))



def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Hi! Our coronavirus disease self assessment scan has been developed on the basis of guidelines from Government of India!"\
    "This interaction should not be taken as expert medical advice!"\
    "say ready if you are ready"
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
   
    # Add additional code here as needed
    pass

    

def on_launch(launch_request, session):
   
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
   
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "answerIntent":
        return answer_response()
    elif intent_name == "ageIntent":
        return age_response(intent_request)
    elif intent_name == "genderIntent":
        return gender_response(intent_request)
    elif intent_name == "bodyTempIntent":
        return body_temp_response(intent_request)    
    elif intent_name == "diseaseIntent":
        return disease_response(intent_request)
    elif intent_name == "severeDiseaseIntent":
        return severe_response(intent_request)    
    elif intent_name == "travelIntent":
        return past_response(intent_request)     
    elif intent_name == "pastIntent":
        return status_response(intent_request) 
    elif intent_name == "statusIntent":
        return final_response(intent_request)    
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
   
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])



def lambda_handler(event, context): 
   
    print("Incoming request...")

    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
