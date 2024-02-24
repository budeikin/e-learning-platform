from rest_framework.serializers import ModelSerializer, RelatedField
from courses.models import Subject, Course, Module, Content


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']


class ModuleSerializer(ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description']


class CourseSerializer(ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules']


class ItemRelatedField(RelatedField):
    def to_representation(self, value):
        return value.render()


class ContentSerializer(ModelSerializer):
    content = ItemRelatedField(read_only=True)

    class Meta:
        model = Content
        fields = ['order', 'content']


class ModuleWithContentSerializer(ModelSerializer):
    contents = ContentSerializer(many=True)

    class Meta:
        model = Module
        fields = ['order', 'title', 'description', 'contents']


class CourseWithContentSerializer(ModelSerializer):
    modules = ModuleWithContentSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug',
                  'overview', 'created', 'owner',
                  'modules']
