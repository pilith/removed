# Models
from .models import component
from .models import fixed_board

import django_filters as df

class componentFilter(df.FilterSet):
    class Meta:
        model = component

