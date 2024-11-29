from django.db import models
import online_shop.models as om


class UsersReview(om.BaseModel):
    product = models.ForeignKey(om.Product, on_delete=models.CASCADE, verbose_name='Product')
    rate = models.IntegerField(default=0, verbose_name='Rate', validators=[om.validate_rate])
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = 'UserReview'
        verbose_name_plural = 'UserReviews'

    def __str__(self):
        return f'{self.rate}'
