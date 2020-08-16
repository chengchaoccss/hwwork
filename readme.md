## 这是我的个人学习记录的代码，用来在不同服务器之间进行代码git

1. ssh公钥创建并在github上正确添加。
2. git在本地电脑上正确安装并配置。
3. 如果直接push不上去，可以使用先git clone的方法来创建本地与服务器之间的连接，然后再push。
4. 这条笔记是在华为服务器上添加的。1-3步没有问题。
5. 此处出现了一个问题，服务器上每次使用git push命令都需要输入密码，解决方法是：git config --global credential.helper store。输入该命令后在git push，可行！
