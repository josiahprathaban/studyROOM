from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.utils import timezone

from room.models import Question, Answer


def login_user(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('room:index')
    else:
        return render(request, 'login/login.html', {'error': True})


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    top_question_list = Question.objects.order_by('-ans_count')[:5]
    context = {
        'user': request.user,
        'latest_question': latest_question_list,
        'top_question': top_question_list,
    }
    return render(request, 'room/index.html', context)


def update_question(request):
    question = Question(user=request.user, question_text=request.POST['question'], key_words=request.POST['key'],
                        pub_date=timezone.now())
    question.save()
    return redirect('room:index')


def update_answer(request, question_id):
    answer = Answer(user=request.user, question_id=question_id, answer_text=request.POST['answer'],
                    pub_date=timezone.now())
    question = Question.objects.get(pk=question_id)
    question.ans_count = question.ans_count + 1
    question.save()
    answer.save()
    return redirect('room:index')


def search(request):
    search_list = Question.objects.filter(key_words__contains=request.POST['search'])
    context = {
        'user': request.user,
        'search_question': search_list,
        'key': request.POST['search'],
    }
    return render(request, 'room/search.html', context)
