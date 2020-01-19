from django.db import models


class Users(models.Model):
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Publications(models.Model):
    student_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title