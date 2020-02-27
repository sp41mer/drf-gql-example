import graphene

from lecture_gql.schema import Query as LectureQuery
from lecture_gql.schema import Mutation as LectureMutation

class Query(LectureQuery, graphene.ObjectType):
    pass

class Mutation(LectureMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
