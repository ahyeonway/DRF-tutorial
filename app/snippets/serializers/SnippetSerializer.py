from rest_framework import serializers

from ..models import STYLE_CHOICES, LANGUAGE_CHOICES, Snippet


class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        검증한 데이터로 새 `Snippet` 인스턴스를 생성하여 리턴합니다.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        검증한 데이터로 기존 `Snippet` 인스턴스를 업데이트한 후 리턴합니다.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class SnippetSerializer2:
    pk = None
    title = None
    code = None

    def __init__(self, instance):
        # instance가 pk를 가지고 있다면
        if hasattr(instance, 'pk'):
            # self.pk에 instace의 pk
            self.pk = instance.pk
        if hasattr(instance, 'title'):
            self.title = instance.title
        if hasattr(instance, 'code'):
            self.code = instance.code

    @property
    def data(self):
        return {
            'pk': self.pk,
            'title': self.title,
            'code': self.code,
        }