

def is_primitive(value):
    return isinstance(value, (str, int, float, bool))


def _custom_property_to_plain_data(value):
    if is_primitive(value):
        return value
    else:
        return value.to_dict()

_IGNORED_CUSTOM_PROPS = [
    '_RNA_UI',
    'background_color',
    'frames_per_second',
    'namedlayers',
    'cycles',
    'cycles_visibility',
]

def get_custom_properties(blender_data):
    custom_props = {
        key: value.to_list() if hasattr(value, 'to_list') else value
        for key, value in blender_data.items()
        if key not in _IGNORED_CUSTOM_PROPS
    }

    custom_props = {
        key: _custom_property_to_plain_data(value) for key, value in custom_props.items()
    }

    return custom_props

# pylint: disable=unused-argument
class BaseExporter:
    gltf_key = ''
    blender_key = ''

    @classmethod
    def get_custom_properties(cls, blender_data):
        return get_custom_properties(blender_data)

    @classmethod
    def check(cls, state, blender_data):
        return True

    @classmethod
    def default(cls, state, blender_data):
        return {
            'name': blender_data.name
        }

    @classmethod
    def export(cls, state, blender_data):
        return {}
