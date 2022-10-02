from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError



@method_decorator(login_required, name='dispatch')
class Is_admin_mixins(object):
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_staff):
            raise ValidationError(''' you don't have permissions ''')
        return super().dispatch(request, *args, **kwargs)