from __future__ import annotations

ANSI_COLOR_TO_RGB: dict[str, tuple[int, int, int]] = {
    "black": (0, 0, 0),
    "red": (128, 0, 0),
    "green": (0, 128, 0),
    "yellow": (128, 128, 0),
    "blue": (0, 0, 128),
    "magenta": (128, 0, 128),
    "cyan": (0, 128, 128),
    "white": (192, 192, 192),
    "bright_black": (128, 128, 128),
    "bright_red": (255, 0, 0),
    "bright_green": (0, 255, 0),
    "bright_yellow": (255, 255, 0),
    "bright_blue": (0, 0, 255),
    "bright_magenta": (255, 0, 255),
    "bright_cyan": (0, 255, 255),
    "bright_white": (255, 255, 255),
    "grey0": (0, 0, 0),
    "gray0": (0, 0, 0),
    "navy_blue": (0, 0, 95),
    "dark_blue": (0, 0, 135),
    "blue3": (0, 0, 215),
    "blue1": (0, 0, 255),
    "dark_green": (0, 95, 0),
    "deep_sky_blue4": (0, 95, 175),
    "dodger_blue3": (0, 95, 215),
    "dodger_blue2": (0, 95, 255),
    "green4": (0, 135, 0),
    "spring_green4": (0, 135, 95),
    "turquoise4": (0, 135, 135),
    "deep_sky_blue3": (0, 135, 215),
    "dodger_blue1": (0, 135, 255),
    "green3": (0, 215, 0),
    "spring_green3": (0, 215, 95),
    "dark_cyan": (0, 175, 135),
    "light_sea_green": (0, 175, 175),
    "deep_sky_blue2": (0, 175, 215),
    "deep_sky_blue1": (0, 175, 255),
    "spring_green2": (0, 255, 95),
    "cyan3": (0, 215, 175),
    "dark_turquoise": (0, 215, 215),
    "turquoise2": (0, 215, 255),
    "green1": (0, 255, 0),
    "spring_green1": (0, 255, 135),
    "medium_spring_green": (0, 255, 175),
    "cyan2": (0, 255, 215),
    "cyan1": (0, 255, 255),
    "dark_red": (135, 0, 0),
    "deep_pink4": (175, 0, 95),
    "purple4": (95, 0, 175),
    "purple3": (95, 0, 215),
    "blue_violet": (95, 0, 255),
    "orange4": (135, 95, 0),
    "grey37": (95, 95, 95),
    "gray37": (95, 95, 95),
    "medium_purple4": (95, 95, 135),
    "slate_blue3": (95, 95, 215),
    "royal_blue1": (95, 95, 255),
    "chartreuse4": (95, 135, 0),
    "dark_sea_green4": (95, 175, 95),
    "pale_turquoise4": (95, 135, 135),
    "steel_blue": (95, 135, 175),
    "steel_blue3": (95, 135, 215),
    "cornflower_blue": (95, 135, 255),
    "chartreuse3": (95, 215, 0),
    "cadet_blue": (95, 175, 175),
    "sky_blue3": (95, 175, 215),
    "steel_blue1": (95, 215, 255),
    "pale_green3": (135, 215, 135),
    "sea_green3": (95, 215, 135),
    "aquamarine3": (95, 215, 175),
    "medium_turquoise": (95, 215, 215),
    "chartreuse2": (135, 215, 0),
    "sea_green2": (95, 255, 95),
    "sea_green1": (95, 255, 175),
    "aquamarine1": (135, 255, 215),
    "dark_slate_gray2": (95, 255, 255),
    "dark_magenta": (135, 0, 175),
    "dark_violet": (175, 0, 215),
    "purple": (175, 0, 255),
    "light_pink4": (135, 95, 95),
    "plum4": (135, 95, 135),
    "medium_purple3": (135, 95, 215),
    "slate_blue1": (135, 95, 255),
    "yellow4": (135, 175, 0),
    "wheat4": (135, 135, 95),
    "grey53": (135, 135, 135),
    "gray53": (135, 135, 135),
    "light_slate_grey": (135, 135, 175),
    "light_slate_gray": (135, 135, 175),
    "medium_purple": (135, 135, 215),
    "light_slate_blue": (135, 135, 255),
    "dark_olive_green3": (175, 215, 95),
    "dark_sea_green": (135, 175, 135),
    "light_sky_blue3": (135, 175, 215),
    "sky_blue2": (135, 175, 255),
    "dark_sea_green3": (175, 215, 135),
    "dark_slate_gray3": (135, 215, 215),
    "sky_blue1": (135, 215, 255),
    "chartreuse1": (135, 255, 0),
    "light_green": (135, 255, 135),
    "pale_green1": (175, 255, 135),
    "dark_slate_gray1": (135, 255, 255),
    "red3": (215, 0, 0),
    "medium_violet_red": (175, 0, 135),
    "magenta3": (215, 0, 215),
    "dark_orange3": (215, 95, 0),
    "indian_red": (215, 95, 95),
    "hot_pink3": (215, 95, 135),
    "medium_orchid3": (175, 95, 175),
    "medium_orchid": (175, 95, 215),
    "medium_purple2": (175, 135, 215),
    "dark_goldenrod": (175, 135, 0),
    "light_salmon3": (215, 135, 95),
    "rosy_brown": (175, 135, 135),
    "grey63": (175, 135, 175),
    "gray63": (175, 135, 175),
    "medium_purple1": (175, 135, 255),
    "gold3": (215, 175, 0),
    "dark_khaki": (175, 175, 95),
    "navajo_white3": (175, 175, 135),
    "grey69": (175, 175, 175),
    "gray69": (175, 175, 175),
    "light_steel_blue3": (175, 175, 215),
    "light_steel_blue": (175, 175, 255),
    "yellow3": (215, 215, 0),
    "dark_sea_green2": (175, 255, 175),
    "light_cyan3": (175, 215, 215),
    "light_sky_blue1": (175, 215, 255),
    "green_yellow": (175, 255, 0),
    "dark_olive_green2": (175, 255, 95),
    "dark_sea_green1": (215, 255, 175),
    "pale_turquoise1": (175, 255, 255),
    "deep_pink3": (215, 0, 135),
    "magenta2": (255, 0, 215),
    "hot_pink2": (215, 95, 175),
    "orchid": (215, 95, 215),
    "medium_orchid1": (255, 95, 255),
    "orange3": (215, 135, 0),
    "light_pink3": (215, 135, 135),
    "pink3": (215, 135, 175),
    "plum3": (215, 135, 215),
    "violet": (215, 135, 255),
    "light_goldenrod3": (215, 175, 95),
    "tan": (215, 175, 135),
    "misty_rose3": (215, 175, 175),
    "thistle3": (215, 175, 215),
    "plum2": (215, 175, 255),
    "khaki3": (215, 215, 95),
    "light_goldenrod2": (255, 215, 135),
    "light_yellow3": (215, 215, 175),
    "grey84": (215, 215, 215),
    "gray84": (215, 215, 215),
    "light_steel_blue1": (215, 215, 255),
    "yellow2": (215, 255, 0),
    "dark_olive_green1": (215, 255, 135),
    "honeydew2": (215, 255, 215),
    "light_cyan1": (215, 255, 255),
    "red1": (255, 0, 0),
    "deep_pink2": (255, 0, 95),
    "deep_pink1": (255, 0, 175),
    "magenta1": (255, 0, 255),
    "orange_red1": (255, 95, 0),
    "indian_red1": (255, 95, 135),
    "hot_pink": (255, 95, 215),
    "dark_orange": (255, 135, 0),
    "salmon1": (255, 135, 95),
    "light_coral": (255, 135, 135),
    "pale_violet_red1": (255, 135, 175),
    "orchid2": (255, 135, 215),
    "orchid1": (255, 135, 255),
    "orange1": (255, 175, 0),
    "sandy_brown": (255, 175, 95),
    "light_salmon1": (255, 175, 135),
    "light_pink1": (255, 175, 175),
    "pink1": (255, 175, 215),
    "plum1": (255, 175, 255),
    "gold1": (255, 215, 0),
    "navajo_white1": (255, 215, 175),
    "misty_rose1": (255, 215, 215),
    "thistle1": (255, 215, 255),
    "yellow1": (255, 255, 0),
    "light_goldenrod1": (255, 255, 95),
    "khaki1": (255, 255, 135),
    "wheat1": (255, 255, 175),
    "cornsilk1": (255, 255, 215),
    "grey100": (255, 255, 255),
    "gray100": (255, 255, 255),
    "grey3": (8, 8, 8),
    "gray3": (8, 8, 8),
    "grey7": (18, 18, 18),
    "gray7": (18, 18, 18),
    "grey11": (28, 28, 28),
    "gray11": (28, 28, 28),
    "grey15": (38, 38, 38),
    "gray15": (38, 38, 38),
    "grey19": (48, 48, 48),
    "gray19": (48, 48, 48),
    "grey23": (58, 58, 58),
    "gray23": (58, 58, 58),
    "grey27": (68, 68, 68),
    "gray27": (68, 68, 68),
    "grey30": (78, 78, 78),
    "gray30": (78, 78, 78),
    "grey35": (88, 88, 88),
    "gray35": (88, 88, 88),
    "grey39": (98, 98, 98),
    "gray39": (98, 98, 98),
    "grey42": (108, 108, 108),
    "gray42": (108, 108, 108),
    "grey46": (118, 118, 118),
    "gray46": (118, 118, 118),
    "grey50": (128, 128, 128),
    "gray50": (128, 128, 128),
    "grey54": (138, 138, 138),
    "gray54": (138, 138, 138),
    "grey58": (148, 148, 148),
    "gray58": (148, 148, 148),
    "grey62": (158, 158, 158),
    "gray62": (158, 158, 158),
    "grey66": (168, 168, 168),
    "gray66": (168, 168, 168),
    "grey70": (178, 178, 178),
    "gray70": (178, 178, 178),
    "grey74": (188, 188, 188),
    "gray74": (188, 188, 188),
    "grey78": (198, 198, 198),
    "gray78": (198, 198, 198),
    "grey82": (208, 208, 208),
    "gray82": (208, 208, 208),
    "grey85": (218, 218, 218),
    "gray85": (218, 218, 218),
    "grey89": (228, 228, 228),
    "gray89": (228, 228, 228),
    "grey93": (238, 238, 238),
    "gray93": (238, 238, 238),
}