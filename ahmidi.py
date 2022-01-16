import string

def bankNum(_scene):
    # Return the bank of which the scene is a part of
    if 1 <= _scene <= 128:
        return 1
    elif 128 <= _scene <= 256:
        return 2
    elif 256 <= _scene <= 384:
        return 3
    elif 384 <= _scene <= 500:
        return 4
    else:
        return 0

def sceneHex(_scene):
    # Find the hex value of the current scene
    # A&H variable: SS
    if _scene % 128 != 0:
        return hex((_scene % 128) - 1)
    else:
        return hex(128)

# _ch = Midi Channel, _note = the note _vel = velocity from 1 to 127
def customString(type, ch, note, velocity):
    match type.lower():
        case "off":
            _stringType = "8"
        case "on":
            _stringType = "9"
        case "pc":
            _stringType = "A"
        case "cc":
            _stringType = "B"
        case "cp":
            _stringType = "C"

    _ch = _stringType + hex(ch-1)[2:]
    _note, _vel = hex(note)[2:], hex(velocity)[2:]
    _string = _ch + " " + _note + " " +  _vel
    return _string.upper()

print(customString("CC",16, 100, 127))