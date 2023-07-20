from rest_framework import serializers


from goals.models import GoalCategory, Goal
from core.serializers import UserSerializer

class GoalCategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        read_only_field = ('id', 'created', 'updated', 'user')
        fields = '__all__'


class GoalCategorySerializer(GoalCategoryCreateSerializer):
    user = UserSerializer(read_only=True)


class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated', 'user')

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError('not allowed in deleted category')

        if value.user != self.context['request'].user:
            raise serializers.ValidationError('not owner of the category')

        return value



class GoalSerializer(GoalCreateSerializer):
    user = UserSerializer(read_only=True)
