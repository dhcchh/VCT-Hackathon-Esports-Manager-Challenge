import csv
import json
import boto3
import os
import glob
import sys
import json
from langchain_text_splitters import MarkdownHeaderTextSplitter
import os 
import pandas as pd 

s3_client = boto3.client('s3')

def csv_lambda_handler(event, context):
    # Iterate through all records (in case multiple files are uploaded)
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        # Get the CSV file from S3
        try:
            response = s3_client.get_object(Bucket=bucket, Key=key)
            content = response['Body'].read().decode('utf-8').splitlines()
        except Exception as e:
            print(f"Error fetching file {key} from S3: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error processing CSV file {key}')
            }
        
        # Read the CSV file row by row
        reader = csv.reader(content)
        headers = next(reader)
        
        for row in reader:
            process_row(headers, row)  # Call the processing function for each row
    
    return {
        'statusCode': 200,
        'body': json.dumps('CSV files processed successfully!')
    }

def csv_lambda_handler_local(event, context):
    league_dict = {'gc': 'Game Changers', 'intl': 'International', 'challengers': 'Challengers'}
    region_dict = {'pacific': 'Pacific', 'emea': 'EMEA', 'china': 'China', 'americas': 'Americas'}
    # Simulate reading the file from local storage instead of S3
    file_dir = 's3-bucket/csv/'
    csv_files = glob.glob(os.path.join(file_dir, '*.csv'))
    processed_data = \
    {
        "Leagues": {
            "International": {
                "Regions": {
                    "Americas": {
                    },
                    "Pacific": {
                    },
                    "China": {
                    },
                    "EMEA": {
                    }
                }

            },
            "Challengers": {
                "Regions": {
                    "Americas": {
                        "Sub Regions": {
                        }
                    },
                    "Pacific": {
                        "Sub Regions": {
                        }
                    },
                    "China": {
                    },
                    "EMEA": {
                        "Sub Regions": {
                        }
                    }
                }
            },
            "Game Changers": {
                "Regions": {
                    "Americas": {
                        "Sub Regions": {
                        }
                    },
                    "Pacific": {
                    },
                    "China": {
                    },
                    "EMEA": {
                    }
                }
            }
        }
    }
    for csv_file in csv_files:
        try:
            # Instead of S3, read the CSV from your local directory
            # sample file name = league_region_subregion.csv or league_region.csv for international
            filename = os.path.splitext(os.path.basename(csv_file))[0]
            name_list = filename.split('_')
            region = region_dict[name_list[1]]
            league_pre = name_list[0]
            if len(name_list) == 3:
                sub_region = name_list[2]
            league = league_dict[league_pre]
            with open(csv_file, mode='r') as file:
                content = file.read().splitlines()
        except Exception as e:
            print(f"Error fetching file locally: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps('Error processing CSV file')
            }
        
        # Read the CSV file row by row
        reader = csv.reader(content)
        headers = next(reader)  # Get the headers from the first row

        processed_players = []
        for row in reader:
            processed_row = process_row(headers, row)  # Process each row, each row is a player
            processed_players.append(processed_row)

        player_dict = {"Players": processed_players}
        if league == 'International':
            processed_data['Leagues'][league]['Regions'][region] = player_dict
        elif league == 'Challengers':
            if region == 'China': 
                processed_data['Leagues'][league]['Regions'][region] = player_dict
            else:
                processed_data['Leagues'][league]['Regions'][region]['Sub Regions'][sub_region] = player_dict
        elif league == 'Game Changers':
            if region == 'Americas':
                processed_data['Leagues'][league]['Regions'][region]['Sub Regions'][sub_region] = player_dict
            else:
                processed_data['Leagues'][league]['Regions'][region] = player_dict
        
    csv_save_json_locally(processed_data, 's3-bucket/json/metadata.json')

    return {
        'statusCode': 200,
        'body': json.dumps('CSV processed successfully!')
    }

def md_lambda_handler_local(event, context):
    # Simulate reading the file from local storage instead of S3
    file_dir = 's3-bucket/md/'
    md_files = glob.glob(os.path.join(file_dir, '*.md'))
    for md_file in md_files:
        try:
            # Instead of S3, read the CSV from your local directory
            filename = os.path.splitext(os.path.basename(md_file))[0]
            with open(md_file, mode='r') as file:
                content = file.read()
        except Exception as e:
            print(f"Error fetching file locally: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps('Error processing CSV file')
            }

        md_chunks = process_text(content)

        # Print chunks 
        for i, chunk in enumerate(md_chunks):
            print(f"Chunk {i+1}:\n")
            print(chunk.page_content)  
            print("\n---\n")  
        # Save chunks to local json files or upload them to S3
        csv_save_json_locally(md_chunks, f's3-bucket/json/{filename}_chunks.json')

def process_text(content):
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
        ]
    # Split the chunks 
    md_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on, 
        strip_headers=False
    )
    md_chunks = md_splitter.split_text(content)
    return md_chunks


def process_row(headers, row):
    # Match each column header to the corresponding row value
    row_dict = {headers[i]: row[i] for i in range(len(headers))}  # Create a key-value pair for each column
    
    # Print the dictionary (for debugging purposes)
    # print(f'Processed Row: {row_dict}')
    
    # Further processing logic can be added here
    # e.g., Upload each row or processed data to another S3 bucket, database, etc.
    # upload_chunk_to_s3(row_dict)
    return row_dict

def upload_chunk_to_s3(chunk_data):
    # Convert the dictionary to a JSON string and then to bytes
    chunk_json = json.dumps(chunk_data)  # Convert dict to JSON string
    chunk_bytes = chunk_json.encode('utf-8')  # Convert JSON string to bytes
    
    # Upload to S3 using the bytes
    s3_client.put_object(Bucket='your-bucket-name', Key='chunk.json', Body=chunk_bytes)

def csv_save_json_locally(data, filename):
    try:
        # Convert data to JSON and save to the local file
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving JSON to local file: {e}")

def md_save_json_locally(chunks, filename):
    try:
        # Convert the chunks into JSON format
        chunk_data = [{"chunk": i+1, "content": chunk.page_content} for i, chunk in enumerate(chunks)]
        
        # Save the JSON data to a file
        with open(filename, 'w') as json_file:
            json.dump(chunk_data, json_file, indent=4)
        
        print(f"Chunks saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving JSON to local file: {e}")