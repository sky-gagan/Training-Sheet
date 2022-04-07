attributes = ['engineTransmission_battery_value',
       'engineTransmission_engineoilLevelDipstick_value',
       'engineTransmission_engineOil',
       'engineTransmission_engineOil_cc_value_0',
       'engineTransmission_engine_value', 'engineTransmission_coolant_value',
       'engineTransmission_engineMounting_value',
       'engineTransmission_engineSound_value',
       'engineTransmission_engineSound_cc_value_0',
       'engineTransmission_exhaustSmoke_value',
       'engineTransmission_engineBlowByBackCompression_value',
       'engineTransmission_engineBlowByBackCompression_cc_value_0',
       'engineTransmission_clutch_value',
       'engineTransmission_gearShifting_value', 'fuel_type',
       'odometer_reading', 
       'how_old']

input_data = {}
for attr in attributes:
    val = input("Enter value of {} : ".format(attr))
    input_data[attr] = val

print(input_data)
    