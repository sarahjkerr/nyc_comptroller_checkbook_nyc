#libraries
import requests
import xml.etree.ElementTree as ET

#build xml
base_url = 'https://www.checkbooknyc.com/api'

request_tag = ET.Element('request')

type_of_data = ET.SubElement(request_tag,'type_of_data')
type_of_data.text = 'Contracts_OGE'

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

response_columns = ET.SubElement(request_tag, 'response_columns')

response_col_1 = ET.SubElement(response_columns, 'column')
response_col_1.text = 'contract_id'

full_xml_request = ET.tostring(request_tag)
print(full_xml_request)

#send request
print (requests.post(base_url, data=full_xml_request).text)
