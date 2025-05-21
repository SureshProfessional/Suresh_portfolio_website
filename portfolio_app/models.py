from django.db import models

class SingleObjectModel(models.Model):
    class Meta:
        abstract = True 
    
    def save(self,*args, **kwargs):
        self.pk = 1  
        super().save(*args,**kwargs)

    def delete(self,*args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj,created = cls.objects.get_or_create(pk=1)
        return obj


class Profile(SingleObjectModel):
    main_photo = models.ImageField(upload_to='uploads/',)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    main_project = models.CharField(max_length=50)
    add_resume = models.FileField(upload_to='uploads/',)
    
    def __str__(self):
        return self.name
