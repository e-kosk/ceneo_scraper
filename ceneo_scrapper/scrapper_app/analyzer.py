from django_pandas.io import read_frame

from scrapper_app.models import OpinionModel


def analyze_product(product):

    qs = OpinionModel.objects.filter(product=product)
    df = read_frame(qs)

    result = {
        'avg_score': df['stars'].mean().round(2) if not df['stars'].empty else None,
        'max_score': df['stars'].max() if df['stars'].max() > 0 else None,
        'min_score': df['stars'].min() if df['stars'].min() > 0 else None,
        'most_frequent_score_times': df['stars'].value_counts().max() if df['stars'].value_counts().max() > 0 else None,
        'most_frequent_score_value': df['stars'].value_counts().keys()[0] if df['stars'].value_counts().max() > 0 else None,
        'opinions_amount': None or df['id'].count(),
        'purchase_confirmed': None or df['purchase_date'].count(),
    }

    return result
