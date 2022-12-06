# putting code within the body of a try block adds a mechanism around that code that allows us to detect errors (which are called exceptions) and decide what to do if they happen

# try:
#     fh = open('text.txt')
#     for line in fh:
#         print(line.strip())
# finally:
#     fh.close()

# Open files using context managers
# with open('text.txt') as fh:
#     for line in fh:
#         print(line.strip())

# files/existence.py
# import os
# filename = 'text.txt'
# path = os.path.dirname(os.path.abspath(filename))
# print(os.path.isfile(filename))  # True
# print(os.path.isdir(path))  # True
# print(path)  # /Users/fab/srv/lpp/ch7/files

# import json

# info = {
#     'full_name': 'Sherlock Holmes',
#     'address': {
#         'street': '221B Baker St',
#         'zip': 'NW1 6XE',
#         'city': 'London',
#         'country': 'UK',
# }}
# # json.dumps py => json
# # json.loads json => py
# print(json.dumps(info, indent=2, sort_keys=True))