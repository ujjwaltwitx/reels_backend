from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import schedule
import utility_functions

cookie = r'csrftoken=VOfNPnjkPjH7IekAo0Hjk8KUS64zvtmI;ds_user_id=56375154046;ig_did=B9C3B47F-3BB4-4D03-95FC-C4C0099BF3AB;mid=Y4BTZgAEAAGsmZYfCRVhUEpOTkp8;rur="VLL\05456375154046\0541700890345:01f7a528bb91235c4933fffc071b54dabe22d760ca76890c3444c0765a4b4fa2f4617183";sessionid=56375154046%3AaU6mA8vrCtYA31%3A21%3AAYfdBmdmWWVo6EGeEDhhHEz-gD9otKOlLdWHQcmP_A;ig_nrcb=1;dpr=1.25;datr=4GA1Y3KJvIiXaytRyP-qewxa;'
def set_cookie():
    global cookie
    cookie = utility_functions.get_cookie()

schedule.every(6).hours.do(set_cookie)

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
