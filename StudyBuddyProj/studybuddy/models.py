from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

#myFields.py
from django.utils.translation import ugettext 
from django.db.models import SmallIntegerField
import datetime


# Create your models here.

"""
class MyModelName(models.Model):
    # A typical class defining a model, derived from the Model class.

    # Fields
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    # ...

    # Metadata	
    class Meta: 
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
        
         # Returns the url to access a particular instance of MyModelName.
         
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        
        # String for representing the MyModelName object (in Admin site etc.)
        
        return self.field_name
"""	

class Student(models.Model):	

	# Fields:
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Metadata
    """
    class Meta: 
        ordering = ["user.username"]
    """
    
    def __str__(self):
        
        # String for representing the MyModelName object (in Admin site etc.)
        
        return self.user.username


# Set of tuples
DAY_OF_THE_WEEK = {
    '1' : ugettext(u'Monday'),
    '2' : ugettext(u'Tuesday'),
    '3' : ugettext(u'Wednesday'),
    '4' : ugettext(u'Thursday'),
    '5' : ugettext(u'Friday'),
    '6' : ugettext(u'Saturday'), 
    '7' : ugettext(u'Sunday'),
}

DAY_OF_THE_WEEK_2 = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday')
)

class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length']=1 
        super(DayOfTheWeekField,self).__init__(*args, **kwargs)


class StudyGroup(models.Model):
    # A model for study groups.

    # Fields
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default="")
    members = models.ManyToManyField(Student , help_text="Select the Students that are a part of this StudyGroup")
    meeting_days = models.CharField(max_length=9, default='Monday', choices=DAY_OF_THE_WEEK_2)
    meeting_time = models.TimeField(default=datetime.time(16, 00))
    meeting_location = models.CharField(max_length=100, default="")

    # Metadata
    class Meta: 
    	ordering = ["name"]

    # Methods
    """
    def get_absolute_url(self):
        # Returns the url to access a particular instance of MyModelName
		return reverse('model-detail-view', args=[str(self.id)])
    """
    
    def __str__(self):        
        # String for representing the MyModelName object (in Admin site etc.)        
        return self.name


class StudyGroupForm(ModelForm):
	class Meta:
		model = StudyGroup
		fields = '__all__'
		# exclude = ()


class ChatMessage(models.Model):
	sender = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
	group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	message = models.TextField(max_length=2000)    

	def __str__(self):        
	    # String for representing the MyModelName object (in Admin site etc.)        
	    return self.message

