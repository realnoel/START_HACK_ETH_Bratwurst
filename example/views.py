from django.shortcuts import render, redirect
from .models import Question, Answer, UserFundsResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return redirect('recommender')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

def questionnaire(request):
    return render(request, 'questionnaire.html')

@login_required
def logout(request):
    logout(request)
    return redirect('login')

@login_required
def recommender(request):
    if request.method == 'POST':
        # Save user's answer to the previous question
        answer_id = request.POST.get('answer')
        answer = Answer.objects.get(id=answer_id)
        user_response = UserFundsResponse(user=request.user, question=answer.question, answer=answer)
        user_response.save()

        # Get the next question
        next_question = Question.objects.exclude(id__in=UserFundsResponse.objects.filter(user=request.user).values('question_id')).first()

        # If there are no more questions, redirect to results page
        if next_question is None:
            return redirect('results')

    else:
        # If method is GET, display the first unanswered question
        next_question = Question.objects.exclude(id__in=UserFundsResponse.objects.filter(user=request.user).values('question_id')).first()
    
    # If there are no more questions, redirect to results page
    if next_question is None:
        return redirect('results')

    # Get possible answers for this question
    answers = Answer.objects.filter(question=next_question)

    # Render the questionnaire page
    return render(request, 'questionnaire.html', {'question': next_question, 'answers': answers})