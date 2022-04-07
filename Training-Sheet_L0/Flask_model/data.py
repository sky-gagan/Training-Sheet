import pickle 
record = [ 1.        ,  1.        ,  0.        ,  0.        ,  0.        ,
         1.        ,  1.        ,  0.        ,  4.        ,  1.        ,
         1.        ,  1.        ,  1.        ,  1.        ,  4.        ,
         0.00517201, -0.76833361]
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
data = {}
for feature, value in zip(attributes, record):
        data[feature] = value
pickle.dump(data, open('data.pkl',"wb"))