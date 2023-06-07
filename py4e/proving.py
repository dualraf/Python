import numpy as np
import pandas as pd
import re
a = np.arange(8)
b = a[4:6]
b[:] = 40
c = a[4] + a[6]
s = 'ACAABAACAAABACDBADDDFSDDDFFSSSASDAFAAACBAAAFASD'
pattern ='[^A](?=AAA)'
S = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print(S.iloc(0))