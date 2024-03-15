from urllib.parse import uses_query
import openai
import json
from secret_key import openai_api_key
import endpoints
openai.api_key = openai_api_key
import dummy



def get_answer(questions,chat_histories):
    messages = [{"role": "user", "content": questions},]
    functions = [
        {
            "name": "getuserprofileslist",
            "description": """Get practitioners details only this is refer by key word 'practitioner details'  
            """
        },
         {
        "name": "get_practitioner_availabilities",
        "description": """Get practitioner availabilities based on the provided input parameters key work is availability of practitioner""",
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

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",
    )
    response_message = response["choices"][0]["message"]
    if response_message.get("function_call"):
        available_functions = {
            "getuserprofileslist": endpoints.getuserprofileslist,
            "get_practitioner_availabilities":endpoints.get_practioner_availabilities
        }
        function_name = response_message["function_call"]["name"]
        function_args = json.loads(response_message["function_call"]["arguments"])
        fuction_to_call = available_functions[function_name]
        function_response = fuction_to_call(function_args)
        return function_response

    else:  
        #return dummy.get_response(questions,chat_histories)
        # return response_message["content"]
           
        return f"Sorry for the inconvience.. As i am asistant i can only give response for valid questions"
         
        