def bankNum(_scene):
    # Return the bank of which the scene is a part of
    if _scene >= 1 and _scene <= 128:
        return 1
    elif _scene >= 128 and _scene <= 256:
        return 2
    elif _scene >= 256 and _scene <= 384:
        return 3
    elif _scene >= 384 and _scene <= 500:
        return 4
    else:
        return 0

def sceneHex(_scene):
    # Find the hex value of the current scene
    if _scene % 128 != 0:
        return hex((_scene % 128) - 1)
    else:
        return hex(128)

scene = input("Enter your scene: ")
print(sceneHex(int(scene)))