import uuid

from django.db import models
from django.contrib.auth.models import User

from dj_admin_plus.fields import HTMLField


# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
    
class Place(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
    
class Currentmood(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
    
class Hobbies(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
    
class Subjects(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
    
class Flowers(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
    
class SessionUser(models.Model):
    track_id = models.UUIDField()
    username = models.CharField(max_length=100)


    def __str__(self):
        return self.username
    
class QuizModel(models.Model):
    track_id = models.UUIDField(default=uuid.uuid4)
    session_user = models.ForeignKey(to=SessionUser,on_delete=models.CASCADE)
    favorite_color_answer = models.IntegerField(null=True,blank=True)
    favorite_place_answer = models.IntegerField(null=True,blank=True)
    current_mood_answer = models.IntegerField(null=True,blank=True)
    favorite_hobby_answer = models.IntegerField(null=True,blank=True)
    favorite_subject_answer = models.IntegerField(null=True,blank=True)
    favorite_flower_answer = models.IntegerField(null=True,blank=True)

    
    def __str__(self):
        return str(self.track_id)
    
class AnswerModel(models.Model):
    track_id = models.UUIDField(default=uuid.uuid4)
    quiz=models.ForeignKey(to=QuizModel,on_delete=models.CASCADE)
    answered_by=models.ForeignKey(to=SessionUser,on_delete=models.CASCADE)
    favorite_color_answer=models.IntegerField(null=True,blank=True)
    favorite_place_answer=models.IntegerField(null=True,blank=True) 
    current_mood_answer=models.IntegerField(null=True,blank=True)
    favorite_hobby_answer=models.IntegerField(null=True,blank=True)
    favorite_subject_answer=models.IntegerField(null=True,blank=True)
    favorite_flower_answer=models.IntegerField(null=True,blank=True)


    def __str__(self):
        return str(self.quiz.track_id)
    
class Physics(models.Model):
    track_id = models.UUIDField(default=uuid.uuid4)
    question_text = models.CharField(max_length=300)
    # Options
    option_a = models.CharField(max_length=200,null=True,blank=True)
    option_b = models.CharField(max_length=200,null=True,blank=True)
    option_c = models.CharField(max_length=200,null=True,blank=True)
    option_d = models.CharField(max_length=200,null=True,blank=True)

    # Correct answer (fixed)
    ANSWER_CHOICES = [
         (1, 'Option A'),
         (2, 'Option B'),
         (3, 'Option C'),
         (4, 'Option D'),
    ]
    correct_answer = models.IntegerField(choices=ANSWER_CHOICES,null=True,blank=True)

    def __str__(self):
        return str(self.track_id)
    

    
class PhysicsAnswerModel(models.Model):
    track_id = models.UUIDField(default=uuid.uuid4)
    session_user = models.ForeignKey(to=SessionUser,on_delete=models.CASCADE)
    physics_answer = models.IntegerField(null=True,blank=True)
    physics_answer = models.IntegerField(null=True, blank=True)
    physics2_answer = models.IntegerField(null=True, blank=True)
    physics3_answer = models.IntegerField(null=True, blank=True)
    physics4_answer = models.IntegerField(null=True, blank=True)
    physics5_answer = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.session_user)
    
class Blog(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    content = HTMLField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name