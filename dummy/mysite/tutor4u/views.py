from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Question, User, Choice, Profile
from django.template import loader
from django.urls import reverse
from .forms import PostForm

# Create your views here


def index(request):
    if request.user is not None and request.user.is_authenticated:
        return render(request, 'tutor4u/index.html', context={'user': request.user})
    else:
        return render(request, 'tutor4u/index.html')


def signup_complete(request):
    return render(request, 'tutor4u/signup_complete.html')


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'tutor4u/detail.html', {'question': question})


def results(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request,'tutor4u/results.html',{'user': user})


def tutorresults(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request,'tutor4u/tutorresults.html',{'user': user})


def user_login(request):
    if request.method == 'GET':
        return render(request, 'tutor4u/login.html')
    elif request.method == 'POST':
        print(request.POST)
        username = request.POST['userid']
        password = request.POST['pswrd']

        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect(reverse('tutor4u:index'))
        else:
            return render(request, 'tutor4u/login.html', context={'error': 'Invalid username or password'})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        text = request.POST['test']
        print(text)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'tutor4u/detail.html', {

            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('tutor4u:results', args=(question.id,)))


def about(request):
    return render(request, 'tutor4u/about.html')

def locations(request):
    return render(request, 'tutor4u/locations.html')

def subjects(request):
    return render(request, 'tutor4u/subjects.html')

def lv(request):
    return render(request, 'tutor4u/lv.html')

def tutee_signup(request):
    if request.method == 'GET':
        return render(request, 'tutor4u/sign2.html')
    elif request.method == 'POST':
        print(request.POST)
        id = Profile.objects.all().order_by('-user_id')[0].user_id
        q = Profile(user_id=id+1, name=request.POST['user_name'], email=request.POST['user_email'],
                 password=request.POST['user_password'], biography=request.POST['user_bio'],
                 major=request.POST['user_major'], currentyear=request.POST['currentyear'],
                 gender=request.POST['user_gender'])
        q.save()
        print(q)
        return HttpResponseRedirect(reverse('tutor4u:index'))


def tutor_signup(request):
    if request.method == 'GET':
        return render(request, 'tutor4u/tutor_signup.html')
    elif request.method == 'POST':
        print(request.POST)
        id = Profile.objects.all().order_by('-user_id')[0].user_id
        q = Profile(user_id=id+1, name=request.POST['user_name'], email=request.POST['user_email'],
                 password=request.POST['user_password'], biography=request.POST['user_bio'],
                 major=request.POST['user_major'], currentyear=request.POST['currentyear'],
                 gender=request.POST['user_gender'], course1=request.POST['option1'], grade1=request.POST['grade1'],
                 course2=request.POST['option2'], grade2=request.POST['grade2'], course3=request.POST['grade3'],
                 grade3=request.POST['option3'])
        q.save()
        print(q)
        return HttpResponseRedirect(reverse('tutor4u:index'))


def signup_action(request):
    q = Profile(name=request.POST['user_name'],email=request.POST['user_email'],password=request.POST['user_password'],gender=request.POST['user_gender'],biography=request.POST['user_bio'],major=request.POST['user_major'],currentyear=request.POST['currentyear'])
    q.save()
    print(q.id)
    return HttpResponseRedirect(reverse('tutor4u:results',args=(q.id,)))


def form_upload(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleaned_data['created_at']
            post = m.Post.objects.create(content=content,
                                         created_at=created_at)
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id': post.id}))
 
    return render(request, 'tutor4u/form_upload.html', {
        'form': form,
    })
