"""
import os 
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:\\Ver + Fellowship\\mateo_cloud_service.json'

def run_my_query():
    client = bigquery.Client()
    query = '''
            SELECT COUNT(*)  FROM `bigquery-public-data.world_bank_intl_education.international_education`
            '''
    query_job = client.query(query)
    rows = query_job.result()
    return rows
"""
#This was an example to see if the Bigquery is working on Django

import os 
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:\\Ver + Fellowship\\mateo_cloud_service.json'

def visual_query_builder():
    client = bigquery.Client()
    query = '''
            SELECT country_code
            FROM `bigquery-public-data.world_bank_intl_education.country_series_definitions`
            LIMIT 5
            '''
    query_job = client.query(query)
    rows = query_job.result()
    return rows

    
    