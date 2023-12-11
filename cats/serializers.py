from rest_framework.serializers import ModelSerializer
from .models import Cat
from rest_framework import serializers

class ListCreateCatSerializer(ModelSerializer):
    """
    Сеориализотор для добавления кота в список питомцев.
    """
    catname = serializers.CharField(required=True, max_length=50)
    class Meta:
        model = Cat
        fields = (
            'catname',
            'id',  # На данный момент используется для ручного тестирования
        )


class CatSerializer(serializers.ModelSerializer):
    """
    Сериализатор для просмотра более подробной информации о питомце.
    Также используется для редактирования описания питомца.
    """
    cat_birthdate = serializers.DateField(required=False)
    catname = serializers.CharField(required=False)
    class Meta:
        model = Cat
        fields = (
            'catname',
            'cat_birthdate',
            'breed',
            'fur'
        )

class CatDeleteSerializer(ModelSerializer):
    """
    Сериализатор для удаления питомцев их списка.
    """
    class Meta:
        model = Cat
        fields = ('__all__')