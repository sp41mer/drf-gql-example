import json

from graphene_django.utils.testing import GraphQLTestCase
from conf.schema import schema


class GQLTestCase(GraphQLTestCase):
    # Here you need to inject your test case's schema
    GRAPHQL_SCHEMA = schema

    def test_some_query(self):
        response = self.query(
            '''
            query {
              allSchools{
                id
                name
              }
            }
            ''',
            op_name='allSchools'
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_all_students_query(self):
        response = self.query(
            '''
            query {
              allStudents{
                id
                name
              }
            }
            ''',
            op_name='allStudents'
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
