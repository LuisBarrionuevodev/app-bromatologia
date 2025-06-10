import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.inspector_logica import (
    crear_inspector,
    # obtener_inspector,
    # actualizar_inspector,
    # eliminar_inspector
)

# Datos de prueba
afiliado_test = 12345
nombre_test = "Juan"
apellido_test = "Pérez"
turno_test = 1  # Mañana

# Crear
crear_inspector(afiliado_test, nombre_test, apellido_test, turno_test)

# Obtener
# inspector = obtener_inspector(afiliado_test)

# # Actualizar
# actualizar_inspector(afiliado_test, "Juan Manuel", "Pérez", 2)  # Turno tarde

# # Obtener actualizado
# obtener_inspector(afiliado_test)

# # Eliminar
# eliminar_inspector(afiliado_test)

# # Intentar obtener eliminado
# obtener_inspector(afiliado_test)
