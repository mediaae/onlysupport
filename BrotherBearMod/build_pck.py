#!/usr/bin/env python3
"""
熊二Mod - 生成美术素材并打包为 Godot .pck
BrotherBearMod - Generate art assets and pack into Godot .pck
"""
import struct
import hashlib
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("请安装 Pillow: pip install Pillow")
    sys.exit(1)

# ========== 配置 ==========
MOD_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(MOD_DIR, "assets")
OUTPUT_PCK = os.path.join(MOD_DIR, "BrotherBearMod.pck")

# 颜色定义
BROWN = (139, 105, 20)       # 棕色 (熊皮色)
GOLD = (255, 215, 0)         # 金色 (蜂蜜色)
DARK_BROWN = (74, 40, 0)     # 深褐
LIGHT_BROWN = (180, 140, 60) # 浅棕
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HONEY_YELLOW = (255, 193, 37)
GREEN = (34, 139, 34)
RED = (200, 50, 50)

def get_font(size):
    """尝试加载中文字体"""
    font_paths = [
        "C:/Windows/Fonts/msyh.ttc",    # 微软雅黑
        "C:/Windows/Fonts/simhei.ttf",   # 黑体
        "C:/Windows/Fonts/simsun.ttc",   # 宋体
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except:
                pass
    return ImageFont.load_default()

def create_character_portrait():
    """创建角色立绘 (512x512)"""
    img = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 熊身 (大椭圆)
    draw.ellipse([100, 80, 412, 480], fill=BROWN, outline=DARK_BROWN, width=4)
    # 头部
    draw.ellipse([150, 30, 362, 230], fill=BROWN, outline=DARK_BROWN, width=4)
    # 耳朵
    draw.ellipse([140, 20, 200, 80], fill=BROWN, outline=DARK_BROWN, width=3)
    draw.ellipse([312, 20, 372, 80], fill=BROWN, outline=DARK_BROWN, width=3)
    draw.ellipse([155, 35, 185, 65], fill=LIGHT_BROWN)
    draw.ellipse([327, 35, 357, 65], fill=LIGHT_BROWN)
    # 眼睛
    draw.ellipse([200, 100, 230, 130], fill=WHITE)
    draw.ellipse([282, 100, 312, 130], fill=WHITE)
    draw.ellipse([208, 108, 222, 122], fill=BLACK)
    draw.ellipse([290, 108, 304, 122], fill=BLACK)
    # 鼻子
    draw.ellipse([240, 135, 272, 160], fill=DARK_BROWN)
    # 嘴巴 (微笑)
    draw.arc([220, 150, 292, 195], 0, 180, fill=DARK_BROWN, width=3)
    # 蜂蜜罐 (右手边)
    draw.rectangle([350, 250, 420, 380], fill=HONEY_YELLOW, outline=DARK_BROWN, width=2)
    draw.text((360, 290), "蜜", fill=DARK_BROWN, font=get_font(28), anchor="mm")
    # 手臂
    draw.ellipse([340, 200, 430, 300], fill=BROWN, outline=DARK_BROWN, width=3)
    draw.ellipse([80, 200, 170, 300], fill=BROWN, outline=DARK_BROWN, width=3)
    # 腿
    draw.ellipse([140, 400, 220, 500], fill=BROWN, outline=DARK_BROWN, width=3)
    draw.ellipse([292, 400, 372, 500], fill=BROWN, outline=DARK_BROWN, width=3)
    # 肚皮
    draw.ellipse([180, 200, 332, 380], fill=LIGHT_BROWN, outline=BROWN, width=2)
    # 文字
    draw.text((256, 460), "熊二", fill=WHITE, font=get_font(32), anchor="mm")
    return img

def create_character_icon():
    """创建角色小图标 (128x128)"""
    img = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # 简化的熊头
    draw.ellipse([10, 15, 118, 115], fill=BROWN, outline=DARK_BROWN, width=3)
    draw.ellipse([5, 5, 40, 40], fill=BROWN, outline=DARK_BROWN, width=2)  # 左耳
    draw.ellipse([88, 5, 123, 40], fill=BROWN, outline=DARK_BROWN, width=2)  # 右耳
    draw.ellipse([12, 10, 33, 30], fill=LIGHT_BROWN)
    draw.ellipse([95, 10, 116, 30], fill=LIGHT_BROWN)
    draw.ellipse([35, 45, 55, 65], fill=WHITE)  # 左眼
    draw.ellipse([73, 45, 93, 65], fill=WHITE)  # 右眼
    draw.ellipse([42, 52, 50, 60], fill=BLACK)
    draw.ellipse([80, 52, 88, 60], fill=BLACK)
    draw.ellipse([53, 65, 75, 80], fill=DARK_BROWN)  # 鼻子
    draw.arc([45, 78, 83, 100], 0, 180, fill=DARK_BROWN, width=2)
    return img

def create_energy_counter():
    """创建能量图标 (64x64)"""
    img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # 蜂蜜滴形状
    draw.ellipse([8, 20, 56, 60], fill=HONEY_YELLOW, outline=DARK_BROWN, width=2)
    draw.polygon([(32, 4), (12, 28), (52, 28)], fill=HONEY_YELLOW, outline=DARK_BROWN)
    draw.text((32, 40), "3", fill=DARK_BROWN, font=get_font(22), anchor="mm")
    return img

def create_card_back():
    """创建卡背 (250x360)"""
    img = Image.new("RGBA", (250, 360), DARK_BROWN)
    draw = ImageDraw.Draw(img)
    # 边框
    draw.rectangle([5, 5, 244, 354], outline=GOLD, width=3)
    draw.rectangle([10, 10, 239, 349], outline=LIGHT_BROWN, width=2)
    # 中央熊头图案
    draw.ellipse([80, 100, 170, 190], fill=BROWN, outline=GOLD, width=2)
    draw.ellipse([75, 85, 105, 115], fill=BROWN, outline=GOLD, width=1)
    draw.ellipse([145, 85, 175, 115], fill=BROWN, outline=GOLD, width=1)
    draw.ellipse([100, 130, 115, 145], fill=WHITE)
    draw.ellipse([135, 130, 150, 145], fill=WHITE)
    draw.ellipse([115, 150, 135, 162], fill=GOLD)
    # 文字
    draw.text((125, 260), "熊二", fill=GOLD, font=get_font(36), anchor="mm")
    draw.text((125, 300), "BrotherBear", fill=LIGHT_BROWN, font=get_font(16), anchor="mm")
    return img

def create_card_portrait(name, color, text, size=(200, 160)):
    """创建卡牌插图"""
    img = Image.new("RGBA", size, color)
    draw = ImageDraw.Draw(img)
    draw.rectangle([2, 2, size[0]-3, size[1]-3], outline=GOLD, width=2)
    draw.text((size[0]//2, size[1]//2), text, fill=WHITE, font=get_font(24), anchor="mm")
    return img

def create_relic_icon(name, color, symbol, size=(96, 96)):
    """创建遗物图标"""
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # 圆形底座
    draw.ellipse([4, 4, size[0]-4, size[1]-4], fill=color, outline=GOLD, width=2)
    draw.text((size[0]//2, size[1]//2), symbol, fill=WHITE, font=get_font(28), anchor="mm")
    return img

def create_potion_icon(name, color, size=(64, 64)):
    """创建药水图标"""
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # 瓶子形状
    draw.rectangle([20, 8, 44, 20], fill=(150, 150, 150), outline=BLACK, width=1)  # 瓶口
    draw.polygon([(16, 20), (48, 20), (52, 56), (12, 56)], fill=color, outline=BLACK, width=2)
    draw.ellipse([14, 50, 50, 62], fill=color, outline=BLACK, width=1)
    # 液面光泽
    draw.ellipse([24, 28, 38, 40], fill=(255, 255, 255, 80))
    return img

def generate_all_assets():
    """生成所有美术素材"""
    os.makedirs(ASSETS_DIR, exist_ok=True)
    assets = {}

    # 角色素材
    char_img = create_character_portrait()
    assets["images/characters/brotherbear_portrait.png"] = char_img

    icon_img = create_character_icon()
    assets["images/icons/brotherbear_icon.png"] = icon_img
    assets["images/icons/brotherbear_icon_outline.png"] = icon_img

    energy_img = create_energy_counter()
    assets["images/energy/brotherbear_energy.png"] = energy_img

    # 卡背
    card_back = create_card_back()
    assets["images/cards/brotherbear_card_back.png"] = card_back

    # 卡牌插图 (按类别)
    card_arts = {
        "strike": (RED, "打击"),
        "defend": (GREEN, "防御"),
        "claw": (BROWN, "熊爪"),
        "honey_collect": (HONEY_YELLOW, "蜂蜜"),
        "bear_claw": (DARK_BROWN, "熊掌"),
        "forest": (GREEN, "森林"),
        "honey_smash": (GOLD, "碎击"),
        "wild_swipe": (BROWN, "横扫"),
        "tree_trunk": (GREEN, "树干"),
        "bark_armor": (LIGHT_BROWN, "树皮"),
        "honey_shield": (HONEY_YELLOW, "蜜盾"),
        "thicket": (GREEN, "树丛"),
        "healing": (GREEN, "治愈"),
        "roar": (RED, "怒吼"),
        "berserk": (RED, "狂暴"),
        "honey_blast": (GOLD, "爆裂"),
        "entangle": (GREEN, "缠绕"),
        "tonic": (HONEY_YELLOW, "补药"),
        "forest_song": (GREEN, "之歌"),
        "fury": (RED, "之怒"),
        "bear_skin": (BROWN, "熊皮"),
        "honey_armor": (HONEY_YELLOW, "蜜甲"),
        "mega_claw": (DARK_BROWN, "巨爪"),
        "forest_wrath": (RED, "天罚"),
        "honey_feast": (GOLD, "盛宴"),
        "golden_honey": (GOLD, "金蜜"),
        "bear_king": (GOLD, "熊王"),
        "honey_rain": (HONEY_YELLOW, "蜜雨"),
        "awakening": (GOLD, "觉醒"),
        "gift": (HONEY_YELLOW, "馈赠"),
        "pact": (GREEN, "盟约"),
        "rally": (RED, "鼓舞"),
        "guardian": (BROWN, "守护"),
        "double": (GOLD, "双倍"),
        "shared": (GOLD, "共享"),
    }

    for name, (color, text) in card_arts.items():
        assets[f"images/cards/portraits/bb_{name}.png"] = create_card_portrait(name, color, text)

    # 遗物图标
    relic_arts = {
        "golden_hive": (GOLD, "蜂"),
        "bear_claw_amulet": (BROWN, "爪"),
        "bee_companion": (HONEY_YELLOW, "蜂"),
        "forest_totem": (GREEN, "图"),
        "honey_jar": (HONEY_YELLOW, "罐"),
        "bear_fang": (DARK_BROWN, "牙"),
        "pine_sap_ring": (LIGHT_BROWN, "环"),
        "crown_of_bears": (GOLD, "冠"),
    }

    for name, (color, symbol) in relic_arts.items():
        assets[f"images/relics/bb_{name}.png"] = create_relic_icon(name, color, symbol)

    # 药水图标
    potion_arts = {
        "honey_potion": HONEY_YELLOW,
        "bear_paw_potion": BROWN,
        "forest_potion": GREEN,
        "polluted_potion": (100, 60, 60),
    }

    for name, color in potion_arts.items():
        assets[f"images/potions/bb_{name}.png"] = create_potion_icon(name, color)

    # 保存所有素材到本地
    for path, img in assets.items():
        full_path = os.path.join(ASSETS_DIR, path.replace("/", os.sep))
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        img.save(full_path, "PNG")

    print(f"生成了 {len(assets)} 个美术素材")
    return assets

def create_godot_pck(assets, output_path):
    """
    创建 Godot 4.x 格式的 .pck 文件
    格式参考: Godot 4.x core/io/file_access_pack.h
    """
    # 准备文件数据
    files = []
    for res_path, img in assets.items():
        # 转为 res:// 路径
        godot_path = f"res://{res_path}"
        # 保存为 PNG bytes
        import io
        buf = io.BytesIO()
        img.save(buf, "PNG")
        png_data = buf.getvalue()
        files.append((godot_path, png_data))

    # 计算文件表大小
    HEADER_SIZE = 0x70  # Godot 4.x header is 0x70 bytes + 8 bytes file count = 0x78

    # 计算文件表大小 (entry: 4+path_len+padding+8+8+16 = path_len aligned to 4 + 36)
    file_table_size = 8  # file count (uint64)
    for godot_path, _ in files:
        path_bytes = godot_path.encode("utf-8")
        path_len = len(path_bytes)
        padded_len = path_len + (4 - path_len % 4) % 4
        file_table_size += 4 + padded_len + 8 + 8 + 16  # path_len + path + offset + size + md5

    # 填充 file_table_size 到 16 字节对齐
    file_table_size = (file_table_size + 15) & ~15

    # 数据偏移 = header(0x70) + file_count(8) + file_table
    data_offset = HEADER_SIZE + 8 + file_table_size

    # 计算每个文件的数据偏移
    current_offset = data_offset
    file_entries = []
    for godot_path, png_data in files:
        md5 = hashlib.md5(png_data).digest()
        file_entries.append((godot_path, current_offset, len(png_data), md5))
        current_offset += len(png_data)

    total_data_size = current_offset - data_offset

    # 写入 .pck
    with open(output_path, "wb") as f:
        # === Header (0x70 = 112 bytes, then file count) ===
        f.write(b"GDPC")                        # Magic (0x00)
        f.write(struct.pack("<I", 3))            # Pack format version (0x04)
        f.write(struct.pack("<I", 4))            # Version (0x08)
        f.write(struct.pack("<I", 5))            # Engine major (0x0C)
        f.write(struct.pack("<I", 1))            # Engine minor (0x10)
        f.write(struct.pack("<I", 2))            # Engine patch (0x14)
        f.write(struct.pack("<Q", 0x70))         # Header size = 0x70 (0x18)
        f.write(struct.pack("<Q", file_table_size))  # File table size (0x20)

        # Reserved padding to reach 0x70 (112)
        # Already written: 6*4 + 2*8 = 40 bytes. Need 112 - 40 = 72 bytes of zeros
        f.write(b"\x00" * 72)

        # === File Table ===
        for godot_path, offset, size, md5 in file_entries:
            path_bytes = godot_path.encode("utf-8")
            path_len = len(path_bytes)
            f.write(struct.pack("<I", path_len))
            f.write(path_bytes)
            # Pad to 4-byte alignment
            padding = (4 - path_len % 4) % 4
            f.write(b"\x00" * padding)
            f.write(struct.pack("<Q", offset))
            f.write(struct.pack("<Q", size))
            f.write(md5)

        # Pad file table to 16-byte alignment
        current_pos = f.tell()
        table_end = HEADER_SIZE + file_table_size
        if current_pos < table_end:
            f.write(b"\x00" * (table_end - current_pos))

        # === File Data ===
        for godot_path, png_data in files:
            f.write(png_data)

    final_size = os.path.getsize(output_path)
    print(f"打包完成: {output_path} ({final_size:,} bytes, {len(files)} files)")

if __name__ == "__main__":
    print("=" * 50)
    print("  熊二Mod - 美术素材生成器 & PCK打包工具")
    print("=" * 50)
    print()

    print("[1/2] 生成美术素材...")
    assets = generate_all_assets()

    print("[2/2] 打包 .pck 文件...")
    create_godot_pck(assets, OUTPUT_PCK)

    print()
    print("完成！素材已保存到 assets/ 目录")
    print(f"PCK 文件: {OUTPUT_PCK}")
