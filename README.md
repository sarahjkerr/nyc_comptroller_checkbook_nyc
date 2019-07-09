# nyc_comptroller_checkbook_nyc
Retrieve data from NYC Comptroller's Checkbook NYC API

Requests to the API must be XML sent using a post request.

This code builds the XML using ElementTree and sends it via requests.

#Example Results
<?xml version="1.0"?>
<response>
  <status>
    <result>success</result>
  </status>
  <request_criteria>
    <request>
      <type_of_data>Contracts_OGE</type_of_data>
      <records_from>1</records_from>
      <max_records>10</max_records>
      <search_criteria>
        <criteria>
          <name>status</name>
          <type>value</type>
          <value>active</value>
        </criteria>
        <criteria>
          <name>category</name>
          <type>value</type>
          <value>expense</value>
        </criteria>
      </search_criteria>
      <response_columns>
        <column>contract_id</column>
      </response_columns>
    </request>
  </request_criteria>
  <result_records>
    <record_count>2718</record_count>
    <contract_transactions>
      <transaction>
        <contract_id>CTA180120187211342</contract_id>
      </transaction>
      <transaction>
        <contract_id>CTA180120187210202</contract_id>
      </transaction>
      <transaction>
        <contract_id>CTA180120187210921</contract_id>
      </transaction>
      <transaction>
        <contract_id>CTA180120187211326</contract_id>
      </transaction>
      <transaction>
        <contract_id>CTA180120187207999</contract_id>
      </transaction>
      <transaction>
        <contract_id>CTA180120187204427</contract_id>
      </transaction>
      <transaction>
        <contract_id>CTA180120187204427</contract_id>
      </transaction>
      <transaction>
        <contract_id>CTA180120187207487</contract_id>
      </transaction>
      <transaction>
        <contract_id>CTA180120187211267</contract_id>
      </transaction>
      <transaction>
        <contract_id>CTA180120187206931</contract_id>
      </transaction>
    </contract_transactions>
  </result_records>
</response>
