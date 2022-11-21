from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import schedule
import utility_functions

cookie = r'csrftoken=xNtrN8kd9oDiRF8q1NU20pqOUOTL9lMC;ds_user_id=56375154046;ig_did=0387AE91-4A44-4517-84B8-69E5EECBDDB2;mid=Y3sWuAAEAAHETLD9KjRko81qdnKx;rur="LDC\05456375154046\0541700547130:01f776af8ba46c74d661153c1026775ef599eb56e11d45fe67e1bc8a30d098d89b103ae0";sessionid=56375154046%3AZfXe9XzuNT263g%3A10%3AAYd2Ou73p0ijNYG1iNb_JopygsnyhBT4GTKnCG6TUw;'
def set_cookie():
    global cookie
    cookie = utility_functions.get_cookie()


schedule.every(12).hours.do(set_cookie)

# Create your views here.
@api_view(['POST'])
def getDownloadUrl(request):
    schedule.run_pending()
    response = ''
    headers = {
        'Host': 'www.instagram.com',
        'User-Agent': 'Mozilla',
        'Accept': 'text/html,application/xhtml+xml,application/xml',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Alt-Used': 'www.instagram.com',
        'Cookie': cookie,
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Cache-Control': 'max-age=0',
        'TE': 'trailers'
    }
    url = '{0}/?__a=1&__d=dis'.format(request.data.get('share_link', False))
    response = requests.get(url=url, headers=headers)
    data = {}
    try:
        shotcodeMedia = response.json()['graphql']['shortcode_media']
        videoUrl = shotcodeMedia['video_url']
        videoId = shotcodeMedia['shortcode']
        videoThumbnailUrl = shotcodeMedia['display_resources'][2]['src']
        accountThumbnailUrl = shotcodeMedia['owner']['profile_pic_url']
        accountName = shotcodeMedia['owner']['username']
        viewCount = shotcodeMedia['video_view_count']
        data = {
            'videoUrl' :videoUrl,
            'videoId':videoId,
            'videoThumbnailUrl' : videoThumbnailUrl,
            'accountThumbnailUrl' : accountThumbnailUrl,
            'accountName': accountName,
            'viewCount':viewCount
        }
    except:
        data = {
            'error' : "cant fetch data from the server"
        }
    try:
        shotcodeMedia = response.json()['items'][0]
        videoUrl = shotcodeMedia['video_versions'][0]['url']
        videoId = shotcodeMedia['code']
        videoThumbnailUrl = shotcodeMedia['image_versions2']['candidates'][0]['url']
        accountThumbnailUrl = shotcodeMedia['user']['profile_pic_url']
        accountName = shotcodeMedia['user']['username']
        viewCount = shotcodeMedia['view_count']

        data = {
            'videoUrl' :videoUrl,
            'videoId':videoId,
            'videoThumbnailUrl' : videoThumbnailUrl,
            'accountThumbnailUrl' : accountThumbnailUrl,
            'accountName': accountName,
            'viewCount':viewCount
        }
    except:
        data = {
            'error' : "cant fetch data from the server"
        }

    return Response(data)
