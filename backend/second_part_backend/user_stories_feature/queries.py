#Standard libraries
import os 

#Python dotenv
from dotenv import load_dotenv

#Google cloud
from google.cloud import bigquery

load_dotenv()

google_application_credentials = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])


def visual_query_builder(country_code, series_code,year, value):
    """
    Visual Query Builder

    This function executes a SQL query for BigQuery on multiple tables in the 'world_bank_intl_education' dataset of BigQuery's public data.
    The tables include 'country_series_definitions', 'international_education', 'series_summary', and 'country_summary'. The query retrieves counts of specified fields from these tables based on certain conditions.

    Parameters:
        country_code (str): The country code to be used in the query conditions.
        series_code (str): The series code to be used in the query conditions.
        year (int): The year to be used in the query conditions.
        value (float): The value to be used in the query conditions.

    Returns:
        google.cloud.bigquery.table.RowIterator: An iterator over the query result rows.
    """
    client = bigquery.Client()
    query = f'''
            SELECT 
                'country_series_definitions' as table_name,
                COUNT(csd.country_code) as country_count,
                COUNT(csd.series_code) as series_count,
                NULL as year_count,
                NULL as value_count
            FROM 
                bigquery-public-data.world_bank_intl_education.country_series_definitions as csd
            WHERE 
                csd.country_code = @country_code AND csd.series_code = @series_code
            UNION ALL
            SELECT 
                'international_education' as table_name,
                COUNT(ie.country_code) as country_count,
                NULL as series_count,
                COUNT(ie.year) as year_count,
                COUNT(ie.value) as value_count
            FROM 
                bigquery-public-data.world_bank_intl_education.international_education as ie
            WHERE 
                ie.country_code = @country_code
            UNION ALL
            SELECT 
                'series_summary' as table_name,
                NULL as country_count,
                COUNT(ss.series_code) as series_count,
                NULL as year_count,
                NULL as value_count
            FROM 
                bigquery-public-data.world_bank_intl_education.series_summary
 as ss
            WHERE 
                ss.series_code = @series_code
            UNION ALL
            SELECT 
                'country_summary' as table_name,
                COUNT(cs.country_code) as country_count,
                NULL as series_count,
                NULL as year_count,
                NULL as value_count
            FROM 
                bigquery-public-data.world_bank_intl_education.country_summary
 as cs
            WHERE 
                cs.country_code = @country_code
        '''
    query_params = [
        bigquery.ScalarQueryParameter('country_code', 'STRING', country_code),
        bigquery.ScalarQueryParameter('series_code', 'STRING', series_code),
        bigquery.ScalarQueryParameter('year', 'INT64', int(year)),
        bigquery.ScalarQueryParameter('value', 'FLOAT64', float(value)),
    ]
    job_config = bigquery.QueryJobConfig()
    job_config.query_parameters = query_params
    query_job = client.query(query, job_config=job_config)
    rows = query_job.result()
    return rows
    
    