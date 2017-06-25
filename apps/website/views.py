from django.shortcuts import render
from imgurpython import ImgurClient

client_id = '5607e0203dfde28'
client_secret = '34352559f583b268e370cb7c1b18705d3d8917f3'

client = ImgurClient(client_id, client_secret)

def index (request):
    return render(request, 'website/index.html')

def sketch (request):
    items = client.gallery()
    roshigallery = client.get_album_images("FnEEt")
    print roshigallery
    context = {'roshigallery' : roshigallery}
    return render (request, 'website/sketch.html', context)

def paint (request):
    return render (request, 'website/paint.html')
