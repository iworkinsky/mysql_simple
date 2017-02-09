from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def detail(request,question_id):
    return HttpResponse("you are loking at question %s" % question_id)
def results(request,question_id):
    response = "You are loking at the resuts of question %s"
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("you are voting on question %s" % question_id)