from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

# Create your views here.
@api_view(['POST'])
def getDownloadUrl(request):
    cookie = r'mid=YzVfxQALAAGY8R6FBhcA1jK-TXpG; ig_did=56D9408D-72BD-4FF0-AA5E-2D0A21385822; ig_nrcb=1; ds_user_id=26458373780; datr=4GA1Y3KJvIiXaytRyP-qewxa; dpr=1.25; csrftoken=6QiG5luupwYujvumjNBDoqDRtMMXfXGg; sessionid=26458373780%3ARMoeo3bidC6tAO%3A15%3AAYcpm0my0eVtAFgJp3JjBwJATSzBZPVdE4MCey8HAw; shbid="19750\05426458373780\0541699629613:01f7ce82ace8bfae96ff1d0958f769e2eda821ec6a7b01363d2b4ee5f820ea7cb1f5338e"; shbts="1668093613\05426458373780\0541699629613:01f7b1c4a65bceac87da78cf7081490eee7d68ac780cc721eebfb8502f67311270283d1e"; rur="CLN\05426458373780\0541699629705:01f70387211e8ff1ab4beca5f8ceead6424d608f88ebfc53fac173fa0a4f54f5d405d767'
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
    url = '{0}/?__a=1&__d=dis'.format(request.data['share_link']) 
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
