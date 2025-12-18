from django.http import HttpRequest
from django.shortcuts import render, redirect
from accounts.static.accounts.database import Expense, Income
from django.views import View


class BudgetView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "budget.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        pass

    def get_frequency_divider(self):
        return "Test passed"
