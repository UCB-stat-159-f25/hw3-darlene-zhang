import numpy as np
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ligotools import readligo

def test_channel_to_seglist():
    dq_data = np.array([0, 1, 1, 1, 1, 0, 0, 1, 1, 1])
    pieces = readligo.dq_channel_to_seglist(dq_data, fs=1)
    
    assert len(pieces) == 2

def test_segment_list():
    my_segments = [(100, 200), (300, 400)]
    seglist = readligo.SegmentList(my_segments)
    
    assert len(seglist.seglist) == 2