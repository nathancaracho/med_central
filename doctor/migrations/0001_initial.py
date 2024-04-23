# Generated by Django 5.0.4 on 2024-04-22 01:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expedition_org', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PR', 'Paraná'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OfficeAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PR', 'Paraná'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2)),
                ('street', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddd', models.CharField(choices=[('11', 'São Paulo'), ('12', 'Vale do Paraíba Paulista'), ('13', 'Santos'), ('14', 'Bauru'), ('15', 'Sorocaba'), ('16', 'Barretos'), ('17', 'Ribeirão Preto'), ('18', 'Presidente Prudente'), ('19', 'Campinas'), ('21', 'Rio de Janeiro'), ('22', 'Niterói'), ('24', 'Volta Redonda'), ('27', 'Vitoria'), ('28', 'Linhares'), ('31', 'Belo Horizonte'), ('32', 'Juiz de Fora'), ('33', 'Governador Valadares'), ('34', 'Uberlândia'), ('35', 'Poços de Caldas'), ('37', 'Varginha'), ('38', 'Montes Claros'), ('41', 'Curitiba'), ('42', 'Londrina'), ('43', 'Maringá'), ('44', 'Ponta Grossa'), ('45', 'Toledo'), ('47', 'Joaçaba'), ('48', 'Florianópolis'), ('49', 'Criciúma'), ('51', 'Porto Alegre'), ('53', 'Caxias do Sul'), ('54', 'Pelotas'), ('55', 'Santa Maria'), ('61', 'Brasília'), ('62', 'Goiânia'), ('63', 'Jataí'), ('64', 'Catalão'), ('67', 'Corumbá'), ('68', 'Rio Branco'), ('71', 'Salvador'), ('73', 'Juazeiro'), ('74', 'Itabuna'), ('75', 'Jequié'), ('77', 'Barreiras'), ('79', 'Sena Madureira'), ('81', 'Recife'), ('82', 'Maceió'), ('83', 'João Pessoa'), ('84', 'Natal'), ('85', 'Campina Grande'), ('87', 'Caruaru'), ('88', 'Sobral'), ('89', 'Fortaleza'), ('91', 'Manaus'), ('92', 'Porto Velho'), ('93', 'Santarém'), ('94', 'Altamira'), ('97', 'Manaus'), ('98', 'São Luís'), ('99', 'Maranhão')], max_length=2)),
                ('numbers', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('crm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.crm')),
                ('officeAddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.officeaddress')),
                ('PhoneNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.phonenumber')),
            ],
        ),
    ]