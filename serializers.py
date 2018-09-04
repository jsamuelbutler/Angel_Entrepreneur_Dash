from django.db.models import Q
from django.utils.timezone import now
from rest_framework import serializers

from .models import Accelerator, Cohort


class SimpleAcceleratorSerializer(serializers.ModelSerializer):
    logo = serializers.CharField(max_length=500, read_only=True)

    class Meta:
        model = Accelerator
        fields = ('id', 'name', 'logo')


class SimpleCohortSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(required=False, allow_null=True)
    end_date = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = Cohort
        fields = ('id', 'name', 'start_date', 'end_date', 'accelerator')


class CohortSerializer(SimpleCohortSerializer):
    current_week = serializers.ReadOnlyField()

    @staticmethod
    def validate_start_date(value):
        if not value:
            return value
        if now().date() > value:
            raise serializers.ValidationError('Start date can\'t be less the current date.')
        return value

    @staticmethod
    def validate_end_date(value):
        if not value:
            return value
        if now().date() > value:
            raise serializers.ValidationError('End date can\'t be less the current date.')
        return value

    def validate(self, validated_data):
        start_date = validated_data.get('start_date')
        end_date = validated_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError('Start date can\'t be more then end date.')

        name = validated_data.get('name', self.instance.name if self.instance else None)
        accelerator = validated_data.get('accelerator', self.instance.name if self.instance else None)

        if Cohort.objects.filter(name=name, accelerator=accelerator).exclude(
                    Q(id=self.instance.id) if self.instance else Q()
                ).exists():
            raise serializers.ValidationError('Already there is a fund with such name.')
        return validated_data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()

        return instance

    class Meta:
        model = Cohort
        fields = '__all__'
        read_only_fields = ('watchers',)


class AcceleratorSerializer(serializers.ModelSerializer):
    cohorts = SimpleCohortSerializer(many=True, read_only=True)
    logo = serializers.CharField(max_length=100, allow_blank=True)
    name = serializers.CharField(max_length=50, allow_blank=False)

    class Meta:
        model = Accelerator
        fields = '__all__'
