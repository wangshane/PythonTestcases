import numpy as np
import torch
from torch.nn.parameter import Parameter
from torch.nn.modules.module import Module


class GraphConvolution(Module):
    def __init__(self, in_features, out_features, bias=True):
        super(GraphConvolution, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        # Shape: (in_features, out_features)
        self.weight = Parameter(torch.FloatTensor(in_features, out_features))
        if bias:
            self.bias = Parameter(torch.FloatTensor(out_features))
        else:
            self.register_parameter('bias', None)
        self.reset_parameters()


    def reset_parameters(self):
        stdv = 1. / np.sqrt(self.weight.size(1))
        # uniform_(from, to): sampling
        self.weight.data.uniform_(-stdv, stdv)
        if self.bias is not None:
            self.bias.data.uniform_(-stdv, stdv)


    def forward(self, input, adj):
        sup = torch.mm(input, self.weight)
        output = torch.spmm(adj.float(), sup)
        if self.bias is not None:
            return output + self.bias
        else:
            return output


    def __repr__(self):
        return self.__class__.__name__ + ' (' \
                + str(self.in_features) + ' -> ' \
                + str(self.out_features) + ')'