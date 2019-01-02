from xml.dom import minidom
#打开xml文件
dom=minidom.parse('class_info.xml')
#获取文档对象,读取根节点的信息
root=dom.documentElement
#根据标签名获取标签对象
names=root.getElementsByTagName('name')
ages=root.getElementsByTagName('age')
citys=root.getElementsByTagName('city')

logins=root.getElementsByTagName('login')

# for i in range(2):
#     username=logins[i].getAttribute('username')
#     print(username)
#     password=logins[i].getAttribute('password')
#     print(password)
#分别打印内容
# for i in range(4):
#     print(names[i].firstChild.data)
#     print(ages[i].firstChild.data)
#     print(citys[i].firstChild.data)
# print(root.nodeName)
# print(root.nodeValue)
# print(root.nodeType)

tags=root.getElementsByTagName('student')
print(tags[0].nodeName)
print(tags[0].tagName)
print(tags[0].nodeType)
print(tags[0].nodeValue)
