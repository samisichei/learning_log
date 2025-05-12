from django.urls import path
from . import views  # import views from this app

app_name = 'learning_logs'  # this helps avoid name clashes

urlpatterns = [
    path('', views.index, name='index'),  # this is the homepage
    path('topics/', views.topics, name='topics'), #topics page
    path('topics/<int:topic_id>/', views.topic, name='topic'), # Detail page for a single topic
    path('new_topic/', views.new_topic, name='new_topic'), # Page to add a new topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), #Page for adding a new entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'), # for editing an existing entry
    
]
