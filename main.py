# Willy Saronamihardja 80408898.  ICS 32.  Project 3.

import mapAPI
import output



def main():
    try: 
        amount_of_locations = mapAPI.obtain_location_amount()
        
        list_of_places = mapAPI.obtain_location_areas(amount_of_locations)
     
        the_url = mapAPI.build_search_url(list_of_places)
        
        the_result = mapAPI.obtain_result(the_url)

        request_amount = mapAPI.obtain_request_amount()

        all_requests = mapAPI.obtain_requests(request_amount)

        mapAPI.request_action(all_requests, the_result)
        
    except:
        raise SystemExit
        
    else:
        print ('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    




if __name__ == '__main__':
    main()
