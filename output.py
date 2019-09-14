# Willy Saronamihardja 80408898.  ICS 32.  Project 3.

import urllib.parse
import urllib.request
import json
import mapAPI


class STEPS:
    def locate(response: dict) -> None:
        '''
        Goes through the MapQuest dict and prints out the narrative
        from the dict.
        '''
        for item in response['route']['legs']:
            for subitem in item['maneuvers']:
                print (subitem['narrative'])

            


class TOTALDISTANCE:
    def locate(response: dict) -> int:
        '''
        Goes through the MapQuest dict and returns a rounded int
        representing the distance it takes from point A to point B.
        '''
        distance = response['route']['distance']
        return int(round(distance))



class TOTALTIME:
    def locate(response: dict) -> int:
        '''
        Goes through the MapQuest dict and returns a rounded int
        representing the time it takes from point A to point B.
        '''
        time = response['route']['time']
        newtime = time / 60
        return int(round(newtime))



class LATLONG:
    def locate(response: dict) -> None:
        '''
        Goes through a MapQuest dict and prints out the latitude and
        longitude of the locations.
        '''
        lng = response['route']['locations'][0]['latLng']['lng']
        lat = response['route']['locations'][0]['latLng']['lat']
       
        if lng < 0:                    
            lng = -1 * lng
            lng = '{0:.2f}'.format(lng) + 'W'  
        else:
            lng = '{0:.2f}'.format(lng) + 'E'
            
        if lat < 0:
            lat = -1 * lat
            lat = '{0:.2f}'.format(lat) + 'S'
        else:
            lat = '{0:.2f}'.format(lat) + 'N'
            
        print (lat, lng)
        
        
    def last_locate(response: dict) -> None:
        '''
        Goes through a MapQuest dict and prints the last lat and lng
        of the destinations in a certain format.
        '''
        
        last_lng = response['route']['locations'][-1]['latLng']['lng']
        last_lat = response['route']['locations'][-1]['latLng']['lat']

        if last_lng < 0:                    
            last_lng = -1 * last_lng
            last_lng = '{0:.2f}'.format(last_lng) + 'W'  
        else:
            last_lng = '{0:.2f}'.format(last_lng) + 'E'
            
        if last_lat < 0:
            last_lat = -1 * last_lat
            last_lat = '{0:.2f}'.format(last_lat) + 'S'
        else:
            last_lat = '{0:.2f}'.format(last_lat) + 'N'
            
        print (last_lat, last_lng)


class ELEVATION:
    def lnglat_locate(response: dict) -> [float]:
        '''
        Goes through a MapQuest dict and returns a list of all the
        unchanged lats and lngs appended to it.
        '''
        list_of_latlng = []
        lng = response['route']['locations'][0]['latLng']['lng']
        lat = response['route']['locations'][0]['latLng']['lat']
                   
        list_of_latlng.append(lat)
        list_of_latlng.append(lng)
        return list_of_latlng


    def lnglat_locate_last(response: dict) -> [float]:
        '''
        Goes through a MapQuest dict and returns a list of the last
        unchanged lat and lng with those two appended to it.
        '''
        list_of_last_latlng = []
        last_lng = response['route']['locations'][-1]['latLng']['lng']
        last_lat = response['route']['locations'][-1]['latLng']['lat']
            
        list_of_last_latlng.append(last_lat)
        list_of_last_latlng.append(last_lng)
        return list_of_last_latlng



        
    def locate(list_of_lnglat: [float]) -> None:
        '''
        Takes a list of the lng and lat and converts that in order to create
        the url.  The url is then taken to be made into a json and into a
        dict that Python can read.  Using that dict and a certain function,
        the height (elevation) is printed.
        '''
        thestr = str(list_of_lnglat)

        newstr = thestr.replace("[", '')
        newstr = newstr.replace("]", '')
        newstr = newstr.replace(" ", '')
        
        query_parameters = [
            ('key', mapAPI.consumer_key), ('shapeFormat', 'raw'),
            ('latLngCollection', newstr)  ]
        
        url = mapAPI.base_mapquest_elevation_url + "/profile?" + urllib.parse.urlencode(query_parameters)
        
        try:
            response = urllib.request.urlopen(url)
            json_text = response.read().decode(encoding = 'utf-8')
            json_dict = json.loads(json_text)

        except:
            print ('MAPQUEST ERROR')
            raise SystemExit


        for item in json_dict['elevationProfile']:
            newitem = item['height']
            newitem = mapAPI.convert_meters_to_feet(newitem)
            print (newitem)







        
