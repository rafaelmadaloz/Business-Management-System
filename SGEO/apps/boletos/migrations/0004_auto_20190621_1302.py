# Generated by Django 2.0.5 on 2019-06-21 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boletos', '0003_boleto_pedido_de_venda'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boleto',
            options={'permissions': (('view_boleto', 'Can view boleto'),), 'verbose_name': 'Boleto'},
        ),
        migrations.AlterModelOptions(
            name='configuracaoboleto',
            options={'permissions': (('view_configuracaoboleto', 'Can view configuracaoboleto'),), 'verbose_name': 'Configuração de Boleto'},
        ),
    ]
