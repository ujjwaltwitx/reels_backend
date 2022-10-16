from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

# Create your views here.
@api_view(['POST'])
def getDownloadUrl(request):
    
    cookie = r'mid=YzVfxQALAAGY8R6FBhcA1jK-TXpG; ig_did=56D9408D-72BD-4FF0-AA5E-2D0A21385822; ig_nrcb=1; csrftoken=NGHr6eG9cFXBQvGouZdv4b2Y3oCqfWwj; ds_user_id=26458373780; sessionid=26458373780%3A0RPa8kE6VXe7lK%3A29%3AAYeRGcN3BT8R0GUP7jSmfRAk-ebzA-r3jreEQdI6bw; dpr=1.25; datr=4GA1Y3KJvIiXaytRyP-qewxa; shbid="19750\05426458373780\0541695978599:01f7b17421e21acfcc2b1e27ecc282819ec4c67fb4b292263dfe692c98f4fac2ac364f01"; shbts="1664442599\05426458373780\0541695978599:01f7a25ebc6d7edee1261b7563139cd6e894b86b337915a191e2bbea809bac179e041de3"; rur="CLN\05426458373780\0541695978687:01f741755fa6bf720320977e2a4afe5830e2400fe43d56b3032926b917a3c4bced412cf0"'
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
