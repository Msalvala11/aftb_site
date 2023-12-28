from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Conversation(models.Model):
    client_name = models.CharField(max_length=255)
    client_number = PhoneNumberField(blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation with {self.client}"

class Prompts_and_Responses(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    promptResponse = models.CharField(max_length=10, choices={i: i for i in ['prompt', 'response']})
    message = models.TextField()
    
    def __str__(self):
        return f"Prompt: {self.prompt}, Response: {self.response}"