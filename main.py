# Importa los módulos necesarios.
import datetime

FORMAT = ('%H:%M:%S') # Escribe el formato del tiempo recibido.
WEIGHT = 75
HEIGHT = 175
K_1 = 0.035  # Coeficiente para contar calorías.
K_2 = 0.029  # Coefficient for counting calories
STEP_M = 0.65  # Longitud de un paso en metros.
storage_data = {}  # Diccionario para almacenar los datos recibidos.
def check_correct_data(data):
    """Comprobar si el paquete recibido es correcto."""
    if len(data) != 2:
        return False
    if not data[0]:
        return False
    if not data[1]:
        return False
    return True
def check_correct_time(time):
    """Comprobar si el parámetro tiempo es correcto."""
    if storage_data:
        last_time = max(storage_data.keys())
        if time <= last_time:
            return False
    return True
def get_step_day(steps):
    """Obtén el número de pasos dados durante el día actual."""
    return sum(storage_data.values()) + steps
def get_distance(steps):
    """Obtén la distancia recorrida en km."""
    distance = steps * STEP_M / 1000
    return distance
def get_calories_burned(dist, current_time):
    """Obtén las calorías quemadas."""
    hours = current_time.hour + current_time.minute/60
    MEANSPEED = dist / hours
    calBurned = (K_1 * WEIGHT + (MEANSPEED ** 2 / HEIGHT) * K_2 * WEIGHT) * hours * 60
    return calBurned
def get_achievement(dist):
    """Obtén el mensaje de felicitaciones para la distancia recorrida."""
    if dist >= 6.5:
        return '¡Qué buen entrenamiento! Objetivo cumplido.'
    elif dist >= 3.9:
        return '¡No está mal! Hoy ha sido un día productivo.'
    elif dist >= 2:
        return 'Menos de lo que querías, ¡pero vamos a intentar mejorar mañana!'
    else:
        return 'Está bien tomarse un día libre. No siempre se puede ganar.'
def show_message(time, steps, dist, calories_burned, achievement):
    """Mostrar mensaje en la terminal con los valores proporcionados."""
    print(
        f"Tiempo: {time}.\n"
        f"Pasos dados hoy: {steps}.\n"
        f"La distancia fue {dist:.2f} km.\n"
        f"Has quemado {calories_burned:.2f} cal.\n"
        f"{achievement}\n"
    )
def accept_package(data):
    """Procesar paquete de datos."""
    if not check_correct_data(data):
        print('Paquete inválido')
        return storage_data

    # Desempaqueta los datos recibidos.
    pack_time =  datetime.datetime.strptime(data[0], FORMAT).time()

    if not check_correct_time(pack_time):
        print('Valor de tiempo inválido')
        return storage_data

    day_steps = get_step_day(data[1])
    dist = get_distance(day_steps)
    calories_burned = get_calories_burned(dist, pack_time)
    achievement = get_achievement(dist)

    storage_data[pack_time] = data[1]

    show_message(data[0], day_steps, dist, calories_burned, achievement)

    return storage_data

# Self-test data. Do not delete it.
if __name__ == "__main__":
    package_0 = ('2:00:01', 505)
    package_1 = (None, 3211)
    package_2 = ('9:36:02', 15000)
    package_3 = ('9:36:02', 9000)
    package_4 = ('8:01:02', 7600)
    package_5 = ('10:01:02', 100)
    package_6 = ('10:01:02', 100)
    accept_package(package_0)
    accept_package(package_1)
    accept_package(package_2)
    accept_package(package_3)
    accept_package(package_4)
    accept_package(package_5)
    accept_package(package_6)

