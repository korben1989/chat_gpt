from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Answers, Answers1, Answers2
from openai import OpenAI

def messagefunc(message):
    opai = "sk-proj-YgIDj7agHzUqukmF75ozT3BlbkFJP3HNZLMzXUoLWhTQySLd"
    client = OpenAI(
        # organization='org-nVNzaT3XsSVhj9KF02qSnOnl',
        # project='Default Project',
        api_key=opai
    )

    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message}],
        stream=True,
    )
    a = ''
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            a += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")
    return a

class IndexPageView(TemplateView):
    template_name = 'GPT_app/index/index.html'

def p2(request):
    a = messagefunc(request.GET['text'])
    try:
        Answers.objects.get(user_cookies=request.COOKIES['csrftoken'])
        Answers.objects.filter(user_cookies=request.COOKIES['csrftoken']).update(a2=request.GET['text'])
    except:
        Answers.objects.create(user_cookies=request.COOKIES['csrftoken'], a2=request.GET['text'])

    Answers.objects.filter(user_cookies=request.COOKIES['csrftoken']).update(q2=a)
    return render(request, 'GPT_app/index/index2.html', {'obj': a})

def p3(request):
    # Answers1.objects.create(user_cookies=request.COOKIES['csrftoken'], a2=request.GET['text'])
    # a = messagefunc(request.GET['text'])
    # Answers1.objects.update_or_create(user_cookies=request.COOKIES['csrftoken'], q2=a)
    a = messagefunc(request.GET['text'])
    try:
        Answers1.objects.get(user_cookies=request.COOKIES['csrftoken'])
        Answers1.objects.filter(user_cookies=request.COOKIES['csrftoken']).update(a2=request.GET['text'])
    except:
        Answers1.objects.create(user_cookies=request.COOKIES['csrftoken'], a2=request.GET['text'])

    Answers1.objects.filter(user_cookies=request.COOKIES['csrftoken']).update(q2=a)
    return render(request, 'GPT_app/index/index3.html', {'obj': a})

def p4(request):
    a = messagefunc(request.GET['text'])
    try:
        Answers2.objects.get(user_cookies=request.COOKIES['csrftoken'])
        Answers2.objects.filter(user_cookies=request.COOKIES['csrftoken']).update(a2=request.GET['text'])
    except:
        Answers2.objects.create(user_cookies=request.COOKIES['csrftoken'], a2=request.GET['text'])

    Answers2.objects.filter(user_cookies=request.COOKIES['csrftoken']).update(q2=a)
    return render(request, 'GPT_app/index/index4.html', {'obj': a})
