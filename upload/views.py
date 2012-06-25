# Create your views here.
from upload.models import FPImage
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import requests
from uuid import uuid4
from django.core import serializers
from mimetypes import guess_extension

def home(request):
	return render(request, 'upload/home.html', {'pics':FPImage.objects.all()})
		
def fp_ajax(request):
	if request.is_ajax and request.method == "POST":
		image_url = request.POST.get("data[url]")
		file_ext = guess_extension(str(request.POST.get("data[data][type]")))
		file_name = str(uuid4()) + file_ext
		
		#from http://djangosnippets.org/snippets/2587/
		req = requests.get(image_url)
		img_temp = NamedTemporaryFile(delete=True)
		img_temp.write(req.content)
		img_temp.flush()
		
		new_img = FPImage()
		new_img.image.save(file_name, File(img_temp), save=True)
		
		json_response = serializers.serialize("json", [new_img])
		return HttpResponse(json_response, mimetype="application/json")
	else:
		raise Http404
	