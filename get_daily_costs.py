import boto3
from datetime import datetime, timedelta
client = boto3.client('ce')

start_date = (datetime.now() - timedelta(days=4)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')
print(start_date,end_date)

response = client.get_cost_and_usage(
    TimePeriod= {
        'Start': start_date,
        'End': end_date
    },
   Granularity='DAILY',Metrics=['UnblendedCost'],
   GroupBy = [
       {
           'Type': 'DIMENSION',
            'Key': 'SERVICE'
       }
   ]
)
for item in response['ResultsByTime']:
    print(item['TimePeriod'])
    for group in item['Groups']:
        service_name = group['Keys'][0]
        cost = group['Metrics']['UnblendedCost']['Amount']
        print((f"{service_name}: ${cost}"))
        
    print('\n\n')