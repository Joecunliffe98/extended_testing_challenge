from faker import Faker

fake = Faker('en_GB')

def create_person(add_to_allowlist):
    name = fake.name()
    surname = (name.split(" ")[-1])
    address = fake.address()
    file = open('03_resources/target_directory/originals/' + surname, 'a')
    file.write(name + "\n" + address)
    if add_to_allowlist == True:
        file = open('03_resources/target_directory/allowlist', 'a')
        file.write(surname + "\n")


for i in range(1):
    create_person(True)
