from django.contrib import admin
from .models import Color,Place,Currentmood,Hobbies,Subjects,Flowers,QuizModel,AnswerModel,Blog

# Not required 

# Register your models here.
admin.site.register(Color)
admin.site.register(Place)
admin.site.register(Currentmood)
admin.site.register(Hobbies)
admin.site.register(Subjects)   
admin.site.register(Flowers)
admin.site.register(QuizModel)
admin.site.register(AnswerModel)
admin.site.register(Blog)