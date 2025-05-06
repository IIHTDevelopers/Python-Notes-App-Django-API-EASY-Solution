
from django.contrib import admin
from django.urls import path,re_path
from notesapp.views import NotesCRUDView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes_crud/',NotesCRUDView.as_view()),
    path('notes_crud_pk/<int:pk>/',NotesCRUDView.as_view())
]
