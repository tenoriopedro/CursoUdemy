import re


texto ='''
ONLINE 192.168.0.1 GHIJK activate
OFFLINE 192.168.0.2 GHIJK inactivate
OFFLINE 192.168.0.3 GHIJK activate
ONLINE 192.168.0.4 GHIJK activate
ONLINE 192.168.0.5 GHIJK inactivate
OFFLINE 192.168.0.6 GHIJK activate
'''

# Positive lookhead
# print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=activate)', texto))
# Negative lookhead
# print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!activate)', texto))
# print(re.findall(r'(?=.*[^in]activate).+', texto))

# Positive lookbehind
print(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# Negative lookbehind
print(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
