# Descripción
# Se presenta una funcin que veriica la temperatura de la CPU. Si la temperatura alcanza niveles crticos, se lanza una
# excepcin personalizada. Tambin hay mensajes de advertencia para temperaturas elevadas pero no crticas. Debes
# lanzar distintos mensajes de advertencia cuando la temperatura se encuentra sobre 75 y 90 grados celsius, pero
# debes lanzar un error si la temperatura es mayor a 100 grados celsius

class OverheatingError(Exception):
    def __init__(self, temperature):
        self.__temperature = temperature

    def __str__(self):
        if self.__temperature >= 75 and self.__temperature <= 90:
            return f"Advertencia: La temperatura de la CPU es muy alta. {self.__temperature}"

        if self.__temperature >= 91 and self.__temperature <= 99:
            return f"Super advertencia: No debes seguir trabajando {self.__temperature}"

        if self.__temperature >= 100:
            return f"🔴🔴🔴 POWER OFF THE EQUIPMENT 🔴🔴🔴"


def check_cpu_temperature(temperature):

    if temperature >= 75 and temperature <= 90:
        raise OverheatingError(temperature)

    if temperature >= 91 and temperature <= 99:
        raise OverheatingError(temperature)

    if temperature >= 100:
        raise OverheatingError(temperature)


try:
    temperatura_actual = 95  # Cambia este valor para probar diferentes escenarios
    check_cpu_temperature(temperatura_actual)
except OverheatingError as e:
    print(e)


# OUTPUT
# Advertencia: La temperatura de la CPU es muy alta. 76
# Super advertencia: No debes seguir trabajando 95
# 🔴🔴🔴 POWER OFF THE EQUIPMENT 🔴🔴🔴
