import requests
 
global get_ip
get_ip = input( '[+] IP : ' )
 
def info():
    response = requests.get( f'http://ipinfo.io/{ get_ip }/json' )
 
    user_ip = response.json()[ 'ip' ]
    user_city = response.json()[ 'city' ]
    user_region = response.json()[ 'region' ]
    user_country = response.json()[ 'country' ]
    user_location = response.json()[ 'loc' ]
    user_org = response.json()[ 'org' ]
    user_timezone = response.json()[ 'timezone' ]
 
    global all_info
    all_info = f'\n<INFO>\nIP : { user_ip }\nCity : { user_city }\nRegion : { user_region }\nCountry : { user_country }\nLocation : { user_location }\nOrganization : { user_org }\nTime zone : { user_timezone }'
 
    print( all_info )
 
def record():
    user_record = input( '\n[?] Record (y/n): ' )
 
    if user_record == 'y':
        file = open( 'IP Info.txt', 'a' )
        file.write( f'{ all_info }\n' )
        file.close()
 
        print( '\nSuccess!' )
 
    if user_record == 'n':
        print( '\n<O.K>' )
 
def main():
    info()
    record()
 
main()