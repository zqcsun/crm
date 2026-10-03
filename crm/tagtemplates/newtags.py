from django import template
from crm.models import Lead,Manager 

register = template.Library()

@register.simple_tag
def lead_list():
    leads = Lead.objects.all()
    return {'leads':leads}

@register.simple_tag()
def manager_list():
    managers = Manager.objects.all()
    return {'managers':managers}

@register.simple_tag
def lead_filter(manager,user):
    lead = Lead.objects.filter(manager=manager)
    return {'lead':lead}
