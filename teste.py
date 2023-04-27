from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

# Obtém a data atual
now = timezone.now()

# Obtém a data de início (domingo) e fim (sábado) da semana atual
start_date = now - timedelta(days=now.weekday())
end_date = start_date + timedelta(days=6)


print(start_date)
print(end_date)