from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from goals.models import GoalCategory, Goal, Status, GoalComment
from goals.serializers import GoalCategoryCreateSerializer, GoalCategorySerializer, GoalCreateSerializer, GoalSerializer, GoalCommentCreateSerializer, GoalCommentSerializer
from goals.filters import GoalDateFilter

class GoalCategoryCreateView(CreateAPIView):
    model = GoalCategory
    permission_classes = [IsAuthenticated]
    serializer_class = GoalCategoryCreateSerializer


class GoalCategoryListView(ListAPIView):
    model = GoalCategory
    permission_classes = [IsAuthenticated]
    serializer_class = GoalCategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title"]
    def get_queryset(self):
        return GoalCategory.objects.filter(
            user=self.request.user, is_deleted=False
        )


class GoalCategoryView(RetrieveUpdateDestroyAPIView):
    model = GoalCategory
    serializer_class = GoalCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GoalCategory.objects.filter(user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.status = Status.archived
        instance.save()
        return instance


class GoalCreateView(CreateAPIView):
    model = Goal
    serializer_class = GoalCreateSerializer
    permission_classes = [IsAuthenticated]


class GoalListView(ListAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    filterset_class = GoalDateFilter
    ordering = ['title']
    ordering_fields = ['title', 'created', 'category', 'priority', 'due_date']
    search_fields = ['title', 'description']

    def get_queryset(self):
        return Goal.objects.filter(user = self.request.user,
                                   category__is_deleted=False).exclude(status=Status.archived)


class GoalView(RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(category__is_deleted=False).exclude(status=Status.archived)

    def perform_destroy(self, instance):
        instance.status = Status.archived
        instance.save()


class GoalCommentCreateView(CreateAPIView):
    model = GoalComment
    serializer_class = GoalCommentCreateSerializer
    permission_classes = [IsAuthenticated]


class GoalCommentListView(ListAPIView):
    model = GoalComment
    serializer_class = GoalCommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    filterset_fields = ['goal']
    ordering = ['-created']
    search_fields = ['title', 'text']

    def get_queryset(self):
        return GoalComment.objects.filter(user = self.request.user)


class GoalCommentView(RetrieveUpdateDestroyAPIView):
    model = GoalComment
    serializer_class = GoalCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GoalComment.objects.filter(user = self.request.user)
