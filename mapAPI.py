# Willy Saronamihardja 80408898.  ICS 32.  Project 3.

import urllib.parse
import urllib.request
import json
import output


consumer_key = 'IdtV0hlz0YkkAb6qPVZPbrasnqe1HtAD'

base_mapquest_elevation_url = 'http://open.mapquestapi.com/elevation/v1'

base_mapquest_url = 'http://open.mapquestapi.com/directions/v2'




def obtain_location_amount() -> int:
    '''
    Obtains amount of how many locations the trip will consist of.
    '''
    return int(input())



def obtain_location_areas(amount: int) -> list:
    '''
    Takes the amount of locations (including and
    starting with the starting location) and asks for
    destinations and adds them to a list.
    '''
    list_of_places = []
    
    for place in range(amount):
        location = input()
        list_of_places.append(location)
        
    return list_of_places

        


def build_search_url(list_of_locations: list) -> str:
    '''
    Builds on base url with a given "from" location and a given "to" location.
    Takes in two places.
    '''
    list_of_url = []
    
    for place in range(len(list_of_locations) - 1):
        from_location = list_of_locations[place]
        to_location = list_of_locations[place+1]
        
        query_parameters = [
            ('key', consumer_key), ('from', from_location),
            ('to', to_location) ]

        final_url = base_mapquest_url + '/route?' + urllib.parse.urlencode(query_parameters)
        list_of_url.append(final_url)
    
    return list_of_url

    

    

def obtain_result(list_of_url: list) -> 'json':
    '''
    Takes a URL and returns a JSON response.
    '''
    response = None
    list_of_json = []
    for url in list_of_url:
        try:
            
            response = urllib.request.urlopen(url)
            json_text = response.read().decode(encoding = 'utf-8')
            json_dict = json.loads(json_text)
            list_of_json.append(json_dict)

        except:
            print ('MAPQUEST ERROR')
            raise SystemExit
        
        finally:
            
            if response != None:
                response.close()
                
    return list_of_json



def obtain_request_amount() -> int:
    '''
    Obtains the amount that the user would like to receive for destination information.
    '''
    return int(input())




def obtain_requests(x: int) -> list:
    '''
    Takes the amount and waits for the user to input what is desired of what he/she
    wants to receive.
    '''
    list_of_requests = []
    
    for request in range(x):
        name = input().upper()
        list_of_requests.append(name)

    return list_of_requests


def convert_meters_to_feet(x: int) -> int:
    '''
    Takes in an int (meter measurement) and returns a conversion of
    meters to feet.
    '''
    return round(x * 3.28084)



def request_action(list_of_requests: list, list_of_json: dict) -> None:
    '''
    Takes a list of requests from the user and uses it to locate
    for what was requested in the jsons in the list of jsons.
    '''
    total_distance = 0
    total_time = 0
    list_of_lnglat = []
    new_list = []

    for json in list_of_json:
        for item in json['info']['messages']:
                if item == 'We are unable to route with the given locations.':
                    print ('NO ROUTE FOUND')
                    raise SystemExit
    
    for request in list_of_requests:
        
        if 'STEPS' == request:
            print ('DIRECTIONS')

        elif 'LATLONG' == request:
            print ('LATLONGS')

        elif 'ELEVATION' == request:
            print ('ELEVATIONS')
      
        for json in list_of_json:
            
            if 'STEPS' == request:
                
                output.STEPS.locate(json)
                

            elif 'TOTALDISTANCE' == request:
                total_distance += output.TOTALDISTANCE.locate(json)      

            elif 'TOTALTIME' == request:
                total_time += output.TOTALTIME.locate(json)
                
            elif 'LATLONG' == request:
                output.LATLONG.locate(json)

            elif 'ELEVATION' == request:
                list_of_lnglat.append(output.ELEVATION.lnglat_locate(json))
                                


        if 'TOTALDISTANCE' == request:
            print ('TOTAL DISTANCE:', total_distance, 'miles')
            print ()

        elif 'TOTALTIME' == request:
            print ('TOTAL TIME:', total_time, 'minutes')
            print ()

        elif 'STEPS' == request:
            print ()

        elif 'LATLONG' == request:
            output.LATLONG.last_locate(json)
            print ()

        elif request == 'ELEVATION':

            lastlnglat = output.ELEVATION.lnglat_locate_last(json)
            list_of_lnglat.append(lastlnglat)
            
            for lst in list_of_lnglat:
                for latlng in lst:                 
                    new_list.append(latlng)
                    
    if 'ELEVATION' == request:
        output.ELEVATION.locate(new_list)
            
            
        print ()


