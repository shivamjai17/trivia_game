# views.py
import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.middleware.csrf import get_token
from game.models import Destination
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    inviter = request.GET.get("inviter", "")
    inviter_score = request.session.get("score", {"correct": 0, "incorrect": 0})
    return render(request, "game/home.html", {"inviter": inviter, "inviter_score": inviter_score})

@csrf_exempt
def set_username(request):
    if request.method == "POST":
        data = json.loads(request.body)
        request.session["username"] = data.get("username")
        return JsonResponse({"message": "Username saved successfully!"})
    return JsonResponse({"error": "Invalid request"}, status=400)

def get_random_clues(request):
    destination = Destination.objects.order_by('?').first()
    all_cities = list(Destination.objects.values_list('city', flat=True))
    random.shuffle(all_cities)
    options = random.sample(all_cities, min(3, len(all_cities)))  
    if destination.city not in options:
        options[random.randint(0, len(options)-1)] = destination.city
    clues = random.sample(destination.clues, min(2, len(destination.clues)))
    return JsonResponse({
        "clues": clues,
        "options": options,
        "correct_answer": destination.city,
        "fun_fact": random.choice(destination.fun_fact)
    })

def get_csrf_token(request):
    return JsonResponse({"csrfToken": get_token(request)})

@csrf_exempt
def check_answer(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_answer = data.get("user_answer")
        correct_answer = data.get("correct_answer")
        fun_fact = data.get("fun_fact")
        if "score" not in request.session:
            request.session["score"] = {"correct": 0, "incorrect": 0}
        if user_answer == correct_answer:
            request.session["score"]["correct"] += 1
            return JsonResponse({
                "result": "correct",
                "message": "🎉 Correct! Well done!",
                "fun_fact": fun_fact,
                "score": request.session["score"]
            })
        else:
            request.session["score"]["incorrect"] += 1
            return JsonResponse({
                "result": "incorrect",
                "message": "😢 Oops! Try again!",
                "fun_fact": fun_fact,
                "score": request.session["score"]
            })

def generate_invite_link(request):
    username = request.session.get("username", "Player")
    score = request.session.get("score", {"correct": 0, "incorrect": 0})
    invite_link = request.build_absolute_uri(f"/?inviter={username}")
    return JsonResponse({
        "invite_link": invite_link,
        "message": f"Challenge your friend! {username} scored {score['correct']} points!"
    })
