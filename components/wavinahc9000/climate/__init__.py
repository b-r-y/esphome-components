import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor, climate, number, sensor, switch
from esphome.const import CONF_ID

from .. import CONF_WAVINAHC9000_ID, Wavinahc9000

CONF_TARGET_TEMP = "target_temp_number_id"
CONF_CURRENT_TEMP = "current_temp_sensor_id"
CONF_MODE = "mode_switch_sensor_id"
CONF_ACTION = "action_sensor_id"

wavinahc9000_ns = cg.esphome_ns.namespace("wavinahc9000")
Wavinahc9000Climate = wavinahc9000_ns.class_(
    "Wavinahc9000Climate", climate.Climate, cg.Component
)

CONFIG_SCHEMA = climate.CLIMATE_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(Wavinahc9000Climate),
        cv.GenerateID(CONF_WAVINAHC9000_ID): cv.use_id(Wavinahc9000),
        cv.Required(CONF_TARGET_TEMP): cv.use_id(number.Number),
        cv.Required(CONF_CURRENT_TEMP): cv.use_id(sensor.Sensor),
        cv.Required(CONF_MODE): cv.use_id(switch.Switch),
        cv.Required(CONF_ACTION): cv.use_id(binary_sensor.BinarySensor),
    }
).extend(cv.COMPONENT_SCHEMA)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield climate.register_climate(var, config)

    number_set_temp = yield cg.get_variable(config[CONF_TARGET_TEMP])
    cg.add(var.set_temp_setpoint_number(number_set_temp))

    sens_current_temp = yield cg.get_variable(config[CONF_CURRENT_TEMP])
    cg.add(var.set_current_temp_sensor(sens_current_temp))

    switch_mode = yield cg.get_variable(config[CONF_MODE])
    cg.add(var.set_mode_switch(switch_mode))

    hvac_action = yield cg.get_variable(config[CONF_ACTION])
    cg.add(var.set_hvac_action(hvac_action))
