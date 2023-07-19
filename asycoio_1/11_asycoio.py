# check the status of many webpages
import asyncio
import time
from urllib.parse import urlsplit

# get the HTTP/S status of a webpage
async def get_status(url):
    # split the url into components
    url_parsed = urlsplit(url)
    print(f'{time.ctime()} fetch {url}')
    # open the connection
    if url_parsed.scheme == 'https':
        reader, writer = await asyncio.open_connection(url_parsed.hostname, 443,ssl=True)
    else:
        reader, writer = await asyncio.open_connection(url_parsed.hostname, 80)
    # send GET request
    query = f'GET {url_parsed.path} HTTP/1.1\r\nHost: {url_parsed.hostname}\r\n\r\n'
    # write query to socket
    writer.write(query.encode())
    # wait for the bytes to be written to the socket
    await writer.drain()
    # read the single line response
    response = await reader.readline()
    # close the connection
    writer.close()
    # decode and strip white space
    status = response.decode().strip()
    print(f'{time.ctime()} done {url}')
    # return the response
    return status

# main coroutine
async def main():
    # List of top 10 website to check
    sites = ['https://www.google.com/',
            'https://www.youtube.com',
            'https://www.facebook.com',
            'https://www.twitter.com/',
            'https://www.instagram.com',                    
            'https://www.baidu.com',
            'https://www.wikipedia.org',
            'https://www.yandex.ru/',
            'https://www.yahoo.com',
            'https://www.whatsapp.com'
            ]
    # check the status of all websites
    for url in sites:
        # get the status foe the url
        status = await get_status(url)
        #r eport the url and its status
        print(f'{time.ctime()} {url:30}:\t{status}')

#run the asyncio program
asyncio.run(main())    



## Answer

# PS E:\00Lab\IOT\asyncio_exercise\asycoio_1> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/asycoio_1/11_asycoio.py
# Wed Jul 19 14:32:50 2023 fetch https://www.google.com/
# Wed Jul 19 14:32:50 2023 done https://www.google.com/
# Wed Jul 19 14:32:50 2023 https://www.google.com/       :
#    HTTP/1.1 200 OK
# Wed Jul 19 14:32:50 2023 fetch https://www.youtube.com       
# Wed Jul 19 14:32:51 2023 done https://www.youtube.com
# Wed Jul 19 14:32:51 2023 https://www.youtube.com       :
#    HTTP/1.0 404 Not Found
# Wed Jul 19 14:32:51 2023 fetch https://www.facebook.com      
# Wed Jul 19 14:32:51 2023 done https://www.facebook.com
# Wed Jul 19 14:32:51 2023 https://www.facebook.com      :
#    HTTP/1.1 400 Bad Request
# Wed Jul 19 14:32:51 2023 fetch https://www.twitter.com/      
# Wed Jul 19 14:32:52 2023 done https://www.twitter.com/
# Wed Jul 19 14:32:52 2023 https://www.twitter.com/      :
#    HTTP/1.1 301 Moved Permanently
# Wed Jul 19 14:32:52 2023 fetch https://www.instagram.com     
# Wed Jul 19 14:32:52 2023 done https://www.instagram.com
# Wed Jul 19 14:32:52 2023 https://www.instagram.com     :
#    HTTP/1.1 400 Bad Request
# Wed Jul 19 14:32:52 2023 fetch https://www.baidu.com
# Wed Jul 19 14:32:53 2023 done https://www.baidu.com
# Wed Jul 19 14:32:53 2023 https://www.baidu.com         :
#    HTTP/1.1 400 Bad Request
# Wed Jul 19 14:32:53 2023 fetch https://www.wikipedia.org     
# Wed Jul 19 14:32:53 2023 done https://www.wikipedia.org
# Wed Jul 19 14:32:53 2023 https://www.wikipedia.org     :
#    HTTP/1.1 400
# Wed Jul 19 14:32:53 2023 fetch https://www.yandex.ru/        
# Wed Jul 19 14:32:54 2023 done https://www.yandex.ru/
# Wed Jul 19 14:32:54 2023 https://www.yandex.ru/        :
#    HTTP/1.1 302 Moved temporarily
# Wed Jul 19 14:32:54 2023 fetch https://www.yahoo.com
# Wed Jul 19 14:32:55 2023 done https://www.yahoo.com
# Wed Jul 19 14:32:55 2023 https://www.yahoo.com         :
#    HTTP/1.0 400 Invalid HTTP Request
# Wed Jul 19 14:32:55 2023 fetch https://www.whatsapp.com      
# Wed Jul 19 14:32:55 2023 done https://www.whatsapp.com
# Wed Jul 19 14:32:55 2023 https://www.whatsapp.com      :
#    HTTP/1.1 400 Bad Request