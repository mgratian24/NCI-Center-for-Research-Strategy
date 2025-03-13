"""
This module was developed by Margaret Gratian with support from the NIH RePORTER team.

This module has functions for requesting data from the RePORTER API and getting back results structured as a Pandas DataFrame. This module is not comprehensive of all RePORTER API functionality and instead can be thought of as a starting point for further development. Some comments throughout indicate opportunities for improvements.

"""

import requests
import itertools
import pandas as pd
import json
import math

# Set the endpoint url of the API
url = "https://api.reporter.nih.gov/v2/projects/search"

# Set the headers
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

def get_total_records(data):
    """
    Returns the number of available records in RePORTER for a user specified payload.
    
    Parameters:
    -----------
    data: dictionary
        A dictionary of the user specified payload criteria, 
        e.g., {"agencies":["NCI"], "fiscal_years"=[2021, 2022, 2023]}. 
        This will be dumped to json for use in the request.
    
    Returns:
    --------
    total_records: int
        The number of records available for the given payload.
    """
    # Request data from API
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Save data
    response_json = response.json()

    # Print metadata 
    # print(response_json['meta'])

    # Get total records from json
    total_records = response_json['meta']['total']

    return total_records

def request_by_user_payload(data):
    """
    Request data from the RePORTER API based on a user defined payload and return as a Pandas DataFrame. 
    This function will also print the number of records expected.
    
    Parameters:
    -----------
    data: dictionary
        A dictionary of the user specified payload criteria,
        e.g., {"agencies":["NCI"], "fiscal_years"=[2021, 2022, 2023]}.
        This will be dumped to json for use in the request.
    
    Returns:
    --------
    results_df: Pandas DataFrame
        The API request's response, in tabular format.
    """  
    # Get total records associated with this payload to determine
    # how many loops are necessary 
    total_records = get_total_records(data)

    # Set limit to 500 as a backup for the user 
    # Could modify this to only set the limit if the user has not set one 
    data["limit"] = 500

    # Create the loop range 
    # 500 is the limit per request 
    loop_range = math.ceil(total_records/500) + 1 

    meta = []
    results = []
    for i in range(loop_range):
        # Update the offset in data each time 
        data["offset"] = 500*i

        # Request the data 
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response_json = response.json()
    
        if len(response_json) == 1:
            break
        else:
            if response_json['results'] != []:
                meta.append(response_json['meta'])
                results.append(response_json['results'])
            else:
                break
    
    # Before reading json into df, need to flattern the results
    # results is a list of lists, where the inner list contains the comma separated json records 
    # This flattening is somewhat simplistic, there are more nested jsons that we could deal with later
    flattened_results = list(itertools.chain(*results))

    # Save flattened_results to a df
    results_df = pd.json_normalize(flattened_results)
    #print(results_df.head())

    # return the df of results
    return(results_df)


def request_nci_awards_by_year_and_activity_codes(years, activity_codes):
    """
    Request NCI administered awards from the RePORTER API based on user specified
    fiscal years and activity codes. 
    This function will also print the number of records expected.
    
    Parameters:
    -----------
    years: list of ints
        A list of ints representing the fiscal years to request. 
        Fiscal years should be formatted as YYYY, e.g., 2023.
    activity codes: list of strings
        A list of strings representing the three letter activity codes to request, 
        e.g., ["R01", "R37"]
    
    Returns:
    --------
    results_df: Pandas DataFrame
        The API request's response, in tabular format.
        
    """
    # Create the payload 
    data = {
            "criteria":
            {
                "fiscal_years": years,
                "agencies":["NCI"], 
                "activity_codes": activity_codes, 
            },
            "limit":500,
            "sort_field":"project_start_date",
            "sort_order":"desc"
        }
    
    # Get total records associated with this payload to determine
    # how many loops are necessary 
    total_records = get_total_records(data)
    print(total_records)

    # Create the loop range 
    # 500 is the limit per request 
    loop_range = math.ceil(total_records/500) + 1 

    meta = []
    results = []
    for i in range(loop_range):

        # Update the offset in data each time 
        data["offset"] = 500*i

        # Request the data 
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response_json = response.json()
    
        if len(response_json) == 1:
            break
        else:
            if response_json['results'] != []:
                meta.append(response_json['meta'])
                results.append(response_json['results'])
            else:
                break
    
    # Before reading json into df, need to flattern the results
    # results is a list of lists, where the inner list contains the comma separated json records 
    # This flattening is somewhat simplistic, there are more nested jsons that we should deal with later
    flattened_results = list(itertools.chain(*results))

    # Save flattened_results to a df
    results_df = pd.json_normalize(flattened_results)
    #print(results_df.head())

    # return the df of results
    return(results_df)

def request_nci_awards_by_year_activity_codes_and_ppids(years, activity_codes, ppids):
    """
    Request NCI administered awards from the RePORTER API based on user specified
    fiscal years, activity codes, and NIH PPIDs. 
    This function will also print the number of records expected.
    
    Parameters:
    -----------
    years: list of ints
        A list of ints representing the fiscal years to request. 
        Fiscal years should be formatted as YYYY, e.g., 2023.
    activity codes: list of strings
        A list of strings representing the three letter activity codes to request, 
        e.g., ["R01", "R37"]
    ppids: list of ints
        A list of ints representing NIH PI Profile IDs (PPIDs) to request, 
        e.g., [9999999, 9999991]
    
    Returns:
    --------
    results_df: Pandas DataFrame
        The API request's response, in tabular format.
        
    """
    # Create the payload 
    data = {
            "criteria":
            {
                "fiscal_years": years,
                "agencies":["NCI"], 
                "activity_codes": activity_codes, 
                "pi_profile_ids" : ppids
            },
            "limit":500,
            "sort_field":"project_start_date",
            "sort_order":"desc"
        }
    
    # Get total records associated with this payload to determine
    # how many loops are necessary 
    total_records = get_total_records(data)
    print(total_records)

    # Create the loop range 
    # 500 is the limit per request 
    loop_range = math.ceil(total_records/500) + 1 

    meta = []
    results = []
    for i in range(loop_range):

        # Update the offset in data each time 
        data["offset"] = 500*i

        # Request the data 
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response_json = response.json()
    
        if len(response_json) == 1:
            break
        else:
            if response_json['results'] != []:
                meta.append(response_json['meta'])
                results.append(response_json['results'])
            else:
                break
    
    # Before reading json into df, need to flattern the results
    # results is a list of lists, where the inner list contains the comma separated json records 
    # This flattening is somewhat simplistic, there are more nested jsons that we should deal with later
    flattened_results = list(itertools.chain(*results))

    # Save flattened_results to a df
    results_df = pd.json_normalize(flattened_results)
    #print(results_df.head())

    # return the df of results
    return(results_df)
