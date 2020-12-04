from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.mail import send_mail
from room.models import Question, Answer


def login_user(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('room:index')
    else:
        return render(request, 'login/login.html', {'error': True})


def index(request):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        top_question_list = Question.objects.order_by('-ans_count')[:5]
        context = {
            'user': request.user,
            'latest_question': latest_question_list,
            'top_question': top_question_list,
        }
        return render(request, 'room/index.html', context)


def update_question(request):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        question = Question(user=request.user, question_text=request.POST['question'], key_words=request.POST['key'],
                            pub_date=timezone.now())
        question.save()
        user_mail = User.objects.exclude(email=request.user.email).values_list("email", flat=True)
        send_mail(
        'studyROOM Notifications',
        str(request.user)+' posted a new Question in studyROOM just now. \nIf you can, just give him an answer : http://josiah.pythonanywhere.com/'+str(question.id)+'/question',
        'josiah.prathaban@gmail.com',
        user_mail,
        fail_silently=False,)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def update_answer(request, question_id):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        answer = Answer(user=request.user, question_id=question_id, answer_text=request.POST['answer'],
                        pub_date=timezone.now())
        question = Question.objects.get(pk=question_id)
        question.ans_count = question.ans_count + 1
        question.save()
        answer.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search(request):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        s1 = Question.objects.filter(key_words__contains=request.POST['search'])
        s2 = Question.objects.filter(question_text__contains=request.POST['search'])
        search_list = s1.union(s2)
        context = {
            'user': request.user,
            'search_question': search_list,
            'key': request.POST['search'],
        }
        return render(request, 'room/search.html', context)


def like(request, answer_id):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        answer = Answer.objects.get(pk=answer_id)
        answer.votes = answer.votes + 1
        answer.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def your_question(request):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        question_list = Question.objects.filter(user=request.user)
        context = {
            'user': request.user,
            'question_list': question_list,
        }
        return render(request, 'room/your_questions.html', context)


def your_answer(request):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        answer_list = Answer.objects.filter(user=request.user)
        context = {
            'user': request.user,
            'answer_list': answer_list,
        }
        return render(request, 'room/your_answers.html', context)


def latest_questions(request):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        latest_question_list = Question.objects.order_by('-pub_date')
        context = {
            'user': request.user,
            'question_list': latest_question_list,
        }
        return render(request, 'room/latest_questions.html', context)


def top_questions(request):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        top_question_list = Question.objects.order_by('-ans_count')
        context = {
            'user': request.user,
            'question_list': top_question_list,
        }
        return render(request, 'room/top_questions.html', context)


def delete_question(request, question_id):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        question = Question.objects.get(pk=question_id)
        question.delete()
        return redirect('room:question')


def delete_answer(request, answer_id):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        answer = Answer.objects.get(pk=answer_id)
        answer.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def to_question(request, question_id):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        question = Question.objects.get(pk=question_id)
        context = {
            'user': request.user,
            'question': question,
        }
        return render(request, 'room/question.html', context)


def to_edit(request, answer_id):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        answer = Answer.objects.get(pk=answer_id)
        context = {
            'user': request.user,
            'answer': answer,
            'edit': True,
            'question': answer.question,
        }
        return render(request, 'room/question.html', context)


def edit_answer(request, answer_id):
    if request.user.is_anonymous:
        return redirect('login:index')
    else:
        answer = Answer.objects.get(pk=answer_id)
        answer.answer_text = request.POST['answer']
        answer.pub_date = timezone.now()
        answer.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
