
# Módulos vs Paquetes
#    - Módulo apunta a archivos
#    - Paquetes a carpetas

# You must create the file __init__.py
# to indicate to compiler that the folder
# is going to be a Package

# import usuario.acciones
# usuario.acciones.pay_tax()

# from usuario import acciones
# acciones.pay_tax(87.345)

from usuario.acciones import pay_tax
pay_tax(1238.07)
