from django.urls import path
from . import views

app_name = 'assignmentapp'

urlpatterns = {
    path('',views.list_view, name="list_view")
}