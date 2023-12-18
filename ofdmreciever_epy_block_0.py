"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self,vectorSize=16):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Maximum Hold',   # will show up in GRC
            in_sig=[(np.float32,vectorSize)],
            out_sig=[np.float32]
        )
        self.maximum=0;
        self.maximum1=0;
        self.papr=0;
        self.papr1=0;

        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).


    def work(self, input_items, output_items):
        """example: multiply with constant"""
        self.maximum1 = np.max(input_items[0])
        if(self.maximum<self.maximum1):
            self.maximum = self.maximum1
        self.papr=self.maximum1/np.average(input_items[0])
        if(self.papr1<self.papr):
            self.papr1=self.papr
        output_items[0][:] = self.papr1
        return len(output_items[0])
