import os

key_name='RIOT_API_KEY'
string=os.environ.get(key_name)
print(string)