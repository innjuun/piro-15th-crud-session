from django.db import models

# Create your models here.
class Member(models.Model):
    generation = models.IntegerField("기수")
    birth_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField("연락처", max_length=15)
    profile = models.ImageField("프로필 사진", null=True, upload_to="images/")
    introduction = models.TextField("자기소개", max_length=1000, null=True)

    def __str__(self):
        return str(self.phone_number)