from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length = 200)
    text_body = models.TextField()
    picture = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    web_link = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y ')
