import sys
sys.path.append('.')
from lambda_function import csv_lambda_handler
from lambda_function import csv_lambda_handler_local
from lambda_function import md_lambda_handler_local

event = {
    "Records": [
        {
            "s3": { 
                "bucket": {
                    "name": "example-bucket"
                },
                "object": {
                    "key": "example.csv"
                }
            }
        }
    ]
}

context = {}  # Mock the Lambda context object if needed

# Run the function with upload to s3-bucket
# response = lambda_handler(event, context)

# Run the function locally with the event
response = csv_lambda_handler_local(event, context)
# response = md_lambda_handler_local(event, context)
print(response)
