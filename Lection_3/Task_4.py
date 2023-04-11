import requests

print('Go check out working web site')

ResponseCode = requests.get(input('Please enter web-link: '))

print('OK' if ResponseCode.status_code in (200, 302) else 'FAIL')
