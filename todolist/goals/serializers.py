from rest_framework import serializers


from goals.models import GoalCategory, Goal
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


class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        fields = ('category', 'title', 'description', 'due_date', 'status', 'priority')
        read_only_fields = ('category', 'title', 'description', 'due_date', 'status', 'priority')

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError('not allowed in deleted category')

        if value.user != self.context['request'].user:
            raise serializers.ValidationError('not owner of the category')

        return value



class GoalSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Goal
        fields = ('id', 'user', 'created', 'updated', 'title', 'description', 'due_date', 'status', 'priority', 'category')
        read_only_fields = ('id', 'user', 'created', 'updated', 'title', 'description', 'due_date', 'status', 'priority', 'category')
