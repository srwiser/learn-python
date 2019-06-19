import boto3

client = boto3.client('acm')

response = client.describe_certificate(
    CertificateArn='arn:aws:acm:ap-south-1:123456789:certificate/xxxyyyxxxyyy'
)
