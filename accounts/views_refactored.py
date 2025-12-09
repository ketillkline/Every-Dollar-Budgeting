from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.views import View
from utils.classes import Budget
from accounts.static.accounts.database import Expense

class ExpenseView(View):
    template_name = "expenses.html"

    def get(self, request: HttpRequest):
        expenses = Expense.objects.all().order_by("-date")
        return render(request, self.template_name, {"expenses": expenses})

    def post(self, request: HttpRequest):
        action = request.POST.get("action")

        match action:
            case "clear_all":
                return self.clear_all(request)
            case "clear_single":
                return self.clear_single(request)
            case "edit":
                return self.edit(request)
            case "cancel":
                return self.cancel(request)
            case "add":
                return self.add(request)
            case "add_edited":
                return self.add_edited(request)



    def clear_all(self, request: HttpRequest):
        pass
    def clear_single(self, request: HttpRequest):
        pass
    def edit(self, request: HttpRequest):
        pass
    def cancel(self, request: HttpRequest):
        pass
    def add(self, request: HttpRequest):
        pass
    def add_edited(self, request: HttpRequest):
        pass
