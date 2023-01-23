from rest_framework import serializers
from internship.models import Skill, ProLang, Internship
from company.models import Company


class InternshipSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField('get_company_name')
    skills = serializers.SerializerMethodField('get_skills')
    programming_languages = serializers.SerializerMethodField('get_pro_lang')
    
    def get_company_name(slef, internship_object):
        intern_company =  Company.objects.get(id=internship_object.id)
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

    class Meta:
        model = Internship
        fields = ['company','title','description','category','open_date','closing_date','company_name','skills','programming_languages']

