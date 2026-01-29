import random, json
from fontTools.ttLib import TTFont

from securetext.configs import viet_char_config as vcc
from securetext.configs import app_config as ac
from securetext.services import io_service as ioService
from securetext.services import text_service as textService

# Create cmapping
def generateMapping(puaStart):
    forward = {}
    reverse = {}

    puaList = list(range(puaStart, puaStart + len(vcc.VIET_CHARS)))
    random.shuffle(puaList)

    for ch, code16 in zip(vcc.VIET_CHARS, puaList):
        forward[ch] = chr(code16)
        reverse[chr(code16)] = ch

    return forward, reverse

# Create font => font, mapping => name
def generateAndSaveFont(nameRootFont, mapping):
    font = TTFont(f"{ac.ROOT_FONT}{nameRootFont}.ttf")
    forward, reverse = mapping
    for table in font["cmap"].tables:
        if table.platformID == 3 and table.platEncID in (1, 10):
            new_cmap = table.cmap.copy()
            for src_char, dst_char in forward.items():
                src_code = ord(src_char)
                dst_code = ord(dst_char)
                if src_code in table.cmap:
                    new_cmap[dst_code] = table.cmap[src_code]
            table.cmap = new_cmap
    name = textService.randomText(10)
    fullPath = ioService.makeDir(ac.ROOT_OUT_FONT + "/" + name )
    font.save("{}/{}.{}".format(fullPath, name, "ttf"))

    with open("{}/{}.{}".format(fullPath, name, "json"), "w", encoding="utf-8") as f:
        json.dump({
            "forward": forward,
            "reverse": reverse
        }, f, ensure_ascii=False, indent=2)

    return name

# Load mapping
def loadMapping(mapPath):
    with open(mapPath, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["forward"], data["reverse"]

# encode text
def encode(text: str, fontName: str):
    forward, reverse = loadMapping("{}/{}/{}.json".format(ac.ROOT_OUT_FONT, fontName, fontName))
    return "".join(forward.get(ch, ch) for ch in text)

# get font => 
def getFont(fontName: str):
    return "{}{}/{}.ttf".format(ac.ROOT_OUT_FONT, fontName, fontName)