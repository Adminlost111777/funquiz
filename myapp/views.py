from uuid import uuid4

from django.shortcuts import get_object_or_404,render, redirect, reverse
from django.http import HttpResponse
from django.views import View

from . models import Color, Place, Currentmood, Hobbies, Subjects, Flowers, QuizModel, SessionUser,Blog,AnswerModel,QuizModel

def get_session_user(request):
    track_id_session = request.session.get("track_id")
    if not track_id_session:
        track_id = uuid4()
        request.session['track_id'] = str(track_id)
        print("New session created with track_id:", track_id)
        track_id_session = track_id
    
    session_user, created = SessionUser.objects.get_or_create(
        track_id=track_id_session,
        defaults={'username': 'Guest'}
    )
    return session_user

def contact_us(request):
    return render(request,'contact_us.html')

def about_us(request):
    return render(request,'about_us.html')

def privacy_policy(request):
    return render(request,'privacy_policy.html')


def create_quiz(request):
    """
    1. When user goes to /create-quiz page lets create a quiz model
        than pass track id in link
    2. We will use same track id to access quiz model in other pages 
    """
    session_user = get_session_user(request)
    print("session_user: ", session_user)
    # You need sessionuser because irt sis compulsory but not track_id because ited
    quiz = QuizModel.objects.create(session_user=session_user)
    print("Created: " , quiz)

    redirect_url = reverse('color', kwargs={'track_id': quiz.track_id})
    print("Redirect: ",redirect_url)
    return redirect(redirect_url)



def results(request, quiz_id):
    quiz = get_object_or_404(QuizModel, id=quiz_id)
    answers = quiz.answers.all()
    return render(request, "results.html", {"quiz": quiz, "answers": answers})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request,"blog.html",{"blogs": blogs})

def blog_detail(request, path):
    blog = get_object_or_404(Blog, slug=path) 
    context = {'blog': blog}
    return render(request, 'blog_detail.html', context)

def quiz_view(request):
    session_user = get_session_user(request)
    print("SessionUser:", session_user)

    if request.method == "POST":
        print("User is trying to update or save")
        print("POST data:", request.POST)
        new_username = request.POST.get("username")
        session_user.username = new_username
        session_user.save()
        print("Username Saved :",session_user.username)

    return render(request, 'quiz.html', {'session_user': session_user})

def color(request, track_id):
   print(track_id)
   colors= Color.objects.all()
   quiz = QuizModel.objects.get(track_id=track_id)
   print("quiz: ",quiz)
   if request.method == "POST":
       color_id = request.POST.get('color_id')
       print("id:",color_id)
       quiz.favorite_color_answer = color_id
       quiz.save()

       # We saved answer, now what next answer we want? we need to redurect there
       redirect_url = reverse('flower', kwargs={'track_id': quiz.track_id})
       return redirect(redirect_url)

   return render(request,'color.html',{'colors':colors})

def Flower_view(request,track_id):
    print(track_id)
    flowerss= Flowers.objects.all()
    quiz = QuizModel.objects.get(track_id=track_id)
    print("quiz: ",quiz)
    if request.method == "POST":
        flower_id = request.POST.get('flower_id')
        print("id:",flower_id)
        quiz.favorite_flower_answer = flower_id
        quiz.save()

        redirect_url = reverse('place', kwargs={'track_id': quiz.track_id})
        return redirect(redirect_url)
    
    return render(request,'flower.html',{'flowerss':flowerss})

# Create your views here. fix this how make this workinfg like above copy like above
def Place_view(request,track_id):
      print(track_id)
      places= Place.objects.all()
      quiz = QuizModel.objects.get(track_id=track_id)
      print("quiz: ",quiz)
      if request.method == "POST":
          place_id = request.POST.get('place_id')
          print("id:",place_id)
          quiz.favorite_place_answer = place_id
          quiz.save()

          redirect_url = reverse('hobbies', kwargs={'track_id': quiz.track_id})
          return redirect(redirect_url)
   #  places = get_object_or_404(color, pk=pk)
      return render(request,'place.html',{'places':places})

def Hobbies_view(request,track_id):
    print(track_id)
    hobbiess= Hobbies.objects.all()
    quiz = QuizModel.objects.get(track_id=track_id)
    print("quiz:" ,quiz)
    if request.method == "POST":
        hobbies_id = request.POST.get('hobbies_id')
        print("id:",hobbies_id)
        quiz.favorite_hobby_answer = hobbies_id
        quiz.save()

        redirect_url = reverse('currentmood', kwargs={'track_id': quiz.track_id})
        return redirect(redirect_url)
    return render(request,'hobbies.html',{'hobbiess':hobbiess})

def Currentmood_view(request,track_id):
    print(track_id)
    currentmoods= Currentmood.objects.all()
    quiz = QuizModel.objects.get(track_id=track_id)
    print("quiz: ",quiz)    
    if request.method == "POST":
        currentmood_id = request.POST.get('currentmood_id')
        print("id:",currentmood_id)
        quiz.current_mood_answer = currentmood_id
        quiz.save()

        redirect_url = reverse('subject', kwargs={'track_id': quiz.track_id})
        return redirect(redirect_url)
    return render(request,'currentmood.html',{'currentmoods':currentmoods})



def Subject_view(request,track_id):
    print(track_id)
    subjects= Subjects.objects.all()
    quiz = QuizModel.objects.get(track_id=track_id)
    print("quiz: ",quiz)
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        print("id:",subject_id)
        quiz.favorite_subject_answer = subject_id
        quiz.save()

        # We saved answer, now what next answer we want? we need to redurect there
        redirect_url = reverse('share', kwargs={'track_id': quiz.track_id})
        return redirect(redirect_url)
    return render(request,'subject.html',{'subjects':subjects})

def play_quiz(request,track_id):
    # session_user = get_session_user(request)
    # print session_user
    # quiz = QuizModel.objects.get(track_id=track_id)
    # answer_model = AnswerModel.objects.create(...see above example)
    # answer_track_id = answer_model.track_id
    # print this
    # this is current user who is answering
    session_user = get_session_user(request)
    print("session user: ",session_user)
    quiz = QuizModel.objects.get(track_id=track_id)
    answer_model = AnswerModel.objects.create(quiz=quiz,answered_by=session_user) # left field name should be same as declared in model
    answer_track_id = answer_model.track_id
    print("answer trackid: ",answer_track_id)
    redirect_url = reverse('play_color', kwargs={'track_id': answer_track_id})
    return redirect(redirect_url)
    

def play_color(request,track_id):
    print(track_id)

    colors= Color.objects.all()
    answer_model = AnswerModel.objects.get(track_id=track_id)
    print("quiz: ", answer_model)
    if request.method == "POST":
        color_id = request.POST.get('color_id')
        print("id:",color_id)
        answer_model.favorite_color_answer = color_id
        answer_model.save()

        # comment for
        # redirect_url = reverse('play_flower', kwargs={'track_id': answer_model.track_id})
        # return redirect(redirect_url)
        redirect_url = reverse('play_flower', kwargs={'track_id': answer_model.track_id})
        return redirect(redirect_url)

    return render(request,'color.html',{'colors':colors})
def play_flower(request,track_id):
    print(track_id)
     
    flowerss= Flowers.objects.all()
    answer_model = AnswerModel.objects.get(track_id=track_id)
    print("quiz: ",answer_model)
    if request.method == "POST":
        flower_id = request.POST.get('flower_id')
        print("id:",flower_id)
        answer_model.favorite_flower_answer = flower_id
        answer_model.save()

        redirect_url = reverse('play_place', kwargs={'track_id': answer_model.track_id})
        return redirect(redirect_url)
    
    return render(request,'flower.html',{'flowerss':flowerss})

def play_place(request,track_id):
    print(track_id)
     
    places= Place.objects.all()
    answer_model = AnswerModel.objects.get(track_id=track_id)
    print("quiz: ",answer_model)
    if request.method == "POST":
        place_id = request.POST.get('place_id')
        print("id:",place_id)
        answer_model.favorite_place_answer = place_id
        answer_model.save()

        redirect_url = reverse('play_hobbies', kwargs={'track_id': answer_model.track_id})
        return redirect(redirect_url)
    
    return render(request,'place.html',{'places':places})

def play_hobbies(request,track_id):
    print(track_id)
     
    hobbiess = Hobbies.objects.all()
    answer_model = AnswerModel.objects.get(track_id=track_id)
    print("quiz: ",answer_model)
    if request.method == "POST":
        hobbies_id = request.POST.get('hobbies_id')
        print("id:",hobbies_id)
        answer_model.favorite_hobby_answer = hobbies_id
        answer_model.save()

        redirect_url = reverse('play_mood', kwargs={'track_id': answer_model.track_id})
        return redirect(redirect_url)
    
    return render(request,'hobbies.html',{'hobbiess':hobbiess})

def play_mood(request,track_id):
    print(track_id)
     
    currentmoods = Currentmood.objects.all()
    answer_model = AnswerModel.objects.get(track_id=track_id)
    print("quiz: ",answer_model)
    if request.method == "POST":
        currentmood_id = request.POST.get('currentmood_id')
        print("id:",currentmood_id)
        answer_model.current_mood_answer = currentmood_id
        answer_model.save()

        redirect_url = reverse('play_subject', kwargs={'track_id': answer_model.track_id})
        return redirect(redirect_url)
    
    return render(request,'currentmood.html',{'currentmoods':currentmoods})

def play_subject(request,track_id):
    print(track_id)
     
    subjects = Subjects.objects.all()
    answer_model = AnswerModel.objects.get(track_id=track_id)
    print("quiz: ",answer_model)
    # this yes but I prefer u write urslef
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        print("id:",subject_id)
        answer_model.favorite_subject_answer = subject_id
        answer_model.save()

        redirect_url = reverse('calculator', kwargs={'track_id': answer_model.track_id})
        return redirect(redirect_url)
    
    return render(request,'subject.html',{'subjects':subjects})


def share_quiz(request,track_id):
    quiz = QuizModel.objects.get(track_id=track_id)
    
    return render(request,'share.html',{'quiz':quiz})

def calculator_view(request,track_id):
    # Access anser model
    answer_model = AnswerModel.objects.get(track_id=track_id)
    print("id: ",answer_model)
    print(answer_model.quiz)
    print('This user created question:', answer_model.quiz.session_user)
    print('right answer is:',answer_model.quiz.favorite_color_answer) # Real answer
    print('answered by:',answer_model.answered_by)
    print('answer is: ',answer_model.favorite_color_answer) # User answred

    quiz = answer_model.quiz

    total_question = 6
    point = 0

    if quiz.favorite_color_answer == answer_model.favorite_color_answer:
        point += 1
    if quiz.favorite_flower_answer == answer_model.favorite_flower_answer:
        point += 1
    if quiz.favorite_hobby_answer == answer_model.favorite_hobby_answer:
        point += 1
    if quiz.favorite_place_answer == answer_model.favorite_place_answer:
        point += 1
    if quiz.favorite_subject_answer == answer_model.favorite_subject_answer:
        point += 1
    if quiz.current_mood_answer == answer_model.current_mood_answer:
        point += 1

    percentage = round((point * 100.0)/6, 2)
    return render(request,'calculator.html',{'percentage':percentage})
