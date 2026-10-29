
from flask import Flask
from strawberry.flask.views import GraphQLView
import strawberry
import base64

@strawberry.type
class UploadResult:
    filename: str
    size: int

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello GraphQL!"

@strawberry.type
class Mutation:
    @strawberry.mutation
    def file_upload(self, filename: str, content: str) -> UploadResult:
        data = base64.b64decode(content)

        with open(filename, "wb") as f:
            f.write(data)

        return UploadResult(filename=filename, size=len(data))

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema),
)

if __name__ == "__main__":
    app.run(port=5000, debug=False)

