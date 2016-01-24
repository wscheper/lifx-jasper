import re
import lifx

# Jasper Interface
WORDS = ["ON", "OFF", "ENABLE", "DISABLE", "TOGGLE", "SWITCH", "LIGHTS", "LIGHT", "DIM", "BREATHE"]

# Execute this module when it involves something with "light"
def isValid(text):
    return bool(re.search(r'\b(light|lights)\b', text, re.IGNORECASE))

# Determine the appropriate action to take
def handle(text, mic, profile):
    if isOn(text):
        lifx().toggleIntelligent()
        mic.say("Turning lights on")
    elif isToggle(text):
        lifx().toggleIntelligent()
        mic.say("Toggling lights")
    elif isOff(text):
        lifx().power(false)
        mic.say("Turning lights off")
    elif isNightLights(text):
        lifx().nightLights()
        mic.say("Turning night mode on")
    elif isBreatheLights(text):
        lifx().breatheLights()
        mic.say("Breathing lights")
    else:
        mic.say("That command is unknown")

# eof Jasper interface

# Helpers to determine what action to perform

def isOn(text):
    return bool(re.search(r'\b(on|enable)\b', text, re.IGNORECASE))

def isToggle(text):
    return bool(re.search(r'\b(switch|toggle)\b', text, re.IGNORECASE))

def isOff(text):
    return bool(re.search(r'\b(off|of|disable)\b', text, re.IGNORECASE))

def isNightLights(text):
    return bool(re.search(r'\b(dim|night)\b', text, re.IGNORECASE))

def isBreatheLights(text):
    return bool(re.search(r'\b(breathe)\b', text, re.IGNORECASE))
