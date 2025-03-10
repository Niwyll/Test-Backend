from django.views.generic import ListView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from icecreams.models import IceCreamBucket, Recipe

class ManagementRecipesView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Recipe
    permission_required = "is_superuser"

    def handle_no_permission(self):
        return redirect("seller:home")

class ManagementBucketsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = IceCreamBucket
    permission_required = "is_superuser"

    def handle_no_permission(self):
        return redirect("seller:home")
