# -*- coding:utf-8 -*-
#一般都用js写，但是js没有队列的数据结构，就尝试用python写一写
#用python写要注意编码
#我的本地sublime没有连接python的编译器，所以我是在牛客上编辑通过的代码就直接复制过来了
import Queue
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        lst = []
        if root==None:
            return lst
        q = Queue.Queue()
        q.put(root)
        while not q.empty():
            current = q.get()
            lst.append(current.val)
            if current.left!=None:
                q.put(current.left)
            if current.right!=None:
                q.put(current.right)
        return lst
#python的语句为空要写pass
#声明一个空数组可以就像js那样
#题目，层序遍历二叉树，通过列队，在每一轮循环中实现：取出当前节点-左结点入列-右节点入列
#这样，几次循环后完成一层的输出
