#libraries
import requests
import xml.etree.ElementTree as ET
import pandas as pd

#load organization dataframe and prep search list
orgs = pd.DataFrame('FILEPATH')
orgs_list = list(orgs['company_name'])

#create xml builder function
base_url = 'https://www.checkbooknyc.com/api'

def build_xml(x):
    xml_request_list = []
    
    for item in x:
        request_tag = ET.Element('request')
    
        type_of_data = ET.SubElement(request_tag,'type_of_data')
        type_of_data.text = 'Contracts'

        records_from = ET.SubElement(request_tag, 'records_from')
        records_from.text = '1'

        max_records = ET.SubElement(request_tag, 'max_records')
        max_records.text = '10'

        search_criteria = ET.SubElement(request_tag, 'search_criteria')

        criteria_1 = ET.SubElement(search_criteria, 'criteria')

        name_1 = ET.SubElement(criteria_1, 'name')
        name_1.text = 'status'

        type_1 = ET.SubElement(criteria_1, 'type')
        type_1.text = 'value'

        value_1 = ET.SubElement(criteria_1, 'value')      
        value_1.text = 'active'
        
        criteria_2 = ET.SubElement(search_criteria, 'criteria')

        name_2 = ET.SubElement(criteria_2, 'name')
        name_2.text = 'category'

        type_2 = ET.SubElement(criteria_2, 'type')
        type_2.text = 'value'

        value_2 = ET.SubElement(criteria_2, 'value')
        value_2.text = 'expense'
        
        criteria_3 = ET.SubElement(search_criteria, 'criteria')
        
        name_3 = ET.SubElement(criteria_3, 'name')
        name_3.text = 'prime_vendor'
        
        type_3 = ET.SubElement(criteria_3, 'type')
        type_3.text = 'value'
        
        value_3 = ET.SubElement(criteria_3, 'value')
        value_3.text = item
        
        criteria_4 = ET.SubElement(search_criteria, 'criteria')
        
        name_4 = ET.SubElement(criteria_4, 'name')
        name_4.text = 'fiscal_year'
        
        type_4 = ET.SubElement(criteria_4, 'type')
        type_4.text = 'value'
        
        value_4 = ET.SubElement(criteria_4, 'value')
        value_4.text = '2019'

        response_columns = ET.SubElement(request_tag, 'response_columns')
        
        response_col_1 = ET.SubElement(response_columns, 'column')
        response_col_1.text = 'prime_contract_id'
        
        response_col_2 = ET.SubElement(response_columns, 'column')
        response_col_2.text = 'prime_vendor'
        
        response_col_3 = ET.SubElement(response_columns, 'column')
        response_col_3.text = 'prime_contract_purpose'
        
        response_col_4 = ET.SubElement(response_columns, 'column')
        response_col_4.text = 'prime_contract_original_amount'
        
        response_col_5 = ET.SubElement(response_columns, 'column')
        response_col_5.text = 'prime_contract_start_date'
        
        response_col_6 = ET.SubElement(response_columns, 'column')
        response_col_6.text = 'prime_contract_end_date'
        
        response_col_7 = ET.SubElement(response_columns, 'column')
        response_col_7.text = 'prime_contracting_agency'
        
        response_col_8 = ET.SubElement(response_columns, 'column')
        response_col_8.text = 'prime_contract_type'
        
        response_col_9 = ET.SubElement(response_columns, 'column')
        response_col_9.text = 'prime_contract_industry'
        
        full_xml_request = ET.tostring(request_tag)
        
        xml_request_list.append(full_xml_request)
        
#create and post xml
build_xml(orgs_list)

for item in xml_request_list:
  print (requests.post(base_url, data=item).text)
