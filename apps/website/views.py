from django.shortcuts import render
from imgurpython import ImgurClient

client_id = '5607e0203dfde28'
client_secret = '34352559f583b268e370cb7c1b18705d3d8917f3'

client = ImgurClient(client_id, client_secret)

def index (request):
    return render(request, 'website/index.html')

def painting (request):
    roshipainting = client.get_album_images("AF1vc")
    roshiDict = {}
    count = 1
    for x in roshipainting:
        link = str(x.link)
        roshiDict.update({count:link})
        count = count + 1
    context = {'roshiDict' : roshiDict}
    return render (request, 'website/painting.html', context)

def mural (request):
    roshimural = client.get_album_images("O3VTR")
    roshiDictMural = {}
    count = 1
    for x in roshimural:
        link = str(x.link)
        roshiDictMural.update({count:link})
        count = count + 1
    print roshiDictMural
    print 50*'*'
    context = {'roshiDictMural' : roshiDictMural}
    return render (request, 'website/mural.html', context)
