from rest_framework import serializers
from internship.models import Skill, ProLang, Internship


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = ['company','title','description','category']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill','Internship']

class ProLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProLang
        fields = ['ProLang','Internship']
