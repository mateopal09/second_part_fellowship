#Standard libraries
import os 

#Google cloud
from google.cloud import bigquery


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:\\Ver + Fellowship\\mateo_cloud_service.json'

def visual_query_builder():
    """
        Visual Query Builder

        This function executes a SQL query on the 'country_series_definitions' table
        in the 'world_bank_intl_education' dataset of BigQuery's public data.

        Returns:
            google.cloud.bigquery.table.RowIterator: An iterator over the query result rows.
    """
    client = bigquery.Client()
    query = '''
            SELECT country_code
            FROM `bigquery-public-data.world_bank_intl_education.country_series_definitions`
            LIMIT 5
            '''
    query_job = client.query(query)
    rows = query_job.result()
    return rows

    
    