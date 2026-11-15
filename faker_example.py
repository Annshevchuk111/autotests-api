from faker import Faker

fake = Faker()

print(fake.email())

data ={
    "email": fake.email(),
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "age": fake.random_int(1, 100)
}

print(data)