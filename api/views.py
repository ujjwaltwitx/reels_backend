from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import schedule
import utility_functions

cookie = r'csrftoken=dDi8TdHefg2YkI1Gg5GlW6jzTjyG3VMZ;ds_user_id=56375154046;ig_did=1B577566-6737-4BF8-B233-46BABCD0D51E;mid=Y4b37QAEAAGrkvSn4X7UYMk-HcbN;rur="LDC\05456375154046\0541701325679:01f7ba10f9221b0cb7c14255f59b8c9c6dbedccf127da04c505362a942d1827674b62ca7";sessionid=56375154046%3A73dtjLO36XUvfC%3A24%3AAYd26f6Xgwb-pfv4jFGmTdcF7-Vt49sJqlnnKIxddQ;ig_nrcb=1;dpr=1.25;datr=4GA1Y3KJvIiXaytRyP-qewxa;'
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
