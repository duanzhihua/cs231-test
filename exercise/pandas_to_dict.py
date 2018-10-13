# -*- coding: utf-8 -*-

import pandas as pd
df = pd.DataFrame({'col1': [1, 2],
                   'col2': [0.5, 0.75]},
                   index=['a', 'b'])

df.to_dict()

# =============================================================================
# df Out[24]: 
#   col1  col2
# a   1  0.50
# b   2  0.75 

#df.to_dict()
# Out[21]: {'col1': {'a': 1, 'b': 2}, 'col2': {'a': 0.5, 'b': 0.75}}
# =============================================================================

df['col1'].to_dict()

# =============================================================================
# df['col1'].to_dict()
# Out[23]: {'a': 1, 'b': 2}
# =============================================================================
df = df['col1'].to_dict()