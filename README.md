# Django + Graphene — GraphQL by example

A minimal Graphene 2 / graphene-django setup over the same School/City
models used in my other DRF lecture repos, so you can compare REST and
GraphQL side by side.

## What's inside

- `gql_hello_world.py` — GraphQL in 20 lines, no Django: schema, one
  resolver, one query executed in-process.
- `lecture_gql/schema.py` — the real thing:
  - `DjangoObjectType` for models
  - plain list query with a `limit` argument
  - `DjangoFilterConnectionField` + relay `Node` for filtered pagination
  - a mutation (`changeSchoolName`) with proper error handling

## Try it

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# open http://localhost:8000/graphql
```

Query:

```graphql
{
  allSchools(limit: 3) { id name }
  filteredSchools(name_Icontains: "sch") { edges { node { id name } } }
}
```

Mutation:

```graphql
mutation {
  changeSchoolName(schoolId: 1, newName: "Renamed") {
    result
    school { id name }
  }
}
```

Note: this uses Graphene **2.x** (2020-era). The concepts map 1:1 to
newer stacks, but if you're starting a project today look at Strawberry.
