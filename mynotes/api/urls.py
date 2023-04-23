from django.contrib import admin
from django.urls import path
from .views import getRoutes, getNotes, getNote, updateNote, deleteNote, createNote

urlpatterns = [
    path('', getRoutes, name='routes'),
    path('notes/', getNotes, name='notes'),
    path('notes/update/<int:pk>', updateNote, name='updatenote'),
    path('notes/delete/<int:pk>', deleteNote, name='deletenote'),
    path('notes/create/', createNote, name='createNote'),
    path('notes/<int:pk>', getNote, name='note'),   
]