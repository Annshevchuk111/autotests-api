
from faker import Faker


class Fake:
    def __init__(self, faker:Faker):
        self.faker = faker

    def text(self):
        return self.faker.text()

    def uuid4(self):
        return self.faker.uuid4()

    def email(self):
        return self.faker.email()

    def sentence(self):
        return self.faker.sentence()

    def password(self):
        return self.faker.password()

    def first_name(self):
        return self.faker.first_name()
    def last_name(self):
        return self.faker.last_name()

    def middle_name(self):
        return self.faker.first_name()

    def estimated_time(self):
        return f'{self.interger(1,10)} weeks'

    def interger(self, start:int=1,end:int=100) ->int:
        return self.faker.random_int(start, end)

    def min_score(self):
        return self.faker.random_int(1, 30)
    def max_score(self):
        return self.faker.random_int(31, 100)

fake = Fake(faker=Faker())