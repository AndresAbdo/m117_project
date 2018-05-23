from django.db import models
from django.contrib.auth.models import User

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


class StudyGroup(models.Model):
    # A model for study groups.

    # Fields
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default="")
    members = models.ManyToManyField(Student , help_text="Select the Students that are a part of this StudyGroup")


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




class ChatMessage(models.Model):
	sender = models.OneToOneField(Student, on_delete=models.DO_NOTHING)
	group = models.OneToOneField(StudyGroup, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	message = models.TextField(max_length=2000)    

	def __str__(self):        
	    # String for representing the MyModelName object (in Admin site etc.)        
	    return self.group

