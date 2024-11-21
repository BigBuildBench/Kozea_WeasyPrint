"""Draw colors."""

from colorsys import hsv_to_rgb, rgb_to_hsv


def get_color(style, key):
    """Return color, taking care of possible currentColor value."""
    value = style[key]
    return value if value != 'currentColor' else style['color']


def darken(color):
    """Return a darker color."""
    hue, saturation, value = rgb_to_hsv(color.red, color.green, color.blue)
    value /= 1.5
    saturation /= 1.25
    return (*hsv_to_rgb(hue, saturation, value), color.alpha)


def lighten(color):
    """Return a lighter color."""
    hue, saturation, value = rgb_to_hsv(color.red, color.green, color.blue)
    value = 1 - (1 - value) / 1.5
    if saturation:
        saturation = 1 - (1 - saturation) / 1.25
    return (*hsv_to_rgb(hue, saturation, value), color.alpha)


def styled_color(style, color, side):
    """Return inset, outset, ridge and groove border colors."""
    if style in ('inset', 'outset'):
        do_lighten = (side in ('top', 'left')) ^ (style == 'inset')
        return (lighten if do_lighten else darken)(color)
    elif style in ('ridge', 'groove'):
        if (side in ('top', 'left')) ^ (style == 'ridge'):
            return lighten(color), darken(color)
        else:
            return darken(color), lighten(color)
    return color
