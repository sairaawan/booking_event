from django.shortcuts import render
from .models import Artist, Event
from .forms import ArtistForm
from django.http import HttpResponseRedirect

# Create your views here.

def createform(request): 
	form = ArtistForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/home/success/')
	context = {'form': form}
	return render(request, 'Index.html', context)


def success(request):
	return render(request, 'success.html',{})