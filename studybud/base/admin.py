from django.contrib import admin

# Register your models here.
 
   #The room model is not  seen in the database hence we register it in  the admin.py 

from  .models import Room, Topic, Message, User

admin.site.register(Room)  
admin.site.register(User) 
admin.site.register(Topic)
admin.site.register(Message)