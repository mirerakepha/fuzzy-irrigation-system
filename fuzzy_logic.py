import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# FUZZY VARIABLES
soil_moisture = ctrl.Antecedent(np.arange(0, 101, 1), 'soil_moisture')
temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')


irrigation = ctrl.Consequent(np.arange(0, 101, 1), 'irrigation')


soil_moisture['dry'] = fuzz.trapmf(soil_moisture.universe, [0, 0, 25, 45])
soil_moisture['moderate'] = fuzz.trimf(soil_moisture.universe, [30, 50, 70])
soil_moisture['wet'] = fuzz.trapmf(soil_moisture.universe, [55, 75, 100, 100])


temperature['low'] = fuzz.trapmf(temperature.universe, [0, 0, 12, 22])
temperature['medium'] = fuzz.trimf(temperature.universe, [18, 28, 38])
temperature['high'] = fuzz.trapmf(temperature.universe, [32, 40, 50, 50])


humidity['low'] = fuzz.trapmf(humidity.universe, [0, 0, 25, 45])
humidity['medium'] = fuzz.trimf(humidity.universe, [35, 55, 75])
humidity['high'] = fuzz.trapmf(humidity.universe, [65, 85, 100, 100])


irrigation['low'] = fuzz.trapmf(irrigation.universe, [0, 0, 30, 45])
irrigation['medium'] = fuzz.trimf(irrigation.universe, [40, 55, 70])
irrigation['high'] = fuzz.trapmf(irrigation.universe, [65, 80, 100, 100])


rules = [

    # DRY soil 
    ctrl.Rule(soil_moisture['dry'] & temperature['high'], irrigation['high']),
    ctrl.Rule(soil_moisture['dry'] & temperature['medium'], irrigation['high']),
    ctrl.Rule(soil_moisture['dry'] & temperature['low'], irrigation['medium']),

    # MODERATE soil
    ctrl.Rule(soil_moisture['moderate'] & temperature['high'], irrigation['medium']),
    ctrl.Rule(soil_moisture['moderate'] & temperature['medium'], irrigation['medium']),
    ctrl.Rule(soil_moisture['moderate'] & temperature['low'], irrigation['low']),

    # WET soil 
    ctrl.Rule(soil_moisture['wet'], irrigation['low']),

    # HUMIDITY influence
    ctrl.Rule(humidity['high'] & temperature['low'], irrigation['low']),
    ctrl.Rule(humidity['low'] & temperature['high'], irrigation['high']),

    # ABSOLUTE SAFETY NET 
    ctrl.Rule(
        soil_moisture['moderate'] | temperature['medium'] | humidity['medium'],
        irrigation['medium']
    )
]


# CONTROL SYSTEM
irrigation_ctrl = ctrl.ControlSystem(rules)


# INFERENCE FUNCTION (BULLETPROOF)
def get_irrigation_level(soil, temp, hum):
    sim = ctrl.ControlSystemSimulation(irrigation_ctrl)

    sim.input['soil_moisture'] = float(soil)
    sim.input['temperature'] = float(temp)
    sim.input['humidity'] = float(hum)

    sim.compute()
    return sim.output.get('irrigation', 50.0)
