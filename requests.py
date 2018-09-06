import socket
import urllib.request


Pragma = 'akamai-x-tapioca-trace,akamai-x-feo-trace, akamai-x-cache-on, akamai-x-cache-remote-on, \
akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-nonces, \
akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, \
akamai-x-get-request-id'
headers = {'Pragma': Pragma}


#variables
final_result = {}
final_result['snc'] = 0
final_result['sac'] = 0

total_requests = 20
url = 'http://img.grouponcdn.com/deal/VAmXvXyNjkxBLhybuTVDq6uLjVH/VA-1000x600/v1/t220x134.jpg?cache_bust=true'
origin_1 = 'img-sac1.o.grouponcdn.com'


for i in range(total_requests):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    #print(dir(response))
    #print(response.getheaders())

    session_info_List = response.getheader('X-Akamai-Session-Info').split(',')
    for everySessionInfo in session_info_List:
        name_value = everySessionInfo.split(';')
        if name_value[0].strip() == 'name=PMUSER_ORIGIN_TO_USE':
            print(name_value[1])
            if origin_1 in name_value[1]:
                final_result['sac'] += 1
            else:
                final_result['snc'] += 1



print('Origin_1 SAC Requests: ' + str(final_result['sac']) + '\n')
print('Origin_2 SNC Requests: ' + str(final_result['snc']) + '\n')
