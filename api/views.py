from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

# Create your views here.
@api_view(['POST'])
def getDownloadUrl(request):
    cookie = r'mid=YzVfxQALAAGY8R6FBhcA1jK-TXpG; ig_did=56D9408D-72BD-4FF0-AA5E-2D0A21385822; ig_nrcb=1; ds_user_id=26458373780; datr=4GA1Y3KJvIiXaytRyP-qewxa; shbid="19750\05426458373780\0541699366293:01f7bdae4a0211ec1c157346c1a5d88a33b85b8e1188f532d24c5477ef3c86761d11422a"; shbts="1667830293\05426458373780\0541699366293:01f73b42be103361e2aaa9c64ba8e7e08c5cd38203bdd90c5880a318b291331f25a3263c"; dpr=1.25; csrftoken=4rkgLFoDM2Ygc93kVQZwK4vP05Sz8VUf; sessionid=26458373780:PQCXC9Ehum216i:21:AYdBSYbSTcppYx5O821ULOZIGw1DkGSBqcZBPN03jQ; rur="CLN\05426458373780\0541699590687:01f7728f87e2f52c3ca35c8a4d7615d391d43b26f64e3f8311a354e01a7568e1ccfb2263"'
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
    };
    url = '{0}/?__a=1&__d=dis'.format(request.data['share_link'])
    # url = '{0}/?__a=1&__d=dis'.format('https://www.instagram.com/reel/CkwmGreAE6x')
    response = requests.get(url=url, headers=headers)
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
    return Response(data)
