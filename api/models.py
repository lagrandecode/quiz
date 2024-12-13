from django.db import models

# Create your models here.

class Question(models.Model):
    images = models.ImageField(null= True, blank=True, upload_to="images/")
    question = models.CharField(max_length=600)
    option = models.JSONField()
    answer = models.CharField(max_length=300)

    def __str__(self):
        return self.question
    
class Responses(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    select_answer = models.CharField(max_length=200)
    is_correct = models.BooleanField()
    response_time = models.DurationField()

    def save(self, *args,**kwags):
        self.is_correct = self.select_answer == self.answer
        super().save(*args,**kwags)

class Result(models.Model):
    score = models.FloatField()
    completion_date = models.DateTimeField(auto_now_add=True)
    pass_fail_status = models.BooleanField()
    


