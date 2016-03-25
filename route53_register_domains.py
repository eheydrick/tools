#!/usr/bin/python
#
# Bulk register domains with Route53
#
import boto3

client = boto3.client('route53domains', region_name='us-east-1')

domains = [
    'example.com',
    'example.org',
    'example.net'
]

contact_details = {
    'ContactType': 'COMPANY',
    'FirstName': 'Head',
    'LastName': 'Honcho',
    'OrganizationName': 'Example, Inc.',
    'AddressLine1': '111 1st Ave N',
    'City': 'MyCity',
    'State': 'WA',
    'CountryCode': 'US',
    'ZipCode': '98104',
    'PhoneNumber': '+1.2061111111',
    'Email': 'info@example.com'
}


def check_availability(domain):
    check = client.check_domain_availability(DomainName=domain)
    if check['Availability'] == 'AVAILABLE':
        return True
    else:
        return False


def register_domain(domain):
    response = client.register_domain(
        DomainName=domain,
        DurationInYears=1,
        AutoRenew=True,
        AdminContact=contact_details,
        RegistrantContact=contact_details,
        TechContact=contact_details
    )
    return response['OperationId']


for domain in domains:
    available = check_availability(domain)
    if available:
        print "Registering %s" % domain
        operation_id = register_domain(domain)
        print operation_id
    else:
        print "%s is not available" % domain


