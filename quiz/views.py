#coding: utf-8
from django.shortcuts import render

quizzes = {
	"klassiker": {
   		"name": u"Klassiska böcker",
	   	"description": u"Hur bra kan du dina klassiker?"
	},

	"fotboll": {
	   	"name": u"Största fotbollslagen",
	   	"description": u"Kan du dina lag?"
	},
	"kanda-hackare": {
	    	"name": u"Världens mest kända hackare",
	    	"description": u"Hackerhistoria är viktigt, kan du den?"
	},
}

def startpage(request):
	return render(request, "quiz/index.html")

def quiz(request):
	return render(request, "quiz/quiz.html")

def question(request):
	return render(request, "quiz/question.html")

def completed(request):
	return render(request, "quiz/result.html")

# Create your views here.
