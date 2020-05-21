from django.db import models
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Question_papers(models.Model):
    college = models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    subject= models.CharField(max_length=100)
    examination=models.CharField(max_length=100)
    paper = models.FileField(upload_to='preqps',null=True,blank=True)
    


    def __str__(self):
        return  self.college + ' , ' + self.course +' , '+self.year + ' - '+ self.subject 

    
