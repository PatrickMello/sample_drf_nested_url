from rest_framework import serializers

from core.models import Entry, Comment


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'title', 'content', 'created_at',)
        read_only_fields = ('created_at', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'created_at', 'entry')
        read_only_fields = ('created_at', 'entry')

    def save(self, **kwargs):
        return super().save(**self.context.get('extras'))
        