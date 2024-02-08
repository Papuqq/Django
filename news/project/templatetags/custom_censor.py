from django import template

register = template.Library()

unwanted_words = ['редиска']


@register.filter()
def censor(value, re=None):
    for word in unwanted_words:
        value = re.sub(r'\b%s\b' % word, '*' * len(word), value, flags=re.IGNORECASE)
    return value
