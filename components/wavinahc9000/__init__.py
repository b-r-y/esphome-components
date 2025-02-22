import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

wavinahc9000_ns = cg.esphome_ns.namespace("wavinahc9000")
Wavinahc9000 = wavinahc9000_ns.class_("Wavinahc9000", cg.Component)

CONF_WAVINAHC9000_ID = "wavinahc9000_id"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(Wavinahc9000),
    }
)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
