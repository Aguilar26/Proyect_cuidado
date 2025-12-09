import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyect_cuidado.settings')
django.setup()

from django.contrib.auth.models import User

# Crear superusuario
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
    print("✓ Superusuario 'admin' creado exitosamente")
    print("  Username: admin")
    print("  Password: admin123")
else:
    print("✗ El usuario 'admin' ya existe")
