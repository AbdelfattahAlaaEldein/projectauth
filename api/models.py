from django.db import models

# Create your models here.


from django.db import models

class skills(models.Model):
    name=models.CharField(max_length=50,unique=True)
    content=models.TextField()
    video=models.FileField(upload_to='videos/')
    # models.FileField(blank=False,null=False)

    def __str__(self):
      return self.name