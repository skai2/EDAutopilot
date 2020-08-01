from . import directinput
from ..keybinds import get_latest


def get(edkeybinds_dict=get_latest()):
    """Converts ED keybinds dict keys to directinput compatible keys"""
    direct_input_keys = {}
    convert_to_direct_keys = {
        'Key_LeftShift': 'LShift',
        'Key_RightShift': 'RShift',
        'Key_LeftAlt': 'LAlt',
        'Key_RightAlt': 'RAlt',
        'Key_LeftControl': 'LControl',
        'Key_RightControl': 'RControl'
    }

    for keybind in edkeybinds_dict:
        mod = edkeybinds_dict[keybind]['mod']
        key = edkeybinds_dict[keybind]['key']
        # Adequate key to directinput.SCANCODE dict standard
        if key in convert_to_direct_keys:
            key = convert_to_direct_keys[key]
        elif key is not None:
            key = key[4:]
        # Adequate mod to directinput.SCANCODE dict standard
        if mod in convert_to_direct_keys:
            mod = convert_to_direct_keys[mod]
        elif mod is not None:
            mod = mod[4:]
        # Prepare final binding
        binding = None
        if key is not None:
            binding = {}
            binding['pre_key'] = 'DIK_' + key.upper()
            binding['key'] = directinput.SCANCODE[binding['pre_key']]
            if mod is not None:
                binding['pre_mod'] = 'DIK_' + mod.upper()
                binding['mod'] = directinput.SCANCODE[binding['pre_mod']]
        direct_input_keys[keybind] = binding

    if len(direct_input_keys) < len(edkeybinds_dict):
        # log -> Failed to bind keys
        # handle failures
        pass
    return direct_input_keys


if __name__ == '__main__':
    print(get())
