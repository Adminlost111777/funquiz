from django.urls import path

from . import views

urlpatterns = [
    path('',views.quiz_view, name='home'),
    path('blog/',views.blog_list,name='blog_list'),
    path('blog/<slug:path>/',views.blog_detail,name='blog_detail'),
    path('color/<uuid:track_id>/',views.color,name='color'),
    path('place/<uuid:track_id>/',views.Place_view,name='place'),
    # path('place/<int:pk>/',views.Place_view,name='place'),
    path('currentmood/<uuid:track_id>/',views.Currentmood_view,name='currentmood'),
    path('hobbies/<uuid:track_id>/',views.Hobbies_view,name='hobbies'),
    path('subject/<uuid:track_id>/',views.Subject_view,name='subject'), 
    path('flower/<uuid:track_id>/',views.Flower_view,name='flower'),
    path('calculator/<uuid:track_id>/',views.calculator_view,name='calculator'),
    path("create-quiz/", views.create_quiz, name="create_quiz"),
    path('physicsgame_quiz/',views.physicsgame_quiz,name='physicsgame_quiz'),
    path("share-quiz/<uuid:track_id>/",views.share_quiz,name='share'),
    path("play/<uuid:track_id>/",views.play_quiz,name='play'),
    path('play_color/<uuid:track_id>/',views.play_color,name='play_color'),
    path('play_flower/<uuid:track_id>/',views.play_flower,name='play_flower'),
    path('play_place/<uuid:track_id>/',views.play_place,name='play_place'),
    path('play_hobbies/<uuid:track_id>/',views.play_hobbies,name='play_hobbies'),
    path('play_mood/<uuid:track_id>/',views.play_mood,name='play_mood'),
    path('play_subject/<uuid:track_id>/',views.play_subject,name='play_subject'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('aboutus/',views.about_us,name='about_us'),
    path('privacy_policy',views.privacy_policy,name='privacy_policy'),
    path('physics_quiz/<uuid:track_id>/',views.physics_quiz,name='physics_quiz'),
    path('physicscal/<uuid:track_id>/',views.physicscal_view,name='physicscal'),
    path('car_quiz/',views.car_quiz,name='car'),
    path('movie_quiz/',views.movie_quiz,name='movie'),
    path('chemistry_quiz/',views.chemistry_quiz,name='chemistry'),
    path('car_quiz/<uuid:track_id>/',views.car_quiz,name='car'),
    path('movie_quiz/<uuid:track_id>/',views.movie_quiz,name='movie'),
    path('chemistry_quiz/<uuid:track_id>/',views.chemistry_quiz,name='chemistry'),
    
    
]