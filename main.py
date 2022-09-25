import tkinter,webbrowser,os,time
from urllib.request import urlretrieve

def cbk(a,b,c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    print('\r 已下载:%.2f%%' % per, end='')


窗口 = tkinter.Tk()#创造窗口

窗口.geometry('400x300') # 设置窗口大小
窗口.resizable() # 允许用户拉伸主窗口大小
窗口.minsize(200,150)	# 设置窗口被允许调整的最小范围，即宽和高各50
窗口.maxsize(400,300)	# 设置窗口被允许调整的最大范围，即宽和高各400

窗口.title('安装工具') #设置窗口标题

按钮 = tkinter.Button(窗口,text="关闭",width=20,command=窗口.quit) # 添加按钮

按钮.pack(side="bottom") # 将按钮放置在主窗口内

标签 = tkinter.Label(窗口,text="你好欢迎访问 乌清远.top")# 添加标签
标签.pack(side="top") # 将标签放置在主窗口内

def 点击按钮1():
	print(" ---开始下载--- ")
	#下载文件
	urls = ["https://download-ssl.firefox.com.cn/releases-sha2/stub/official/zh-CN/Firefox-latest.exe"
	,"https://dldir1.qq.com/qqfile/qq/PCQQ9.6.7/QQ9.6.7.28815.exe"
	,"https://dldir1.qq.com/weixin/Windows/WeChatSetup.exe"
	,"https://registry.npmmirror.com/-/binary/python/3.9.9/python-3.9.9.exe"
	,"https://dl.hdslb.com/mobile/fixed/bili_win/bili_win-install.exe?v=1.6.1"
	]
	第几文件=1
	for url in urls:
		dir=os.path.abspath('.')
		work_path=os.path.join(dir,str(第几文件)+'.exe')
		urlretrieve(url,work_path,cbk)
		print(" 下载：第"+str(第几文件)+"文件")
		第几文件 = 第几文件+1
	print(" ---安装开始--- ")
	第几文件=1
	for url in urls:
		os.system(os.path.join(dir,str(第几文件)+'.exe'))
		第几文件 = 第几文件+1  
	print(" ---安装完成--- ")
	print(" 给我点赞快！！！")
	webbrowser.open_new("https://space.bilibili.com/692730692")
	
	
按钮1 = tkinter.Button(窗口,text="快速安装\n通用软件\n开发工具",width=20,height=5,command=点击按钮1) # 添加按钮

按钮1.pack(expand=True)

def 点击按钮2():
	print(" 你好朋友\n 我叫乌清远xqy")
	webbrowser.open_new("https://space.bilibili.com/692730692")

按钮2 = tkinter.Button(窗口,text="为我点赞谢谢。。",width=20,command=点击按钮2) # 添加按钮

按钮2.pack(side="bottom")

窗口.mainloop() #显示窗口