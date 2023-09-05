from django.contrib import admin

from follow_app.models import Comment, Coordinator, Member, TeamMember

# Register your models here.
admin.site.register(Member)
admin.site.register(Comment)
admin.site.register(Coordinator)
admin.site.register(TeamMember)

