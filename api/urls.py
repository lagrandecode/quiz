

from .views import QuestionList, QuestionDetail, RegisterView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',QuestionList.as_view()),
    path('<int:pk>/',QuestionDetail.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
