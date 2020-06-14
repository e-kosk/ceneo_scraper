from django.db import models


class OpinionModel(models.Model):

    product = models.ForeignKey(to='ProductModel', on_delete=models.CASCADE, unique=False, null=False, blank=False, verbose_name='Product')
    opinion_id = models.CharField(max_length=10, unique=True, null=False, blank=False, verbose_name='Opinion ID')
    author = models.CharField(max_length=10, unique=False, null=False, blank=False, verbose_name='Author')
    recommendation = models.NullBooleanField(default=None, null=True, blank=True, verbose_name='User recomendation')
    stars = models.FloatField(null=False, blank=False, verbose_name='Score')
    content = models.TextField(null=False, blank=False, verbose_name='Content')
    cons = models.TextField(null=True, blank=True, verbose_name='Cons')
    pros = models.TextField(null=True, blank=True, verbose_name='Pros')
    useful = models.PositiveSmallIntegerField(default=0, null=False, blank=False, verbose_name='Useful')
    useless = models.PositiveSmallIntegerField(default=0, null=False, blank=False, verbose_name='Useless')
    opinion_date = models.DateTimeField(null=False, blank=False, verbose_name='Opinion date')
    purchase_date = models.DateTimeField(null=True, blank=True, verbose_name='Purchase date')

    def __str__(self):
        return f'({self.product_id}) {self.author}: {self.content[:100]}'

    def __repr__(self):
        return f'Opinion({self.product_id} {self.opinion_id}, {self.author}, {self.author}, {self.recommendation}, {self.stars}, {self.content}, {self.cons}, {self.pros}, {self.useful}, {self.useless}, {self.opinion_date}, {self.purchase_date}'


class ProductModel(models.Model):

    product_id = models.CharField(max_length=8, unique=True, null=False, blank=False, verbose_name='Product ID')
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Name')
    rec_chart = models.CharField(max_length=128, null=True, blank=True, verbose_name='Recommendation chart')
    str_chart = models.CharField(max_length=128, null=True, blank=True, verbose_name='Stars chart')

    def __str__(self):
        return f'{self.name[:50]} [{self.product_id}]'
