import torch.nn as nn
import torch

class BasicBlock(nn.module):
    def __init__(self, in_chnnel, out_chnnel, stride=1, downsample=None, **kwargs):
        super(BasicBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_chnnel=in_chnnel, out_chnnel=out_chnnel, kernel_size=3,
                            stride=stride, padding=1, bias=False)
        self.bn1 = nn.BN
