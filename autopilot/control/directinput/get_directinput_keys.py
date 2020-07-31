keys_to_obtain = [
        'YawLeftButton',
        'YawRightButton',
        'RollLeftButton',
        'RollRightButton',
        'PitchUpButton',
        'PitchDownButton',
        'SetSpeedZero',
        'SetSpeed100',
        'HyperSuperCombination',
        'UIFocus',
        'UI_Up',
        'UI_Down',
        'UI_Left',
        'UI_Right',
        'UI_Select',
        'UI_Back',
        'CycleNextPanel',
        'HeadLookReset',
        'PrimaryFire',
        'SecondaryFire'
    ]

def get_bindings(keys_to_obtain=keys_to_obtain):
    """Returns a dict with the directinput equivalent of the requested keys_to_obtain"""
    direct_input_keys = {}
    convert_to_direct_keys = {
        'Key_LeftShift': 'LShift',
        'Key_RightShift': 'RShift',
        'Key_LeftAlt': 'LAlt',
        'Key_RightAlt': 'RAlt',
        'Key_LeftControl': 'LControl',
        'Key_RightControl': 'RControl'
    }

    latest_bindings = get_latest_keybinds()
    bindings_tree = parse(latest_bindings)
    bindings_root = bindings_tree.getroot()

    for item in bindings_root:
        if item.tag in keys_to_obtain:
            key = None
            mod = None
            # Check primary
            if item[0].attrib['Device'].strip() == "Keyboard":
                key = item[0].attrib['Key']
                if len(item[0]) > 0:
                    mod = item[0][0].attrib['Key']
            # Check secondary (and prefer secondary)
            if item[1].attrib['Device'].strip() == "Keyboard":
                key = item[1].attrib['Key']
                if len(item[1]) > 0:
                    mod = item[1][0].attrib['Key']
            # Adequate key to SCANCODE dict standard
            if key in convert_to_direct_keys:
                key = convert_to_direct_keys[key]
            elif key is not None:
                key = key[4:]
            # Adequate mod to SCANCODE dict standard
            if mod in convert_to_direct_keys:
                mod = convert_to_direct_keys[mod]
            elif mod is not None:
                mod = mod[4:]
            # Prepare final binding
            binding = None
            if key is not None:
                binding = {}
                binding['pre_key'] = 'DIK_' + key.upper()
                binding['key'] = SCANCODE[binding['pre_key']]
                if mod is not None:
                    binding['pre_mod'] = 'DIK_' + mod.upper()
                    binding['mod'] = SCANCODE[binding['pre_mod']]
            if binding is not None:
                direct_input_keys[item.tag] = binding
    #             else:
    #                 logging.warning("get_bindings_<"+item.tag+">= does not have a valid keyboard keybind.")

    if len(list(direct_input_keys.keys())) < 1:
        return None
    else:
        return direct_input_keys