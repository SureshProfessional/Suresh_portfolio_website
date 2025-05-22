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
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name

class AboutMe(models.Model):
    description = models.TextField()
    
    def __str__(self):
        return self.description

class Skill(models.Model):
    logo_link = models.CharField(max_length=50)
    logo_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.logo_name

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_des = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)
    
    def __str__(self):
        return self.project_name

class Testimonials(models.Model):
    writer = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.writer
    
class Journey(models.Model):
    year = models.IntegerField()
    details = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.year)