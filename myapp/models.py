from django.db import models

# Create your models herefrom django.db import models
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
    yes='yes'
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
    no='no'
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
    send_cancellation=models.BooleanField(default=False)
    bool_choices=[(yes, 'yes'),(no, 'no')]
    Have_you_worked_with_Arts2Life_UK_before=models.CharField(max_length=20,
        choices=bool_choices,
        default=no)
    Have_you_received_copy_of_registration_form=models.CharField(max_length=20,
        choices=bool_choices,
        default=no)
    Have_you_received_copy_of_contract_form=models.CharField(max_length=20,
        choices=bool_choices,
        default=no)
    def __str__(self):
        return f'{self.Name} has status {self.Status} booked on  {self.timestamp} is handled by {self.Handled_by} has booked for the following:  [ {self.Select_event}]'


@receiver(pre_save, sender=Artist)
def send_email_if_flag_enabled(sender, instance, **kwargs):
    if instance.previous_instance().send_confirmation == False and instance.send_confirmation == True:
        subject = 'Booking Confirmation'
        message = '''Hello {name},

Great news! This email is to confirm that we have you booked in to be performing with us 
Our events team will be in touch with you shortly with the contract so please make sure to keep 
an eye on out for any new emails.

We really look forward to working with you!

Best regards,

Arts2LifeUK Events'''
        messagef=message.format(name=instance.Name, event=instance.Select_event)
        from_email = 'arts2lifeukbooking@gmail.com'
        
        msg=EmailMessage(subject, messagef,from_email, [instance.email],reply_to=['arts2lifeukevents@gmail.com'] )
        #msg.attach_file("data/javascript.docx/")
        msg.send()
    if instance.previous_instance().send_application == False and instance.send_application == True:
        subject = 'Application form'
        message = '''Hey {name},

We are very excited that you have reached out to us, thank you! The registration form is 
attached to this email; if you could complete it (the more info you include, the better) and get it 
back to us ASAP, we can go from there. 

Looking forward to working with you! 

Best regards,

Arts2LifeUK Events'''
        messagef=message.format(name=instance.Name)
        from_email = 'arts2lifeukbooking@gmail.com'
        
        msg=EmailMessage(subject, messagef,from_email, [instance.email],reply_to=['arts2lifeukevents@gmail.com'] )
        msg.attach_file("data/registration.docx/")
        msg.send()
    if instance.previous_instance().send_contract == False and instance.send_contract == True:
        subject = 'Contract'
        message = '''Dear {name},
Plesae find the attached contract form and return it back by replying to this email.
Regards,
Arts2LifeUKEvents'''
        messagef=message.format(name=instance.Name)
        from_email = 'arts2lifeukbooking@gmail.com'
        
        msg=EmailMessage(subject, messagef,from_email, [instance.email],reply_to=['arts2lifeukevents@gmail.com'] )
        msg.attach_file("data/contract.docx/")
        msg.send()
    if instance.previous_instance().send_cancellation == False and instance.send_cancellation == True:
        subject = 'Booking status: cancelled'
        message = '''Dear {name},
        
We are so sorry but we have been unable to book your act to perform.

This is rubbish news but please check out the availability of our other events and get booked in 
for them. You can do this via the drop-down list on the arts2life.co.uk event booking page or just
send an email over to our Events Manager (arts2lifeukevents@gmail.com) and they will get 
back to you ASAP. 

Best regards and hopefully see you soon,

Arts2LifeUK Events'''
        messagef=message.format(name=instance.Name)
        from_email = 'arts2lifeukbooking@gmail.com'
        
        msg=EmailMessage(subject, messagef,from_email, [instance.email],reply_to=['arts2lifeukevents@gmail.com'] )
        #msg.attach_file("data/contract.docx/")
        msg.send()




