from django.shortcuts import render
from .models import Artist, Event
from .forms import ArtistForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
# Create your views here.

def createform(request): 
	name=''
	email=''
	comment=''
	form = ArtistForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		name= form.cleaned_data.get("Name")
		email= form.cleaned_data.get("email")
		subject= "New booking"
		recipients = ['syraawan@live.com']
		comment= name + " with the email, " + email + ", has made request for new booking";
		form.save()
		send_mail(subject, comment, email, recipients )

		
	context = {'form': form}
	return render(request, 'index.html', context)



