from apiclient.discovery import build

service = build("customsearch", "v1",
               developerKey="AIzaSyBp3hgyJhHb0eqzRSYNl-_a0AHw_EToLBk")

res = service.cse().list(
    q='face',
    cx='006837971229697054245:dwfstyb2fvc',
    searchType='image',
    num=2,
    imgType='clipart',
    fileType='png',
    safe= 'off'
).execute()

if not 'items' in res:
    print 'No result !!\nres is: {}'.format(res)
else:
    for item in res['items']:
        print('=================================================')
        print(item['title'])
        print(item['link'])