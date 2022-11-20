from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import utility_functions

cookie = r'mid=YzVfxQALAAGY8R6FBhcA1jK-TXpG; ig_did=56D9408D-72BD-4FF0-AA5E-2D0A21385822; ig_nrcb=1; datr=4GA1Y3KJvIiXaytRyP-qewxa; dpr=1.25; csrftoken=0C9AISnZ5ubwhXojnpOGnCoMm4EW5NUB; ds_user_id=26458373780; sessionid=26458373780:0h0xFaAnJ1pT6a:12:AYfqctEhcvIk-7LF1ojsIkmHQcWkhuCQ1fZ7oIprvQ; shbid="19750\05426458373780\0541700510763:01f76302e8e36649e18a2b91fe063d58f3b61e9ee0cc45ab5f5e4f6e795fc88353d9003b"; shbts="1668974763\05426458373780\0541700510763:01f779df1fe28fba7203acc109c7d26af13e105a19e189aba49689b81be433d77bec8333"; rur="PRN\05426458373780\0541700511387:01f79050d8f9ec314c8099db515ea5dfb8992dc6ef61c76fe507c4c2e210d0451d04697f"'

# Create your views here.
@api_view(['POST'])
def getDownloadUrl(request):
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

    # shotcodeMedia = response.json()['graphql']['shortcode_media']
    # videoUrl = shotcodeMedia['video_url']
    # videoId = shotcodeMedia['shortcode']
    # videoThumbnailUrl = shotcodeMedia['display_resources'][2]['src']
    # accountThumbnailUrl = shotcodeMedia['owner']['profile_pic_url']
    # accountName = shotcodeMedia['owner']['username']
    # viewCount = shotcodeMedia['video_view_count']
    # data = {
    #     'videoUrl' :videoUrl,
    #     'videoId':videoId,
    #     'videoThumbnailUrl' : videoThumbnailUrl,
    #     'accountThumbnailUrl' : accountThumbnailUrl,
    #     'accountName': accountName,
    #     'viewCount':viewCount
    # }
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
