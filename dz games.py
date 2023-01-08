class Dog:
    group = 'dog'

    def __init__(self, name, breed, age):
        self.name = 'Dog'
        self.breed = 'bulldog'
        self.age = '5 years'
        print('Обьект создан')


dog1 = Dog(name='dog', breed='bulldog', age='5 years')

print(dog1.name)
print(dog1.breed)
print(dog1.age)
