from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

def free(request):
    return render(request, 'polls/freelancer.html', {})

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return render(request, 'polls/index.html', {'latest_question_list':latest_question_list})
    # return HttpResponse(output)

def detail(request, question_id): # 질문 상세 페이지
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id): # 투표 결과 페이지
    votess = Question.objects.get(pk=question_id).choice_set.all()
    # choices = Question.objects.get(pk=question_id).Choice.objects.filter(question=question) 이것도 위와 같다.
    response = "You're looking at the results of question %s." % question_id
    return render(request, 'polls/vote.html', {'votess':votess, 'response':response})

def vote(request, question_id): # 투표 페이지
    num = request.POST['choice']
    choice = Choice.objects.get(pk=num)
    vote = choice.votes + 1 # 투표수 1 증가
    choice.votes = vote
    choice.save()

    return HttpResponse("You're voting on question %s." % question_id)

def qnvote(request, question_id):
    
    return render(request, 'polls/qsvote.html', {'question_id':question_id})