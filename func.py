import requests
import json

# Main func

url = "https://cbu.uz/ru/arkhiv-kursov-valyut/json/"

def getRate(currency):
    """For get rub, input argument is 'RUB', for usd - 'USD'"""

    currency += '/'

    response = requests.get(url+currency)
    response = response.json()

    return response[0]['Rate']

def calc(amount,currency,toSum=False):
    """Calc  currency to som, if toSum is True then calc som to currency"""

    if toSum == True:
        result =  amount / float(getRate(currency)) # Som to currency
        result = round(result,2)

        return result

    else: 
        return amount * float(getRate(currency)) # currency to Som

# For handlers

def replyCurrency(amount,currency,toSum=False):
    return (amount,currency,toSum)
