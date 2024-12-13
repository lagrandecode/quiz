from django.contrib import admin

from .models import Question, Responses, Result

# Register your models here.
admin.site.register(Question)
admin.site.register(Responses)
admin.site.register(Result)
