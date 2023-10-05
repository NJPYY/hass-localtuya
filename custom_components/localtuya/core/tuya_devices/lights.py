"""
    This a file contains available tuya data
    https://developer.tuya.com/en/docs/iot/standarddescription?id=K9i5ql6waswzq
    Credits: official HA Tuya integration.
    Modified by: xZetsubou
"""

from .base import DPCode, LocalTuyaEntity, EntityCategory, update_dict


# copied from const.py for now..
CONF_BRIGHTNESS_LOWER = "brightness_lower"
CONF_BRIGHTNESS_UPPER = "brightness_upper"
CONF_COLOR_TEMP_MIN_KELVIN = "color_temp_min_kelvin"
CONF_COLOR_TEMP_MAX_KELVIN = "color_temp_max_kelvin"
CONF_COLOR_TEMP_REVERSE = "color_temp_reverse"
CONF_MUSIC_MODE = "music_mode"

DEFAULTS_VALUES = {
    CONF_BRIGHTNESS_LOWER: 29,
    CONF_BRIGHTNESS_UPPER: 1000,
    CONF_COLOR_TEMP_MIN_KELVIN: 2700,
    CONF_COLOR_TEMP_MAX_KELVIN: 6500,
    CONF_COLOR_TEMP_REVERSE: False,
    CONF_MUSIC_MODE: False,
}

LIGHTS: dict[LocalTuyaEntity] = {
    # Curtain Switch
    # https://developer.tuya.com/en/docs/iot/category-clkg?id=Kaiuz0gitil39
    "clkg": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_BACKLIGHT,
            name="backlight",
            entity_category=EntityCategory.CONFIG,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # String Lights
    # https://developer.tuya.com/en/docs/iot/dc?id=Kaof7taxmvadu
    "dc": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=DPCode.BRIGHT_VALUE,
            color_temp=DPCode.TEMP_VALUE,
            color=DPCode.COLOUR_DATA,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Strip Lights
    # https://developer.tuya.com/en/docs/iot/dd?id=Kaof804aibg2l
    "dd": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=DPCode.BRIGHT_VALUE,
            color_temp=DPCode.TEMP_VALUE,
            color=DPCode.COLOUR_DATA,
            custom_configs=DEFAULTS_VALUES
            # default_color_type=DEFAULT_COLOR_TYPE_DATA_V2,
        ),
    ),
    # Light
    # https://developer.tuya.com/en/docs/iot/categorydj?id=Kaiuyzy3eheyy
    "dj": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=(DPCode.BRIGHT_VALUE_V2, DPCode.BRIGHT_VALUE),
            color_temp=(DPCode.TEMP_VALUE_V2, DPCode.TEMP_VALUE),
            color=(DPCode.COLOUR_DATA_V2, DPCode.COLOUR_DATA),
            scene=(DPCode.SCENE_DATA, DPCode.SCENE_DATA_V2),
            custom_configs=update_dict(DEFAULTS_VALUES, {CONF_MUSIC_MODE: True}),
        ),
        # Not documented
        # Based on multiple reports: manufacturer customized Dimmer 2 switches
        LocalTuyaEntity(
            id=DPCode.SWITCH_1,
            name="light",
            brightness=DPCode.BRIGHT_VALUE_1,
        ),
    ),
    # Ceiling Fan Light
    # https://developer.tuya.com/en/docs/iot/fsd?id=Kaof8eiei4c2v
    "fsd": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=DPCode.BRIGHT_VALUE,
            color_temp=DPCode.TEMP_VALUE,
            color=DPCode.COLOUR_DATA,
            scene=(DPCode.SCENE_DATA, DPCode.SCENE_DATA_V2),
            custom_configs=DEFAULTS_VALUES,
        ),
        # Some ceiling fan lights use LIGHT for DPCode instead of SWITCH_LED
        LocalTuyaEntity(
            id=DPCode.LIGHT,
            name=None,
        ),
    ),
    # Ambient Light
    # https://developer.tuya.com/en/docs/iot/ambient-light?id=Kaiuz06amhe6g
    "fwd": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=DPCode.BRIGHT_VALUE,
            color_temp=DPCode.TEMP_VALUE,
            color=DPCode.COLOUR_DATA,
            scene=(DPCode.SCENE_DATA, DPCode.SCENE_DATA_V2),
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Motion Sensor Light
    # https://developer.tuya.com/en/docs/iot/gyd?id=Kaof8a8hycfmy
    "gyd": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=DPCode.BRIGHT_VALUE,
            color_temp=DPCode.TEMP_VALUE,
            color=DPCode.COLOUR_DATA,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Humidifier Light
    # https://developer.tuya.com/en/docs/iot/categoryjsq?id=Kaiuz1smr440b
    "jsq": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=DPCode.BRIGHT_VALUE,
            color=DPCode.COLOUR_DATA_HSV,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Switch
    # https://developer.tuya.com/en/docs/iot/s?id=K9gf7o5prgf7s
    "kg": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_BACKLIGHT,
            name="backlight",
            entity_category=EntityCategory.CONFIG,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Air Purifier
    # https://developer.tuya.com/en/docs/iot/f?id=K9gf46h2s6dzm
    "kj": (
        LocalTuyaEntity(
            id=DPCode.LIGHT,
            name="backlight",
            entity_category=EntityCategory.CONFIG,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Air conditioner
    # https://developer.tuya.com/en/docs/iot/categorykt?id=Kaiuz0z71ov2n
    "kt": (
        LocalTuyaEntity(
            id=DPCode.LIGHT,
            name="backlight",
            entity_category=EntityCategory.CONFIG,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Unknown light product
    # Found as VECINO RGBW as provided by diagnostics
    # Not documented
    "mbd": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=DPCode.BRIGHT_VALUE,
            color=DPCode.COLOUR_DATA,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Unknown product with light capabilities
    # Fond in some diffusers, plugs and PIR flood lights
    # Not documented
    "qjdcz": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=DPCode.BRIGHT_VALUE,
            color=DPCode.COLOUR_DATA,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Heater
    # https://developer.tuya.com/en/docs/iot/categoryqn?id=Kaiuz18kih0sm
    "qn": (
        LocalTuyaEntity(
            id=DPCode.LIGHT,
            name="backlight",
            entity_category=EntityCategory.CONFIG,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Smart Camera
    # https://developer.tuya.com/en/docs/iot/categorysp?id=Kaiuz35leyo12
    "sp": (
        LocalTuyaEntity(
            id=DPCode.FLOODLIGHT_SWITCH,
            brightness=DPCode.FLOODLIGHT_LIGHTNESS,
            name="Floodlight",
            custom_configs=DEFAULTS_VALUES,
        ),
        LocalTuyaEntity(
            id=DPCode.BASIC_INDICATOR,
            name="Indicator light",
            entity_category=EntityCategory.CONFIG,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Dimmer Switch
    # https://developer.tuya.com/en/docs/iot/categorytgkg?id=Kaiuz0ktx7m0o
    "tgkg": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED_1,
            name="light",
            brightness=DPCode.BRIGHT_VALUE_1,
            brightness_upper=DPCode.BRIGHTNESS_MAX_1,
            brightness_lower=DPCode.BRIGHTNESS_MIN_1,
            custom_configs=DEFAULTS_VALUES,
        ),
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED_2,
            name="light_2",
            brightness=DPCode.BRIGHT_VALUE_2,
            brightness_upper=DPCode.BRIGHTNESS_MAX_2,
            brightness_lower=DPCode.BRIGHTNESS_MIN_2,
            custom_configs=DEFAULTS_VALUES,
        ),
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED_3,
            name="light_3",
            brightness=DPCode.BRIGHT_VALUE_3,
            brightness_upper=DPCode.BRIGHTNESS_MAX_3,
            brightness_lower=DPCode.BRIGHTNESS_MIN_3,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Dimmer
    # https://developer.tuya.com/en/docs/iot/tgq?id=Kaof8ke9il4k4
    "tgq": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name="light",
            brightness=(DPCode.BRIGHT_VALUE_V2, DPCode.BRIGHT_VALUE),
            brightness_upper=DPCode.BRIGHTNESS_MAX_1,
            brightness_lower=DPCode.BRIGHTNESS_MIN_1,
            custom_configs=DEFAULTS_VALUES,
        ),
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED_1,
            name="light",
            brightness=DPCode.BRIGHT_VALUE_1,
            custom_configs=DEFAULTS_VALUES,
        ),
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED_2,
            name="light_2",
            brightness=DPCode.BRIGHT_VALUE_2,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Wake Up Light II
    # Not documented
    "hxd": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name="light",
            brightness=(DPCode.BRIGHT_VALUE_V2, DPCode.BRIGHT_VALUE),
            brightness_upper=DPCode.BRIGHTNESS_MAX_1,
            brightness_lower=DPCode.BRIGHTNESS_MIN_1,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Solar Light
    # https://developer.tuya.com/en/docs/iot/tynd?id=Kaof8j02e1t98
    "tyndj": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=DPCode.BRIGHT_VALUE,
            color_temp=DPCode.TEMP_VALUE,
            color=DPCode.COLOUR_DATA,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Ceiling Light
    # https://developer.tuya.com/en/docs/iot/ceiling-light?id=Kaiuz03xxfc4r
    "xdd": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=DPCode.BRIGHT_VALUE,
            color_temp=DPCode.TEMP_VALUE,
            color=DPCode.COLOUR_DATA,
            custom_configs=DEFAULTS_VALUES,
        ),
        LocalTuyaEntity(
            id=DPCode.SWITCH_NIGHT_LIGHT,
            name="night_light",
        ),
    ),
    # Remote Control
    # https://developer.tuya.com/en/docs/iot/ykq?id=Kaof8ljn81aov
    "ykq": (
        LocalTuyaEntity(
            id=DPCode.SWITCH_CONTROLLER,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=DPCode.BRIGHT_CONTROLLER,
            color_temp=DPCode.TEMP_CONTROLLER,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
    # Fan
    # https://developer.tuya.com/en/docs/iot/categoryfs?id=Kaiuz1xweel1c
    "fs": (
        LocalTuyaEntity(
            id=DPCode.LIGHT,
            name=None,
            color_mode=DPCode.WORK_MODE,
            brightness=DPCode.BRIGHT_VALUE,
            color_temp=DPCode.TEMP_VALUE,
            custom_configs=DEFAULTS_VALUES,
        ),
        LocalTuyaEntity(
            id=DPCode.SWITCH_LED,
            name="light_2",
            brightness=DPCode.BRIGHT_VALUE_1,
            custom_configs=DEFAULTS_VALUES,
        ),
    ),
}

# Socket (duplicate of `kg`)
# https://developer.tuya.com/en/docs/iot/s?id=K9gf7o5prgf7s
LIGHTS["cz"] = LIGHTS["kg"]

# Power Socket (duplicate of `kg`)
# https://developer.tuya.com/en/docs/iot/s?id=K9gf7o5prgf7s
LIGHTS["pc"] = LIGHTS["kg"]
