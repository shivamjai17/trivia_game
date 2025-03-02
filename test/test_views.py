from django.test import TestCase, Client
from django.urls import reverse
from game.models import Destination
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import JsonResponse
import json

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.destination = Destination.objects.create(
            city="Paris",
            clues=["Eiffel Tower", "Louvre Museum"],
            fun_fact=["Paris is known as the City of Lights."]
        )

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "game/home.html")

    def test_set_username(self):
        response = self.client.post(
            reverse("set_username"),
            json.dumps({"username": "testuser"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Username saved successfully!")

    def test_get_random_clues(self):
        response = self.client.get(reverse("get_random_clues"))
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertIn("clues", json_data)
        self.assertIn("options", json_data)
        self.assertIn("correct_answer", json_data)
        self.assertEqual(json_data["correct_answer"], "Paris")

    def test_get_csrf_token(self):
        response = self.client.get(reverse("get_csrf_token"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("csrfToken", response.json())

    def test_check_answer_correct(self):
        session = self.client.session
        session["score"] = {"correct": 0, "incorrect": 0}
        session.save()

        response = self.client.post(
            reverse("check_answer"),
            json.dumps({"user_answer": "Paris", "correct_answer": "Paris", "fun_fact": "City of Lights"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], "correct")
        self.assertEqual(response.json()["score"]["correct"], 1)

    def test_check_answer_incorrect(self):
        session = self.client.session
        session["score"] = {"correct": 0, "incorrect": 0}
        session.save()

        response = self.client.post(
            reverse("check_answer"),
            json.dumps({"user_answer": "Berlin", "correct_answer": "Paris", "fun_fact": "City of Lights"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], "incorrect")
        self.assertEqual(response.json()["score"]["incorrect"], 1)

    def test_generate_invite_link(self):
        session = self.client.session
        session["username"] = "testuser"
        session["score"] = {"correct": 5, "incorrect": 2}
        session.save()

        response = self.client.get(reverse("generate_invite_link"))
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertIn("invite_link", json_data)
        self.assertIn("Challenge your friend!", json_data["message"])
