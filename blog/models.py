from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    checks = models.TextField(null=True)
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    # writer = models.CharField(max_length=200)



    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]