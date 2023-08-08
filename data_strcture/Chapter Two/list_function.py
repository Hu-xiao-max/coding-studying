'''
Python标准类型list就是一种元素个数可变的线性表，可以加入和删除元素，并在各种操作中维持已有元素的顺序
（即保序），而且还具有以下行为特征：

基于下标（位置）的高效元素访问和更新，时间复杂度应该是O(1)；

为满足该特征，应该采用顺序表技术，表中元素保存在一块连续的存储区中。

允许任意加入元素，而且在不断加入元素的过程中，表对象的标识（函数id得到的值）不变。

为满足该特征，就必须能更换元素存储区，并且为保证更换存储区时list对象的标识id不变，只能采用分离式实现技术。

在Python的官方实现中，list就是一种采用分离式技术实现的动态顺序表。这就是为什么用list.append(x) （或 list.insert(len(list), x)，
即尾部插入）比在指定位置插入元素效率高的原因。

在Python的官方实现中，list实现采用了如下的策略：在建立空表（或者很小的表）时，系统分配一块能容纳8个元素的存储区；在执行插入操作
（insert或append）时，如果元素存储区满就换一块4倍大的存储区。但如果此时的表已经很大（目前的阀值为50000），则改变策略，采用加一倍的方法。
引入这种改变策略的方式，是为了避免出现过多空闲的存储位置。
'''
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = [ 234, 5,3, 4, 4,5, 6, 7 ]
tuple=(2, 3, 4, 5, 6, 7 )


#append
print('append')
list_ex=list2
list_ex.append(list1[3])#注意此时list2也被更改了，顺序表赋值以后指向的是原list的指针
print(list_ex)
print(list2)

#len
print('len')
print(len(list2))

#max
print('max')
print(max(list3))

#min
print('min')
print(min(list2))

#tuple转为list
print('tuple转为list')
print(list(tuple))


#sort对列表排序reverse = True 降序， reverse = False 升序（默认）
print('sort')
list3.sort(reverse = True)
print(list3)


#reverse()会向排序
print('reverse')
list3.reverse()
print(list3)

#count返回元素在列表中出现的次数
print('count')
print(list3.count('23'))

#index() 函数用于从列表中找出某个值@第一个@匹配项的索引位置
print('index')
print(list3.index(4))

#extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print('extend')
list3.extend(list2)
print(list3)

#insert() 函数用于将指定对象插入列表的指定位置O(n)
print('insert')
list2.insert(2,123)
print(list2)

#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print('pop')
print(list3.pop(-1))
print(list3)

#remove() 函数用于移除列表中某个值的第一个匹配项
print('remove')
list3.remove(4)
print(list3)