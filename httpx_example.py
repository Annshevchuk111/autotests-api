import httpx

# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
#
# # print(response.status_code)
# # print(response.json())
#
#
# data={
#     "userId": 1,
#     "title": "new task23",
#     "completed": False
# }

#response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)




data = {
    "username": "alex",
    "password": "33553"
}

response = httpx.post('https://httpbin.org/post', data=data)



headers = {"Authorization": "Bearer my_token"}
response = httpx.post('https://httpbin.org/post', headers=headers)




params ={"userId": 1}
response = httpx.get('https://jsonplaceholder.typicode.com/todos',params=params)
print(response.url)
print(response.json())

files = {"file":("example.txt", open("example.txt", "rb"))}
response = httpx.post('https://httpbin.org/post', files=files)
print(response.json())


with httpx.Client() as client:
    response1= client.get('https://jsonplaceholder.typicode.com/todos/1')
    response2= client.get('https://jsonplaceholder.typicode.com/todos/2')

# print(response1.json())
# print(response2.json())

client= httpx.Client(headers={"Authorization": "Bearer my_token"})
response = client.get('https://httpbin.org/get')
print(response.json())


try:
    response = httpx.get('https://httpbin.org/ivalid-url')
    response.raise_for_status()
except httpx.HTTPError as e:
    print(e)


try:
    response = httpx.get('https://httpbin.org/delay/5', timeout=2)
except httpx.ReadTimeout as e:
    print(e)