from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests, math, random
from django.template.loader import render_to_string

from .settings import STATICFILES_DIRS


def map_view(request):
    # Get the CRNS Production value from the Thingspeak API
    try:
        response_CRNS_Production = requests.get("https://api.thingspeak.com/channels/1923611/fields/1/last.txt?api_key=O9FUQR7DP5M2LD9N")
        CRNS_Production_value = round(response_CRNS_Production.json(),2)
    except Exception:
        CRNS_Production_value=0
    # Get the house 1 Production value from the Thingspeak API
    try:
        response_house_Production = requests.get("https://api.thingspeak.com/channels/370210/fields/2/last.txt?api_key=8LIB6S78T5SML76N")
        House1_Production_value = round(response_house_Production.json(),2)
    except Exception:
        House1_Production_value=0
    # Get the house 1 Consumption value from the Thingspeak API
    try:
        response_house_Production = requests.get("https://api.thingspeak.com/channels/1624196/fields/1/last.txt?api_key=N0YG2IGCAAII5X1K")
        House1_Consumption_value = round(response_house_Production.json(),2)
    except Exception:
        House1_Consumption_value=0
    # Get the house2 consumption value from the Thingspeak API
    try:
        response_Consumption = requests.get("https://api.thingspeak.com/channels/1923608/fields/1/last.txt?api_key=G6ZNMEAHDGOSRGG1")
        #House2_Consumption_value = round(response_Consumption.json(), 2)
        House2_Consumption_value = round(float(response_Consumption.text),2)
        if(math.isnan(House2_Consumption_value)):
            House2_Consumption_value=random.randint(100, 200)
        print("ggggg",response_Consumption.status_code, response_Consumption.text)
    except Exception:
        House2_Consumption_value=0

    data = {
        'coordinates': [34.83759288698608, 10.757442465621788],
        'markers': [
            {'lat': 34.83759288698608, 'lng': 10.757442465621788, 'description': f'CRNS', 'production': f'Production: {CRNS_Production_value} W','color':'blue', 'img_url': ''},
            {'lat': 34.83556071052787, 'lng': 10.758569818156426, 'description': f'House 1','production': f'Production: {House1_Production_value} W', 'consumption': f'Consumption: {House1_Consumption_value} W','color': 'blue', 'img_url': 'pictures/house1.png'},
            {'lat': 34.83433083871697, 'lng': 10.756486356497382, 'description': f'House 2', 'consumption': f'consumption: {House2_Consumption_value} W', 'color': 'red','img_url': ''},
        ]
    }
    #data1 = render_to_string('map.html', data)
    #return HttpResponse(data1)

    return render(request, 'map.html', data)


def update_measures(request):
    print("update_measures")
    """# Get the CRNS Production value from the Thingspeak API
    response_CRNS_Production = requests.get(
        "https://api.thingspeak.com/channels/1923611/fields/1/last.txt?api_key=O9FUQR7DP5M2LD9N")
    crns_Production_value = round(response_CRNS_Production.json(), 2)
    #crns_Production_value=0
    # Get the house 1 Production value from the Thingspeak API
    response_house_Production = requests.get(
        "https://api.thingspeak.com/channels/370210/fields/2/last.txt?api_key=8LIB6S78T5SML76N")
    house1_Production_value = round(response_house_Production.json(), 2)
    #house1_Production_value=0
    # Get the house 1 Consumption value from the Thingspeak API
    response_house_Production = requests.get(
        "https://api.thingspeak.com/channels/1624196/fields/1/last.txt?api_key=N0YG2IGCAAII5X1K")
    house1_Consumption_value = round(response_house_Production.json(), 2)
    #house1_Consumption_value=0
    # Get the house2 consumption value from the Thingspeak API
    #response_Consumption = requests.get(
    #    "https://api.thingspeak.com/channels/1923608/fields/1/last.txt?api_key=G6ZNMEAHDGOSRGG1")
    #house2_Consumption_value = round(response_Consumption.json(), 2)
    house2_Consumption_value=0"""
    # Get the CRNS Production value from the Thingspeak API
    try:
        response_CRNS_Production = requests.get(
            "https://api.thingspeak.com/channels/1923611/fields/1/last.txt?api_key=O9FUQR7DP5M2LD9N")
        CRNS_Production_value = round(response_CRNS_Production.json(), 2)
    except Exception:
        CRNS_Production_value = 0
    # Get the house 1 Production value from the Thingspeak API
    try:
        response_house_Production = requests.get(
            "https://api.thingspeak.com/channels/370210/fields/2/last.txt?api_key=8LIB6S78T5SML76N")
        House1_Production_value = round(response_house_Production.json(), 2)
    except Exception:
        House1_Production_value = 0
    # Get the house 1 Consumption value from the Thingspeak API
    try:
        response_house_Production = requests.get(
            "https://api.thingspeak.com/channels/1624196/fields/1/last.txt?api_key=N0YG2IGCAAII5X1K")
        House1_Consumption_value = round(response_house_Production.json(), 2)
    except Exception:
        House1_Consumption_value = 0
    # Get the house2 consumption value from the Thingspeak API
    try:
        response_Consumption = requests.get(
            "https://api.thingspeak.com/channels/1923608/fields/1/last.txt?api_key=G6ZNMEAHDGOSRGG1")
        # House2_Consumption_value = round(response_Consumption.json(), 2)
        House2_Consumption_value = round(float(response_Consumption.text), 2)
        if (math.isnan(House2_Consumption_value)):
            House2_Consumption_value = random.randint(100, 200)
        print("ggggg", response_Consumption.status_code, response_Consumption.text)
    except Exception:
        House2_Consumption_value = 0

    # generate the updated content here
    data = {
        'productionCRNS': CRNS_Production_value,
        'productionM1' : House1_Production_value,
        'consumptionM1': House1_Consumption_value,
        'consumptionM2': House2_Consumption_value

    }
    return JsonResponse(data)
contractId=0
exchangeNum=1
contracts=[["crns", "M1", 10],
           ["crns", "M2", 5],
           ["M1", "M2", 20],
           ["crns", "M1", 10]]
exchanges=[[("M1", "M2", 10)],
           [("crns", "M1", 10), ("crns", "M2", 10)],
           [("crns", "M2", 10), ("M1", "M2", 10)]]
def update_exchange(request):
    print("update_Exchange")
    global contractId
    global exchangeNum
    #initialise the dic
    data = {
        'ex1': [
            {'producer': exchanges[0][0][0],
             'consumer': exchanges[0][0][1],
             'requestedQt': exchanges[0][0][2],
             'consumedQt': 60,
             'injectedQt': 740,
             'beginTimeSlot':9}
        ],
        'ex2': [
            {'producer': exchanges[1][0][0],
             'consumer': exchanges[1][0][1],
             'requestedQt': exchanges[1][0][2],
             'consumedQt': 492,
             'injectedQt': 1711,
             'beginTimeSlot':16},
            {'producer': exchanges[1][1][0],
             'consumer': exchanges[1][1][1],
             'requestedQt': exchanges[1][1][2],
             'consumedQt': 230,
             'injectedQt': 1021,
             'beginTimeSlot':16}
            ],

        'ex3': [
        {'producer': exchanges[2][0][0],
         'consumer': exchanges[2][0][1],
         'requestedQt': exchanges[2][0][2],
         'consumedQt': 45,
         'injectedQt': 5500,
         'beginTimeSlot': 15
         },
            {'producer': exchanges[2][1][0],
             'consumer': exchanges[2][1][1],
             'requestedQt': exchanges[2][1][2],
             'consumedQt': 45,
             'injectedQt': 1500,
             'beginTimeSlot': 15
             }
           ]
    }
    # generate the updated content here
    """data = {
        'ex1': [
            {'producer': contracts[contractId][0],
            'consumer' : contracts[contractId][1],
            'quantity': contracts[contractId][2]}
        ]
    }"""
    if contractId >= len(exchanges):
        contractId = 1
    else:
        contractId += 1
    return JsonResponse(data)