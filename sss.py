import scipy

import numpy
from scipy.io import savemat
from scipy import io


a = numpy.zeros((10,3))
mdic = []
request = ['a', 'b' ,'c']

for i in range(len(request)):
    mdic.append({request[i]: a[:,i]})
print(mdic[0])
print(mdic[1])

drv_save = {}
data = a
drv_save["data"] = data
# for n in range(3):
#     data = a
#     drv_save["IC_%d"%(n+1)] = data
savemat("test_mat.mat",drv_save)


mat_file = io.loadmat('test_mat.mat')
kk =mat_file['data']

print(kk)



# savemat("test_mat.mat", mdic[0])

# tmp = {}
# for varname in midc.names:
#     tmp[varname] = mdic[varname]


# savemat("test_mat.mat", tmp)