import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import School, City


class SchoolType(DjangoObjectType):

    class Meta:
        model = School


class SchoolFilteredType(DjangoObjectType):

    class Meta:
        model = School
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
        # TODO
        return {
            'result': True,
            'school': School.objects.first()
        }


class Mutation:
    change_school_name = SchoolMutation.Field()


class Query:
    all_schools = graphene.List(SchoolType, limit=graphene.Int())
    filtered_schools = DjangoFilterConnectionField(SchoolFilteredType)
    retrieve_school = graphene.Field(SchoolType, id=graphene.Int())

    def resolve_all_schools(self, *args, **kwargs):
        if 'limit' in kwargs:
            return School.objects.all()[:kwargs['limit']]
        return School.objects.all()

    def resolve_retrieve_school(self, info, **kwargs):
        if 'id' in kwargs:
            return School.objects.get(id=kwargs['id'])
