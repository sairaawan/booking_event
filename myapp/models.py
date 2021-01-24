from django.db import models
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.conf import settings
from django_model_changes import ChangesMixin
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError

# Create your models here.
User = settings.AUTH_USER_MODEL
class Event(models.Model):
	
	Event_Date=models.DateField()
	Available='Available'
	Booked='Booked'
	Position_choice=[
	(Available, 'Available'),
	(Booked, 'Booked')]
	Position=models.CharField(
		max_length=20,
        choices=Position_choice,
        default=Available
        )


	def __str__(self):
		return f'{self.Event_Date} - {self.Position}'
		
class Artist(ChangesMixin, models.Model):
	Handled_by= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	Name = models.CharField(max_length = 200, null=True)
	Telephone=models.CharField(max_length = 200, null=True) 
	Members=models.IntegerField(blank=True, null=True)
	email=models.EmailField(max_length=254)
	genre=models.CharField(max_length = 200, null=True)
	Select_event=models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
	pending='pending'

	confirm='confirm'
	cancel='cancel'
	status_choice=[
	(pending,'pending'),
	(confirm,'confirm'),
	(cancel,'cancel')
	]
	Status=models.CharField(
		max_length=20,
        choices=status_choice,
        default=pending
        )
	Additional_details=models.TextField(blank=True, null=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	send_confirmation=models.BooleanField(default=False)
	send_application= models.BooleanField(default=False)
	send_contract=models.BooleanField(default=False)
	


	def __str__(self):
		return f'{self.Name} has status {self.Status} booked on  {self.timestamp} is handled by {self.Handled_by} has booked for the following:  [ {self.Select_event}]'
@receiver(pre_save, sender=Artist)
def send_email_if_flag_enabled(sender, instance, **kwargs):
    if instance.previous_instance().send_confirmation == False and instance.send_confirmation == True:
    	subject = 'Booking Confirmation'
    	message = '''Dear {name},

Your booking has been confirmed.

Regards,

Arts2LifeUKEvents'''
    	messagef=message.format(name=instance.Name)
    	from_email = 'arts2lifeukbooking@gmail.com'
    	
    	msg=EmailMessage(subject, messagef,from_email, [instance.email],reply_to=['arts2lifeukevents@gmail.com', 'arts2lifeukmail.com'] )
    	#msg.attach_file("data/javascript.docx/")
    	msg.send()
    if instance.previous_instance().send_send_application == False and instance.send_send_application == True:
    	subject = 'Application form'
    	message = '''Dear {name},

Plesae find the attached application form and return it back by replying to this email.

Regards,

Arts2LifeUKEvents'''
    	messagef=message.format(name=instance.Name)
    	from_email = 'arts2lifeukbooking@gmail.com'
    	
    	msg=EmailMessage(subject, messagef,from_email, [instance.email],reply_to=['arts2lifeukevents@gmail.com', 'arts2lifeukmail.com'] )
    	msg.attach_file("data/registration.docx/")
    	msg.send()
    if instance.previous_instance().send_send_contract == False and instance.send_send_contract == True:
    	subject = 'Contract'
    	message = '''Dear {name},

Plesae find the attached contract form and return it back by replying to this email.

Regards,

Arts2LifeUKEvents'''
    	messagef=message.format(name=instance.Name)
    	from_email = 'arts2lifeukbooking@gmail.com'
    	
    	msg=EmailMessage(subject, messagef,from_email, [instance.email],reply_to=['arts2lifeukevents@gmail.com', 'arts2lifeukmail.com'] )
    	msg.attach_file("data/contract.docx/")
    	msg.send()


