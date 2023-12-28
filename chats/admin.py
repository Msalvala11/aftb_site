from django.contrib import admin
from .models import Conversation, Prompts_and_Responses

admin.site.register(Conversation)
admin.site.register(Prompts_and_Responses)