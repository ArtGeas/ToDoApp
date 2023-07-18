from rest_framework import serializers


from goals.models import GoalCategory
from core.serializers import UserSerializer

class GoalCategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        read_only_field = ('id', 'created', 'updated', 'user')
        fields = '__all__'


class GoalCategorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = GoalCategory
        fields = '__all__'
        read_only_field = ('id', 'created', 'updated', 'user')
