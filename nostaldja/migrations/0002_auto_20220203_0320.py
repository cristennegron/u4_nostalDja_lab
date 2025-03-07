# Generated by Django 4.0.2 on 2022-02-03 03:20

from django.db import migrations

def seed(apps, schema_editor):
    Fad = apps.get_model('nostaldja', 'Fad')
    Decade = apps.get_model('nostaldja', 'Decade')
    eighties = Decade(start_year="1980s")
    nineties = Decade(start_year="1990s")
    oughts = Decade(start_year="2000s")
    tens = Decade(start_year="2010s")
    eighties.save()
    nineties.save()
    oughts.save()
    tens.save()

    Fad(decade = tens, name='Fidget Spinners', description='A fidget spinner is a toy that consists of a ball bearing in the center of a multi-lobed (typically two or three) flat structure made from metal or plastic designed to spin along its axis with little effort. Fidget spinners became popular toys in April 2017, although similar devices had been invented as early as 1993. ', image_url='https://www.dhresource.com/0x0s/f2-albu-g5-M01-79-07-rBVaJFiuqDSAF3I7AAKBk1FyKy0267.jpg/hand-spinner-fidget-spinner-tri-spinner-diy.jpg').save()
    Fad(decade = tens, name='Block Chain', description='A blockchain, originally block chain, is a continuously growing list of records, called blocks, which are linked and secured using cryptography. Each block typically contains a cryptographic hash of the previous block, a timestamp and transaction data. By design, a blockchain is inherently resistant to modification of the data.', image_url='http://sixpl.com/wp-content/uploads/2017/09/Blockchain-and-Cryptocurrency-Content-Writer.jpg').save()
    Fad(decade = oughts, name='Silly Bandz', description='Silly Bandz are rubber bands made of silicone rubber formed into shapes including animals, objects, numbers, and letters. ', image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Silly_Bandz_2009.jpg/2560px-Silly_Bandz_2009.jpg').save()
    Fad(decade = oughts, name='iPods', description='iPhone - Phone = iPod', image_url='https://commons.wikimedia.org/wiki/File:Ipod-touch-1st-gen.jpg').save()
    Fad(decade = oughts, name='Myspace', description='Myspace (stylized as MySpace) is a social networking website offering an interactive, user-submitted network of friends, personal profiles, blogs, groups, photos, music, and videos. Myspace was the largest social networking site in the world, from 2004 to 2010.', image_url='https://us.hellomagazine.com/imagenes/travel/2018012645793/tom-myspace-founder-travel-photographer/0-230-700/myspace-tom-now-t.jpg').save()
    Fad(decade = nineties, name='JNCOs', description='JNCO, short for "Judge None Choose One", is a Los Angeles, California based clothing company specializing in boys\' and men\'s jeans.', image_url='https://img.buzzfeed.com/buzzfeed-static/static/2015-06/23/15/enhanced/webdr08/enhanced-22226-1435087265-4.jpg?downsize=715:*&output-format=auto&output-quality=auto').save()

def fallow(apps, schema_editor):
    Fad = apps.get_model('nostaldja', 'Fad')
    Decade = apps.get_model('nostaldja', 'Decade')
    Decade.objects.all().delete()
    Fad.objects.all().delete()
class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]
