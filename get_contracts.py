from xml.etree import ElementTree
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring, XML
import requests

search_dict = {'criteria1' : ['status', 'value', 'active'], 'criteria2': ['category', 'value', 'expense']}
response_cols = ['prime_contract_id', 'prime_vendor', 'document_code']
base_url = "https://www.checkbooknyc.com/api"

def generate_xml(criteria_list, response_col_list, records_from, max_records_per_call):
    
    top = Element("request")
    
    type_of_data_tag = SubElement(top, "type_of_data")
    type_of_data_tag.text = "Contracts"
    
    records_from_tag = SubElement(top, "records_from")
    records_from_tag.text = str(records_from)
    
    max_records_tag = SubElement(top, "max_records")
    max_records_tag.text = str(max_records_per_call)
    
    search_criteria_parent = SubElement(top, "search_criteria")
    search_criteria_list = []
    
    response_col_parent = SubElement(top, "response_columns")
    response_cols = []
    
    for key in search_dict:
        
        value = search_dict[key]
        
        name = "<name>" + value[0] + "</name>"
        type_of = "<type>" + value[1] + "</type>"
        value = "<value>" + value[2] + "</value>"
        
        search_criteria_request = "<criteria>" + name + type_of + value + "</criteria>"
        
        all_search_criteria = XML(search_criteria_request)
        
        search_criteria_list.append(all_search_criteria)
        
    for item in response_col_list:
        
        response_col_request = XML("<column>" + item + "</column>")
        
        response_cols.append(response_col_request)
        
    search_criteria_parent.extend(search_criteria_list)
    response_col_parent.extend(response_cols)
    
    full_xml_request = tostring(top)

    return full_xml_request

def get_contracts(total_records, max_records_per_call, criteria_list, response_col_list):

  total_records = total_records
  max_records_per_call = max_records_per_call
  records_pulled = 1
  response_list = []

  while records_pulled < total_records:
    response = requests.post(base_url, data = generate_xml(search_dict, response_col_list, records_pulled, max_records_per_call))
    response_list.append(response.text)
    ended_on = (records_pulled + max_records_per_call) -1
    output = f"Fetching {max_records_per_call} results from {records_pulled} to {ended_on}"
    records_pulled += max_records_per_call

    print(output)

  return response_list

def unpack_response(response_list, response_col_list):
  output_list = []

  for response in response_list:
    thing = get_elem_data(response_col_list, response)

    output_of_thing = split_list(thing, response_col_list)

    output_list.append(output_of_thing)

  return output_list

#Gets the response data for an instance of a response object
def get_elem_data(response_col_list, PLACEHOLDER):
  
  child_elems = []

  for item in response_cols:
    argument = ".//" + item
    for i in ElementTree.fromstring(PLACEHOLDER).findall(argument):
      child_elems.append(i.text)
  
  return child_elems

#Splits the response data into a dict
def split_list(child_elems, response_col_list):

  list_of_lists = []

  response_col_list = response_col_list

  break_pt = int(len(child_elems)/len(response_col_list))

  for i in range(0, len(child_elems), break_pt):
    list_of_lists.append(child_elems[i : i + break_pt])

  return dict(zip(response_cols, list_of_lists))
