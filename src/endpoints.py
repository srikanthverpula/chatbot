import json
import requests
import header
headers=header.headers

def getuserprofileslist(param:{}): # type: ignore
    
    try:
        url ="https://qa.doctrz.in:44325/api/clinic-service/add-practitioners/getuserprofileslist/19019"
        result = requests.get(url, verify=False, headers=headers)
        result.raise_for_status()
        data = result.json()
        if not data:
            return "Sorry. Practitioners are not available."
        fullnames = [f"{entry['first_name']} {entry['last_name']}" for entry in data]
        practitioner_names = ",".join(fullnames)
        return f"Sure.These are the practitioners available :\n{practitioner_names}"
    except Exception as e:
        return f"An error occurred: {e}"

def get_practioner_availabilities(param:{}): # type: ignore
    try:
        base_url = "https://qa.doctrz.in:44325/api/clinic-service/practioner-availabilities"
        params = param
        response = requests.get(base_url,headers=headers, params=params,verify=False)
        response.raise_for_status()
        return json.dumps(response.json())
    except Exception as e:
        return f"An error occurred: {e}"
    