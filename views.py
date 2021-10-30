from django.shortcuts import render
from .quiz import *


def index(request):

    context = {
        'title': 'はじめての Django Web アプリケーション',
    }
    return render(request, 'djangofirst/index.html', context)


def pref_quiz(request):
    prefecture, city, url = prefecture_quiz()
    context = {
        'title': '県庁所在地クイズ',
        'prefecture': prefecture,  
        'city': city,
        'url': url,
    }
    return render(request, 'djangofirst/prefecture_tpl.html', context)


def pref_result(request):
    if request.method == 'POST':
        userinput_city = request.POST['userinput_city']
        prefecture = request.POST['prefecture']
        city = request.POST['city']
        url = request.POST['url']
        
        if city == userinput_city:
            result = '正解です'
        else:
            result = '不正解です'
        
        context = {
            'title': '県庁所在地クイズ － 結果',
            'result': result,
            'prefecture': prefecture,
            'city': city,
            'url': url,
        }
        return render(request, 'djangofirst/prefecture_result.html', context)


def random_quiz(request):
    selected_qa = quiz()
    
    num = [i for i in range(1, 6)]
    question = []
    answer = []
    for i in selected_qa:
        question.append(i[0])
        answer.append(i[1])

    context = {
            'title': 'ランダムクイズ',
            'num': num,
            'question': question,
            'answer': answer,
        }
    return render(request, 'djangofirst/quiz_tpl.html', context)


def quiz_result(request):

    if request.method == "POST":
        score = 0
        user_answer = request.POST.getlist('user_answer')
        answer = request.POST.getlist('answer')
        for i, j in zip(user_answer, answer):
            if i == j:
                score += 20  

        context = {
            'title': 'クイズの結果です',
            'score': score,
            'answer': answer,
            'user_answer': user_answer
            }
        return render(request, 'djangofirst/quiz_result.html', context)


def wiki(request):
    context = {
        'title': 'Python版Wikipediaで調べる',
    }
    return render(request, 'djangofirst/wiki_tpl.html', context) 


def wiki_result(request):
    if request.method == 'GET':
        word = request.GET['word']
        result = wikipy(word)

        context = {
            'title': 'Python版Wikipediaで調べる',
            'result': result,
        }
        return render(request, 'djangofirst/wiki_tpl.html', context) 
        