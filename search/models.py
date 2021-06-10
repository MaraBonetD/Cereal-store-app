from django.contrib.auth.models import User
from django.db import models

class Search(models.Model):
    search_string = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    search_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {}".format(self.search_string, self.user, self.search_timestamp)

