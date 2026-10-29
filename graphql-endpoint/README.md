<h2>
implement a graphql endpoint. 
</h2>

requirments: 
```
> pip install flask strawberry-graphql
```

test with cmd:
```
> curl --noproxy '*' -i \
  -X POST http://127.0.0.1:5000/graphql \
  -H 'Content-Type: application/json' \
  -d '{"query":"mutation UploadFile { fileUpload(filename: \"hello.txt\", content: \"SGVsbG8gV29ybGQh\") { filename size } }","operationName":"UploadFile"}'
```
