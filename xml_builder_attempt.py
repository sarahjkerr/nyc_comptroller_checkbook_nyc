from xml.etree import ElementTree
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring, XML

#Adds the prettify method written by Averroes -> https://gist.github.com/Averroes/6375a1cccd39fe9f2dd7
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def generate_xml(criteria_list, response_col_list, records_from, max_records_per_call):
    
    top = Element("request")
    
    type_of_data_tag = SubElement(top, "type_of_data")
    type_of_data_tag.text = "contracts"
    
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
    
    print(prettify(top))
