import numpy as np
import timeit 

def main():
    data = np.array([[1.5,-0.2,3],[0,-3,6.5]])
    print(data)
    print(data.shape)

    print(data * 10 )
    print(data * data)
    print(data.sum())
    #print(data)

    print("*" *40)
    print(np.zeros((2,3)))
    print(np.zeros(10))
    print(np.empty((2,3)))
    print("*" *40)

    print(np.arange(0,10))
    print(np.arange(0,10,2,dtype=int32))
    print(np.arange(0,10,0.5,dtype=float))
    print(range(0,10))
    print(list(range(0,10)))

def main2():
     data = np.array([[1.5,-0.2,3],[0,-3,6.5]])
     print(data.dtype)

     float_arr = data.astype(np.int32)
     print(float_arr.dtype)

     str_arr = data.astype(np.strings)
     print(str_arr.dtype)
     print(str_arr)

def main3():
    my_arr = np.arange(1_000_000)
    my_list = list(range(1_000_000))
    
    t = timeit.timeit('my_arr * 2',number=10000,globals = locals())
    print(f"10000 次执行总耗时：{t} 秒")
    print(f'平均每次耗时：{t/10000} 秒')
    print("*"* 40)
    t2 = timeit.timeit('my_list * 2',number=10000,globals = locals())
    print(f"10000 次执行总耗时：{t2} 秒")
    print(f'平均每次耗时：{t2/10000} 秒')
 

def main4():
    '''索引和切片'''
    arr = np.arange(10)
    print(arr)
    print(arr[5])
    print(arr[5:])

    print("*"*40)
    arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(arr2d)
    print(arr2d[2])
    print("*"*40)

    arr3d = np.array([[[1,2,3],[4,5,6]],
                      [[7,8,9],[10,11,12]]
                     ])
    #print(arr3d)
    #print(arr3d[0])
    #print(arr3d[1][1][0])
    old_vlue = arr3d[0].copy()
    #print(old_vlue)
    arr3d[0] = 42

    #print(arr3d)
    print(arr3d[0])
    print(old_vlue)

    print("*"*40)
    # 切片
    lower_dim_slice = arr2d[:2]
   # print(lower_dim_slice)
   # print(arr2d[:2,1:])
    #print(arr2d[1,:2])
    print(arr2d[1:2,:2])
    
def main5():
    arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(arr2d.shape)
    print(arr2d[1:3,:2])


def main6():
    names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
    data = np.random.randn(7,2)
    print(names)
    print(data)
    #print(data.shape)
    #print(names == 'Bob')
    #data[names == 'Bob']
    #print(data[names == 'Bob'])

    print("*"*40)
    # ~ 符号用来翻转布尔类型数组
    cond = ~(names == 'Bob')
    print(data[cond])

    print("*"*40)
    mask = (names == 'Bob') | (names == 'Will')
    print(data[mask])
    print(data[~mask])

def main7():
    """花式索引1"""
    arr = np.zeros((8,4))
    for i in range(8):
        arr[i] = i
    print(arr[[4,3,0,6]])

def main8():
    """花式索引2"""
    arr = np.arange(32).reshape(8,4)
    print(arr)
    
    print(arr[[1,5,7,2],[0,3,1,2]])

def main9():
    # 随机数
    #np.random.seed(0)
    #print(np.random.rand(5,2))
    #print(np.random.standard_normal((5,2)))
    #print(np.random.randint(10,size=(3,5)))
    
    #-----point = np.arange(-5,5,0.01)
    # x,y = np.meshgrid(point,point)
    #print(point.shape)
    
    rng = np.random.default_rng(seed=12345)
    data = rng.standard_normal((2,3))
    print(data)

def main10():

    arr = np.arange(10)
    print(arr)
    arr2 = np.sqrt(arr)
    print(arr2)
    print("**"*20)
    rng = np.random.default_rng(seed=12345)
    x = rng.standard_normal(6)
    y = rng.standard_normal(6)

    z = np.max([x,y],axis=1)
    
    print(x)
    print(y)
    print(z)


def main11():
    rng = np.random.default_rng(seed=12345)
    x = rng.standard_normal(6)*5 
    print(x)
    remainder,whole_part = np.modf(x)
    print(remainder)
    print(whole_part)
    

def main12():
    rng = np.random.default_rng(seed=12345)
    arr = rng.standard_normal((5,4))
    print(arr.max())
    print(arr.min())
    print(arr.sum())
    print(arr.mean())

    print("**"*20)
    arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(arr2)
    print(arr2.cumsum())
    print(arr2.cumprod())

def main13():
    '''线性代数'''
    x = np.array([[1,2,3],[4,5,6],[7,8,9]])
    y = np.array([[7,8],[9,10],[11,12]])
    z = np.ones(3)

    #print(x.dot(y))
    #print(np.dot(x,y))
    
   # print(x @ y)
    print(x.shape)
    print(z.shape)
    print(z)
    print(x @ z.T)
    print(x @ z)
    print(x  @ x.T)
    print(x.T @ x)
    print("**"*20)
    print(np.linalg.inv(x))
    


if __name__ == '__main__':

    main13()