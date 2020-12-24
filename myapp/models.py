from django.conf import settings
from django.db import models
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
		
class Artist(models.Model):
	Handled_by= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	Name = models.CharField(max_length = 200, null=True)
	Telephone=models.CharField(max_length = 200, null=True) 
	Members=models.IntegerField(blank=True, null=True)
	email=models.EmailField(max_length=254)
	genre=models.CharField(max_length = 200, null=True)
	Select_event=models.ForeignKey(Event, on_delete=models.CASCADE, default=1, null=True, blank=True)
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


	def __str__(self):
		return f'{self.Name} has status {self.Status} booked on  {self.timestamp} is handled by {self.Handled_by} has booked for the following:  [ {self.Select_event}]'


