from django.contrib import admin

from goals.models import GoalCategory, Goal, GoalComment


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'updated')
    search_fields = ('title', 'user')


class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'updated', 'goal')
    search_fields = ('goal', 'user')


class GoalAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'description', 'due_date', 'status', 'priority', 'created', 'updated')
    search_fields = ('category', 'title', 'description')

admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(GoalComment, GoalCommentAdmin)
