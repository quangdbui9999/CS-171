gas_const = 8.3144621


''' Your solution goes here '''
def compute_gas_volume(pressure, temp, moles):
    return (moles * gas_const * temp / pressure)

gas_pressure = float(input())
gas_moles = float(input())
gas_temperature = float(input())
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')