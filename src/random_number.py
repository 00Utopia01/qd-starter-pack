#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#

import requests

response = requests.get('https://www.random.org/integers/?num=5&min=1&max=6&col=1&base=10&format=plain&rnd=new')

print(f"random number is:{(response.text.strip())[0]}")