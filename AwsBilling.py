import boto3
import json

client = boto3.client('ce')

response_dict = client.get_cost_and_usage(
    TimePeriod={
        'Start': '2019-04-01',
        'End': '2019-04-24'
    },
    Granularity='MONTHLY',
    Filter =  {"And": [
        {"Dimensions": {
            "Key": "INSTANCE_TYPE",
            "Values": ["c4.xlarge"]
        }
        },
        {"Tags": {
            "Key": "user:Team",
            "Values": ["gst"]
        }
        }
    ]
    },
    Metrics=[
        'BlendedCost',
        'UsageQuantity'
    ],
    GroupBy=[
        {
            'Type': 'TAG',
            'Key': 'user:Application'
        },
        {
            'Type': 'DIMENSION',
            'Key': 'INSTANCE_TYPE'
        }
    ]
    # NextPageToken='string'
)

print(response_dict)
with open('response.json', 'w') as fp:
    json.dump(response_dict, fp, sort_keys=True, indent=4)