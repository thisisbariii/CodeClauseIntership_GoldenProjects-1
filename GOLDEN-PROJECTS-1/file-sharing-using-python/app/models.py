from django.db import models

class myfile(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    file = models.FileField(upload_to="myfile")
    date = models.DateField(auto_now_add=True)
