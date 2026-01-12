import json
import random
import os
from fontTools.ttLib import TTFont

# =========================
# CONFIG
# =========================
INPUT_FONT = r"D:/Chuan/TestFontSwap/py/fonts/Noto_Sans,Roboto/Noto_Sans/NotoSans-VariableFont_wdth,wght.ttf"

OUTPUT_DIR = r"D:/Chuan/TestFontSwap/py/outputs/NotoSans"
OUTPUT_FONT = os.path.join(OUTPUT_DIR, "NotoSans-Variable.ttf")
MAPPING_FILE = os.path.join(OUTPUT_DIR, "cmap_mapping.json")

# Unicode Private Use Area
PUA_START = 0xE000

# =========================
# Vietnamese charset
# =========================
VIET_CHARS = list(set("""
aáàạảãăắằặẳẵâấầậẩẫ
bcdđeéèẹẻẽêếềệểễ
fghijklmnopqrstuvwxyýỳỵỷỹz
AÁÀẠẢÃĂẮẰẶẲẴÂẤẦẬẨẪ
BCDĐEÉÈẸẺẼÊẾỀỆỂỄ
FGHIJKLMNOPQRSTUVWXYZ
""".replace("\n", "")))

# =========================
# Create random cmap
# =========================
def create_random_cmap(chars):
    pua_codes = list(range(PUA_START, PUA_START + len(chars)))
    random.shuffle(pua_codes)

    forward = {}
    reverse = {}

    for ch, code in zip(chars, pua_codes):
        forward[ch] = chr(code)
        reverse[chr(code)] = ch

    return forward, reverse

# =========================
# Patch font cmap
# =========================
def patch_font_cmap(font_path, cmap_forward, output_path):
    font = TTFont(font_path)

    for table in font["cmap"].tables:
        if table.platformID == 3 and table.platEncID in (1, 10):
            new_cmap = table.cmap.copy()
            for src_char, dst_char in cmap_forward.items():
                src_code = ord(src_char)
                dst_code = ord(dst_char)
                if src_code in table.cmap:
                    new_cmap[dst_code] = table.cmap[src_code]
            table.cmap = new_cmap

    font.save(output_path)

# =========================
# MAIN
# =========================
if __name__ == "__main__":

    # ✅ TẠO THƯ MỤC OUTPUT NẾU CHƯA CÓ
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    forward, reverse = create_random_cmap(VIET_CHARS)

    patch_font_cmap(INPUT_FONT, forward, OUTPUT_FONT)

    with open(MAPPING_FILE, "w", encoding="utf-8") as f:
        json.dump(
            {
                "encode": forward,
                "decode": reverse
            },
            f,
            ensure_ascii=False,
            indent=2
        )

    print("✅ Done")
    print(f"Font obfuscated: {OUTPUT_FONT}")
    print(f"Mapping saved: {MAPPING_FILE}")
