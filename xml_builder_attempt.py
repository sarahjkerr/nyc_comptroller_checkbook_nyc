import xml.etree.cElementTree as ET

def search_criteria(search_fields_list):
    
    keep_count = 1
    
    criteria_master_str = "search_criteria = ET.SubElement(request_tag, 'search_criteria') "
    
    for key in search_fields_list:
        
        value = search_fields_list[key]
        
        criteria_no = "criteria_" + str(keep_count)
        
        criteria_string = criteria_no + " = ET.SubElement(search_criteria, 'criteria')"
        
        name_of = "name_" + str(keep_count) + " = ET.SubElement(" + criteria_no + ", 'name')"
        name_text = "name_" + str(keep_count) + ".text = '" + key + "'"
        
        type_of = "type_" + str(keep_count) + " = ET.SubElement(" + criteria_no + ", 'name')"
        type_text = "type_" + str(keep_count) + ".text = 'value'"
        
        value_of = "value_" + str(keep_count) + " = ET.SubElement(" + criteria_no + ", 'name')"
        value_text = "value_" + str(keep_count) + ".text = '" + value + "'"
        
        keep_count += 1
        
        criteria_xml = criteria_string + ' ' + name_of +  ' ' + name_text +  ' ' + type_of +  ' ' + type_text + ' ' + value_of +  ' ' + value_text
    
        criteria_master_str += criteria_xml
        
    return criteria_master_str

def response_columns(response_col_list):
       
    keep_count = 1
    
    col_master_str = "response_columns = ET.SubElement(request_tag, 'response_columns') "
    
    for item in response_col_list:
        
        response_col_no = "response_col_" + str(keep_count)
        
        response_col_str = response_col_no + " = ET.SubElement(response_columns, 'column')"
        response_col_text = response_col_no + ".text = " + item
        
        response_col_xml = response_col_str + ' ' + response_col_text
        
        col_master_str += response_col_xml
        
        keep_count += 1
        
    return col_master_str
