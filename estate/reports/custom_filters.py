from django import template

register = template.Library()

@register.filter
def get_item_by_index(lst, index):
    try:
        return lst[index]
    except (IndexError, KeyError):
        return None
