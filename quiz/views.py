from django.shortcuts import render

def startpage(request):
	return render(request, "quiz/index.html")

def quiz(request):
	return render(request, "quiz/quiz.html")

def question(request):
	return render(request, "quiz/question.html")

def completed(request):
	return render(request, "quiz/result.html")

# Create your views here.
