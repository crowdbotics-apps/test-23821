from django.contrib import admin
from .models import (
    Message,
    ThreadMember,
    MessageAction,
    ThreadAction,
    ForwardedMessage,
    Thread,
)

admin.site.register(Thread)
admin.site.register(ThreadMember)
admin.site.register(MessageAction)
admin.site.register(ThreadAction)
admin.site.register(Message)
admin.site.register(ForwardedMessage)

# Register your models here.
