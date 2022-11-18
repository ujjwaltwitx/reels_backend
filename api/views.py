from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

# Create your views here.
@api_view(['POST'])
def getDownloadUrl(request):
    cookie = r'mid=YzVfxQALAAGY8R6FBhcA1jK-TXpG; ig_did=56D9408D-72BD-4FF0-AA5E-2D0A21385822; ig_nrcb=1; datr=4GA1Y3KJvIiXaytRyP-qewxa; shbid="19750\05426458373780\0541699900272:01f701e0bd207b2afeddaa16ad021a7cb482673b62cba2eb3d005bba57c30bbbd441afcf"; shbts="1668364272\05426458373780\0541699900272:01f74eb9cc711169bc4cb7eff33ae89a840895c203dc41fe716f74d1ff0aba0f0b009780"; dpr=1; ds_user_id=56375154046; csrftoken=vriswhTYhDz5mNhsPHcPgWY8kZNJGFIJ; sessionid=56375154046:srSoSCAJXFGdHL:23:AYfUsQDpDPUbtK_GLgd-DFbJsajuNTpNVeH45jhn0g; rur="LDC\05456375154046\0541700296857:01f794d2535c02ebc3b2a68e0c39486c87f7a3b33f7b47632271ee0a1540b267dd3be620"'
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
    # print(request)
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
