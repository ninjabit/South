from south.modelsinspector import add_introspection_rules
from django.conf import settings
from tagging.fields import TagField

add_introspection_rules([], ["^tagging\.fields\.TagField"])
