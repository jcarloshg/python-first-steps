
from usuario.acciones.utilities import pay_tax
import usuario
pay_tax(1238.07)


print(usuario.__name__)
print(usuario.__package__)
print(usuario.__path__)
print(usuario.__file__)
# usuario
# usuario
# ['/home/jose/Documents/school/python/python-01/07-modulos/04-reference-subpaquete/usuario']
# /home/jose/Documents/school/python/python-01/07-modulos/04-reference-subpaquete/usuario/__init__.py


print(usuario.acciones.__name__)
print(usuario.acciones.__package__)
print(usuario.acciones.__path__)
print(usuario.acciones.__file__)
# usuario.acciones
# usuario.acciones
# ['/home/jose/Documents/school/python/python-01/07-modulos/04-reference-subpaquete/usuario/acciones']
# /home/jose/Documents/school/python/python-01/07-modulos/04-reference-subpaquete/usuario/acciones/__init__.py
