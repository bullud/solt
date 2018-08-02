import os
import sys
import numpy as np
from nose import with_setup

sys.path.insert(0,'..')
from fastaug import core as ftgc

_globals = {'img': None, 'mask':None}

def img_mask_2x2_generator():
    img = np.array([[1, 1], [1, 1]]).reshape((2,2)).astype(np.uint8)
    mask = np.array([[1, 0], [0, 1]]).reshape((2,2)).astype(np.uint8)

    for key in _globals:
        _globals[key] = None
    _globals['img'] = img
    _globals['mask'] = mask

def img_2x2_generator():
    img = np.array([[1, 1], [1, 1]]).reshape((2,2))

    for key in _globals:
        _globals[key] = None
    _globals['img'] = img

@with_setup(img_2x2_generator)
def test_data_item_create_img():
    img = _globals['img']
    dc = ftgc.DataContainer((img,), 'I')
    assert True

@with_setup(img_2x2_generator)
def test_pipeline_empty():
    img = _globals['img']
    dc = ftgc.DataContainer((img,), 'I')
    pipeline = ftgc.Pipeline()
    res, _ = pipeline(dc)[0]
    assert np.all(res == img)