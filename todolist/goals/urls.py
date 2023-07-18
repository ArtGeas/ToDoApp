from django.urls import path

from goals.views import GoalCategoryCreateView

urlpatterns = [
    path('goal_category/create', GoalCategoryCreateView.as_view()),
]