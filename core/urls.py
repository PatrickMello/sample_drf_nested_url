"""nested_urls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from core import views


urlpatterns = [
    path("entries", views.EntryListCreateView.as_view(), name="entry_list"),
    path(
        "entry/<int:pk>", views.EntryRetrieveUpdateView.as_view(), name="entry_update"
    ),
    path(
        "entry/<int:entry_id>/comments",
        views.CommentListCreateView.as_view(),
        name="comments_list",
    ),
    path(
        "entry/<int:entry_id>/comment/<int:pk>",
        views.CommentRetrieveUpdateView.as_view(),
        name="comments_update",
    ),
]
