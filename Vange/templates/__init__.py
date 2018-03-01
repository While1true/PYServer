# #coding:utf-8
#
# import win32clipboard as w
# import win32con
#
# #获取剪切板内容
# def gettext():
#     w.OpenClipboard()
#     t = w.GetClipboardData(win32con.CF_TEXT)
#     w.CloseClipboard()
#     return t
#
# #写入剪切板内容
# def settext(aString):
#     w.OpenClipboard()
#     w.EmptyClipboard()
#     w.SetClipboardData(win32con.CF_TEXT, aString)
#     w.CloseClipboard()
# a="aaaa"
# settext(a)
# str=gettext()
# x=b"\x00"
# print(str.decode("utf-8").replace(x.decode("utf-8"),""))