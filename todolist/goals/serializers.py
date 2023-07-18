from rest_framework import serializers


from goals.models import GoalCategory

class GoalCategorySerializer(serializers.ModelSerializer)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        read_only_field = ('id', 'created', 'updated', 'user')
        fields = '__all__'