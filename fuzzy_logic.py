import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# Define fuzzy variables
soil_moisture = ctrl.Antecedent(np.arange(0, 101, 1), 'soil_moisture')
temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')

irrigation = ctrl.Consequent(np.arange(0, 101, 1), 'irrigation')


# Membership functions
soil_moisture['dry'] = fuzz.trapmf(soil_moisture.universe, [0, 0, 20, 40])
soil_moisture['moderate'] = fuzz.trimf(soil_moisture.universe, [30, 50, 70])
soil_moisture['wet'] = fuzz.trapmf(soil_moisture.universe, [60, 80, 100, 100])

temperature['low'] = fuzz.trapmf(temperature.universe, [0, 0, 10, 20])
temperature['medium'] = fuzz.trimf(temperature.universe, [15, 25, 35])
temperature['high'] = fuzz.trapmf(temperature.universe, [30, 40, 50, 50])

humidity['low'] = fuzz.trapmf(humidity.universe, [0, 0, 20, 40])
humidity['medium'] = fuzz.trimf(humidity.universe, [30, 50, 70])
humidity['high'] = fuzz.trapmf(humidity.universe, [60, 80, 100, 100])

irrigation['low'] = fuzz.trapmf(irrigation.universe, [0, 0, 20, 40])
irrigation['medium'] = fuzz.trimf(irrigation.universe, [30, 50, 70])
irrigation['high'] = fuzz.trapmf(irrigation.universe, [60, 80, 100, 100])


# Define fuzzy rules
rules = [
    ctrl.Rule(soil_moisture['dry'] & temperature['high'], irrigation['high']),
    ctrl.Rule(soil_moisture['dry'] & temperature['medium'], irrigation['high']),
    ctrl.Rule(soil_moisture['moderate'] & temperature['high'], irrigation['medium']),
    ctrl.Rule(soil_moisture['moderate'] & humidity['low'], irrigation['medium']),
    ctrl.Rule(soil_moisture['wet'], irrigation['low']),
    ctrl.Rule(humidity['high'] & temperature['low'], irrigation['low'])
]


# Build control system
irrigation_ctrl = ctrl.ControlSystem(rules)
irrigation_sim = ctrl.ControlSystemSimulation(irrigation_ctrl)


def get_irrigation_level(soil, temp, hum):
    irrigation_sim.input['soil_moisture'] = soil
    irrigation_sim.input['temperature'] = temp
    irrigation_sim.input['humidity'] = hum

    irrigation_sim.compute()
    return irrigation_sim.output['irrigation']
