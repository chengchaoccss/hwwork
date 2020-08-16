import uiautomator2 as u2
import time
d = u2.connect('9YS0219C14014108')
# d = u2.connect('http://192.168.1.108:5555')
# d(text='浏览器').click()
# d=u2.connect_wifi('192.168.1.108')
# d.app_install('http://p.gdown.baidu.com/e4694b371a896a11d290bb97a21a3c9d6bf387c313475e182332eb93f8ac18714e2d96bcb93c3b16d51d2bb07948112cd540bbe311658cf6aabf061cee1c3942378d1f4ca23780f74e677c7f3bbd97faac9442fdbe41a93bc1250aa4f4faf971cae8e6d56f917a9ed557bb9407d8ef69d115d925101307df84c78cfd86765ea338f486d0806af17f4d7cc59ef40fd3be352c4ee3ae8c6df14e181b15a47a2c2c11a8e5846c47e709a7fb0f4a3dc8a872b28a5ab6d6f59a03b8420f96f1a4d67c')
# print(d.info)
# url='http://p.gdown.baidu.com/c977ae1dfa3207627452de8347c82ae8fdaa682a14999ed5576246dd44debfb0880c211ca98ad7b0bac174ee58e205567b88b7c44154ffdf9e90f692ea56240a7ad8739b19e84b3f8b872d3bd0471c6bce23ad603e62cb3a84500d3954417cf9ebc7ac6253a22fd3e2872112f5468c6d6ef387f1cfb2f67a7bbd26c78a6c88a004f561042bc9a07de1378bf2a22cb857a16d82eb15a7722aa137a2dcf37133c1018282efae52af3a13809f8c37646b6ba995d909ff4f2097ae2cbe0e58ab48d9340d051c3959ccd54cc0634fc6f63aa6aa6c9692e90c64864f1d06f768f6b8a98933e6fb85485b422d130c52611a8f1f490c65bce63c3a391ccc453d964bfab2e73320a1ee02a4b9aaa0085c2dc027cc'
# d.app_install(url)
# d.press('home')
# d.press('home')
# d(text='腾讯新闻').click()
print(d.app_current())
d.app_start('com.android.gallery3d')
# d.app_stop('com.tencent.news')
# d.app_uninstall('com.baidu.searchbox')