import os
from openai import OpenAI
import json
import endpoints

def get_answer(questions,chat_histories):
    messages = [{"role": "user", "content": questions},]
    client = OpenAI(
        
        api_key=os.getenv("OPENAI_API_KEY")
    )
    messages = [{"role": "user", "content": questions}]
    function = [
            {
                "name": "getuserprofileslist",
                "description": """its giving information about organization practitioner information  
                """
            },
            {
            "name": "get_practitioner_availabilities",
            "description": """Get practitioner availabilities based on the provided input parameters""",
            "parameters": {
                "type": "object",
                "properties": {
                
                    "addl_no_of_patients_in_slot_min": {
                        "type": "integer",
                        "description": "Minimum additional number of patients in a slot",
                    },
                    "addl_no_of_patients_in_slot_max": {
                        "type": "integer",
                        "description": "Maximum additional number of patients in a slot",
                    },
                    "date_created_min": {
                        "type": "string",
                        "description": "Minimum creation date",
                    },
                    "date_created_max": {
                        "type": "string",
                        "description": "Maximum creation date",
                    },
                    "from_time_min": {
                        "type": "integer",
                        "description": "Minimum from time",
                    },
                    "from_time_max": {
                        "type": "integer",
                        "description": "Maximum from time",
                    },
                    "last_updated_min": {
                        "type": "string",
                        "description": "Minimum last updated date",
                    },
                    "last_updated_max": {
                        "type": "string",
                        "description": "Maximum last updated date",
                    },
                    "no_of_patients_in_slot_min": {
                        "type": "integer",
                        "description": "Minimum number of patients in a slot",
                    },
                    "no_of_patients_in_slot_max": {
                        "type": "integer",
                        "description": "Maximum number of patients in a slot",
                    },
                    "org_branch_id_min": {
                        "type": "integer",
                        "description": "Minimum organization branch ID",
                    },
                    "org_branch_id_max": {
                        "type": "integer",
                        "description": "Maximum organization branch ID",
                    },
                    "slot_duration_min": {
                        "type": "integer",
                        "description": "Minimum slot duration",
                    },
                    "slot_duration_max": {
                        "type": "integer",
                        "description": "Maximum slot duration",
                    },
                    "to_time_min": {
                        "type": "integer",
                        "description": "Minimum to time",
                    },
                    "to_time_max": {
                        "type": "integer",
                        "description": "Maximum to time",
                    },
                    "user_profile_id_min": {
                        "type": "integer",
                        "description": "Minimum user profile ID",
                    },
                    "user_profile_id_max": {
                        "type": "integer",
                        "description": "Maximum user profile ID",
                    },
                    "friday": {
                        "type": "boolean",
                        "description": "Friday availability",
                    },
                    "monday": {
                        "type": "boolean",
                        "description": "Monday availability",
                    },
                    "saturday": {
                        "type": "boolean",
                        "description": "Saturday is availabe in promp this will true",
                    },
                    "sunday": {
                        "type": "boolean",
                        "description": "Sunday availability is selected then this value need to pass as true",
                    },
                    "thursday": {
                        "type": "boolean",
                        "description": "Thursday availability",
                    },
                    "tuesday": {
                        "type": "boolean",
                        "description": "Tuesday availability",
                    },
                    "wednesday": {
                        "type": "boolean",
                        "description": "Wednesday availability",
                    },
                    "meeting_type_min": {
                        "type": "integer",
                        "description": "Minimum meeting type",
                    },
                    "meeting_type_max": {
                        "type": "integer",
                        "description": "Maximum meeting type",
                    },
                },
            },
        },
        ]
    response = client.chat.completions.create(
        messages=messages,
        functions=function,
        function_call="auto",
        model="gpt-3.5-turbo",
    )
    if response.choices:
        choice = response.choices[0]

        if choice.finish_reason == 'function_call' and choice.message.function_call:
            function_call = choice.message.function_call
            function_name = function_call.name
            function_args = json.loads(function_call.arguments)
            available_functions = {
                "getuserprofileslist": endpoints.getuserprofileslist,
                "get_practitioner_availabilities":endpoints.get_practioner_availabilities
            }

            if function_name in available_functions:
                function_to_call = available_functions[function_name]
                function_response = function_to_call(function_args)
                return function_response
            else:
                return "Error: Function '{}' not found".format(function_name)
        else:
           
            #return dummy.get_response(questions,chat_histories)
            # return response_message["content"]
           
            return f"Sorry for the inconvience.. As i am asistant i can only give response for valid questions"
    else:
        return "No response received"
         
        