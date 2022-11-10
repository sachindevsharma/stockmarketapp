

paper_bg_color = '#1a1c23'
plot_bg_color  = '#30333d'
plot_bg_color2 = '#22252b'
header_color   = 'silver'
text_color     = '#ededed'
green_color    = '#45df7e'
red_color      = '#da5657'


def _bg_color(mode):
    mode_dict = {
        "dark": '#30333d',
        "light": '#22252b'
    }
    return mode_dict[mode.lower()]
    
def _text_color(mode):
    text_dict = {
        "dark": '#ededed',
        "light": 'black'
    }
    return text_dict[mode.lower()]


class Config:
    
    mode = "dark"
    bg_color = _bg_color(mode)
    text_color = _text_color(mode)
    
    
