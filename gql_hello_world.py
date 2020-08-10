import graphene


class Query(graphene.ObjectType):

    hello = graphene.String()
    world = graphene.String()

    def resolve_hello(self, info):
        return 'World'

    def resolve_world(self, *args, **kwargs):
        return 'Hello'


schema = graphene.Schema(query=Query)

request = schema.execute('''
  query {
    world
  }
''')


print(request.data)
