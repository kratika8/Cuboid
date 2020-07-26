from django.db import models

class Cuboid(models.Model):
    # fields of the model

    id = models.IntegerField(primary_key=True)
    length = models.IntegerField(null=True, blank=True, default=None)
    breadth = models.IntegerField(null=True, blank=True, default=None)
    height = models.IntegerField(null=True, blank=True, default=None)
    createdby = models.CharField(max_length=50, null=True)
    createdtime = models.DateField(null= True)






