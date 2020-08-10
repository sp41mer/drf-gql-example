import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import School, City, Student


class SchoolType(DjangoObjectType):

    class Meta:
        model = School


class StudentType(DjangoObjectType):

    class Meta:
        model = Student


class SchoolFilteredType(DjangoObjectType):

    class Meta:
        model = School
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )


class StudentFilteredType(DjangoObjectType):

    class Meta:
        model = Student
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )


class CityType(DjangoObjectType):

    class Meta:
        model = City


class SchoolMutation(graphene.Mutation):

    class Arguments:
        school_id = graphene.Int(required=True)
        new_name = graphene.String(required=True)

    result = graphene.Boolean()
    school = graphene.Field(SchoolType)

    def mutate(self, info, school_id, new_name):
        school = School.objects.get(id=school_id)
        school.name = new_name
        school.save()
        return {
            'result': True,
            'school': School.objects.get(id=school_id)
        }


class StudentMutation(graphene.Mutation):

    class Arguments:
        student_id = graphene.Int(required=True)
        new_name = graphene.String(required=True)

    result = graphene.Boolean()
    old_student = graphene.Field(StudentType)
    new_student = graphene.Field(StudentType)

    def mutate(self, info, student_id, new_name):
        student = Student.objects.get(id=student_id)
        old_student = Student.objects.get(id=student_id)
        student.name = new_name
        student.save()
        return {
            'result': True,
            'old_student': old_student,
            'new_student': student
        }



class Mutation:
    change_school_name = SchoolMutation.Field()
    change_student_name = StudentMutation.Field()


class Query:
    all_schools = graphene.List(SchoolType, limit=graphene.Int())
    filtered_schools = DjangoFilterConnectionField(SchoolFilteredType)
    retrieve_school = graphene.Field(SchoolType, id=graphene.Int())

    all_students = graphene.List(StudentType, limit=graphene.Int())
    retrive_student = graphene.Field(StudentType, id=graphene.Int())
    filtered_students = DjangoFilterConnectionField(StudentFilteredType)

    def resolve_all_schools(self, *args, **kwargs):
        if 'limit' in kwargs:
            return School.objects.all()[:kwargs['limit']]
        return School.objects.all()

    def resolve_all_students(self, *args, **kwargs):
        if 'limit' in kwargs:
            return Student.objects.all()[:kwargs['limit']]
        return Student.objects.all()

    def resolve_retrive_student(self, *args, **kwargs):
        if 'id' in kwargs:
            return Student.objects.get(id=kwargs['id'])

    def resolve_retrieve_school(self, info, **kwargs):
        if 'id' in kwargs:
            return School.objects.get(id=kwargs['id'])
