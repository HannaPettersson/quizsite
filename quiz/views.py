#coding: utf-8
from django.shortcuts import render
from quiz.models import Quiz

quizzes = {
	"klassiker": {
   		"name": u"Klassiska böcker",
	   	"description": u"Hur bra kan du dina klassiker?", 
	   	"image": "katt1.jpg"
	},

	"fotboll": {
	   	"name": u"Största fotbollslagen",
	   	"description": u"Kan du dina lag?",
	   	"image": "katt2.jpg"
	},
	"kanda-hackare": {
	    	"name": u"Världens mest kända hackare",
	    	"description": u"Hackerhistoria är viktigt, kan du den?",
	    	"image": "katt3.jpg"
	},
}

def startpage(request):
	context = {
	    "quizzes": Quiz.objects.all(),
	}

	return render(request, "quiz/index.html", context)

def quiz(request, slug):
	context = {
	    	"quiz": Quiz.objects.get(slug=slug),
	}
	return render(request, "quiz/quiz.html", context)

def question(request, slug, number):
	context = {
		"question_number": number,
	    	"question": u"Hur många bultar har ölandsbron?",
		"answer1": u"12",
	   	"answer2": u"66 400",
	    	"answer3": u"7 428 954",
	    	"quiz_slug": slug,
	}
	return render(request, "quiz/question.html", context)

def completed(request, slug):
	context = {
	    	"correct": 12,
	    	"total": 20,
			"quiz_slug": slug,
	}
	return render(request, "quiz/result.html", context)

# Create your views here.
