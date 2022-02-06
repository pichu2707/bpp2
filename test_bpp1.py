import pytest
import bpp1


def test_gasto():
    lst = [946, 630, 506, 462, 321, 290, 271, 268, 207, 147, 126, 117]
    assert bpp1.gasto(lst) == 117
    
def test_ahorro():
    lst2 = [-960, -848, -456, -384, -380, -378, -303, -296, -271, -221, -116, -11]
    assert bpp1.ahorro(lst2) == -11

def test_media():
    media = 357.5833333333333
    assert bpp1.mediames(media) == 357.5833333333333