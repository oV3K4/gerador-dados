from faker import Faker
from faker.providers import internet
fake = Faker()

nome = fake.name()
primeiro_nome_fem = fake.first_name_female()
usuario = fake.user_name()
senha = fake.password()
endereco = fake.address()
fake.add_provider(internet)

print(f"Nome: {nome}")
print(f'Nome feminino: {primeiro_nome_fem}')
print(f'Usuário: {usuario}')
print(f'Senha: {senha}')
print(f'Endereço: {endereco}')
print(fake.ipv4_private())