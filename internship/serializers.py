from rest_framework import serializers
<<<<<<< HEAD
from internship.models import Gig,Skill, ProLang, Internship


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = ['company','title','description','category']
=======
from internship.models import Skill, ProLang, Internship
from company.models import Company


class InternshipSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField('get_company_name')
    skills = serializers.SerializerMethodField('get_skills')
    programming_languages = serializers.SerializerMethodField('get_pro_lang')
    internship_id = serializers.SerializerMethodField('get_internship_id')
    
    def get_company_name(slef, internship_object):
        intern_company =  Company.objects.get(id=internship_object.company.id)
        return intern_company.name
    
    def get_skills(slef, internship_object):
        internship_skills =  Skill.objects.filter(Internship=internship_object.id)
        skills = "" 
        for Obj in internship_skills:
            skills += Obj.skill + ", "
        return skills[:-2]
    
    def get_pro_lang(slef, internship_object):
        internship_prog_langs =  ProLang.objects.filter(Internship=internship_object.id)
        prog_langs = "" 
        for Obj in internship_prog_langs:
            prog_langs += Obj.ProLang + ", "
        return prog_langs[:-2]
    
    def get_internship_id(slef, internship_object):
        return internship_object.id

    class Meta:
        model = Internship
        fields = ['company','title','description','category','open_date','closing_date','company_name','skills','programming_languages','internship_id']

>>>>>>> internship

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill','Internship']

class ProLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProLang
        fields = ['ProLang','Internship']

<<<<<<< HEAD
class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = ['Internship','open_date','closing_date']
=======
>>>>>>> internship
