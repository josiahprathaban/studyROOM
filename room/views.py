from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.utils import timezone

from room.models import Question, Answer


def index(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return content(user, request)
    else:
        return render(request, 'login/login.html', {'error': True})


def update_question(request):
    question = Question(user=request.user, question_text=request.POST['question'], key_words=request.POST['key'],
                        pub_date=timezone.now())
    question.save()
    return content(request.user, request)


def update_answer(request, question_id):
    answer = Answer(user=request.user, question_id=question_id, answer_text=request.POST['answer'],
                    pub_date=timezone.now())
    question = Question.objects.get(pk=question_id)
    question.ans_count = question.ans_count + 1
    question.save()
    answer.save()
    return content(request.user, request)


def content(user, request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    top_question_list = Question.objects.order_by('-ans_count')[:5]
    context = {
        'user': user,
        'latest_question': latest_question_list,
        'top_question': top_question_list,
    }
    return render(request, 'room/index.html', context)
