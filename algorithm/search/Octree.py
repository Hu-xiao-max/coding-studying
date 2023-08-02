import numpy as np

class OctreeNode:
    '''
    定义 OctreeNode 类：
    这个类表示八叉树的节点。每个节点包含以下属性：
    '''
    def __init__(self, center, size):
        self.center = center#center：节点的中心点，是一个三维坐标（numpy 数组）。
        self.size = size#size：节点的尺寸，表示该节点所表示的立方体区域的边长。
        self.children = [None] * 8#children：一个长度为 8 的列表，表示该节点的 8 个子节点。初始时所有子节点都为 None。
        self.points = []#points：一个列表，用于存储该节点内的点云数据。


    def insert(self, point):
        '''
        首先，我们检查当前节点是否满足插入条件。
        插入条件是：当前节点没有子节点，且存储的点云数量小于 1。
        这里只允许存储一个点，可以根据需要调整。如果满足条件，就将点添加到 points 列表中，并返回。
        '''
        if len(self.points) < 1 and all(child is None for child in self.children):
            self.points.append(point)
            #加入完第一个点（[0,0,0]）后返回退出接口
            return
   
        if all(child is None for child in self.children):#创建子节点
            self.subdivide()#从第二个点开始到最后一个点都要划分，此例中5个点所以除去第一个在上一个if中用过后要对剩下四个点划分四次

        for child in self.children:
            #把对应点放入子节点中
            if child.contains(point):
                child.insert(point)
                return#找到点对应所属的子节点后弹出

    def subdivide(self):
        for i in range(8):
            offset = np.array([(i >> 0) & 1, (i >> 1) & 1, (i >> 2) & 1]) 
            # i=0时：offset=0 0 0
            # i=1时：offset=1 0 0
            # i=2时：offset=0 1 0
            # i=3时：offset=1 1 0
            # i=4时：offset=0 0 1
            # i=5时：offset=1 0 1
            # i=6时：offset=0 1 1
            # i=7时：offset=1 1 1

            offset=offset* 0.5 - 0.25

            child_center = self.center + offset * self.size
            # print(child_center)
            child_size = self.size * 0.5

            #构建各个子结点
            self.children[i] = OctreeNode(child_center, child_size)
            
        # print(points)
        for point in self.points:
            self.insert(point)
            #进insert接口中的child的for循环，把point对应到子节点中
      
        self.points.clear()#清空points，self.points=[]


    def contains(self, point):
        #print(all(abs(point - self.center) <= self.size * 0.5))
        # 判断当前的point是否是在子节点的区域中
        return all(abs(point - self.center) <= self.size * 0.5)
    


    def intersects(self, aabb_min, aabb_max):
        return all(abs(self.center - (aabb_min + aabb_max) / 2) <= (self.size + aabb_max - aabb_min) * 0.5)

    def search(self, aabb_min, aabb_max):
        if not self.intersects(aabb_min, aabb_max):
            return []

        result = [point for point in self.points if np.all((point >= aabb_min) & (point <= aabb_max))]

        if any(child is not None for child in self.children):
            for child in self.children:
                result.extend(child.search(aabb_min, aabb_max))

        return result

if __name__ == "__main__":
    # 下面的代码实现的是给定n个点云，然后给定一个搜索范围，输出在这个范围内的点云
    # 创建一个八叉树根节点并插入一些点云数据
    root = OctreeNode(np.array([0, 0, 0]), 1)#[0, 0, 0]是节点中心点，1是节点尺寸
    list_points = np.array([
        [0, 0, 0],
        [0.1, 0.1, 0.1],
        [0.2, 0.2, 0.2],
        [0.3, 0.3, 0.3],
        [0.4, 0.4, 0.4],
    ])

    for point_in_list in list_points:
        root.insert(point_in_list)
        print(1)

    # 搜索给定范围内的点云
    aabb_min = np.array([0.15, 0.15, 0.15])
    aabb_max = np.array([0.5, 0.5, 0.5])
    search_result = root.search(aabb_min, aabb_max)
    print("Search result:", search_result)