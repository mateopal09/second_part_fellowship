#Standard libraries
import os 

#Google cloud
from google.cloud import bigquery


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:\\Ver + Fellowship\\mateo_cloud_service.json'

def visual_query_builder(country_code, series_code,year, value):
    """
        Visual Query Builder

        This function executes a SQL query on the 'country_series_definitions' table
        in the 'world_bank_intl_education' dataset of BigQuery's public data.

        Returns:
            google.cloud.bigquery.table.RowIterator: An iterator over the query result rows.
    """
    client = bigquery.Client()
    query = f'''
            SELECT {country_code}, {series_code}, {year}, {value}
            FROM `bigquery-public-data.world_bank_intl_education.country_series_definitions` as csd
            JOIN `bigquery-public-data.world_bank_intl_education.country_summary` as cs
            ON csd.country_code = cs.country_code
            JOIN `bigquery-public-data.world_bank_intl_education.series_summary` as ss
            ON csd.series_code = ss.series_code
            '''
    query_job = client.query(query)
    rows = query_job.result()
    return rows

    
    