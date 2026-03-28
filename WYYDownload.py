import requests as api
import tkinter as save
from tkinter import filedialog

root = save.Tk()
root.withdraw()
root.attributes("-topmost",True)#置顶选择保存路径的窗口

def get(id):
    return(api.get("https://api.byfuns.top/1/",params={"id":id},timeout=5))

def download(url, filename="音乐.mp3"):
    print("开始下载...")
    data = api.get(url, timeout=10).content
    with open(filename, "wb") as f:#创建文件并打开
        f.write(data)#写入文件
    print(f"下载完成！文件名：{filename}")

print("WYY Download\n")
print("作者：F_code\n")
id = input("音乐ID：")
print("处理中，大约等待5秒...")
res = get(id)
if res.status_code==200:
    print("完成，已确认歌曲存在，请选择后续操作")
    print("1.下载歌曲\n2.获取下载链接")
    a = input("请输入操作编号：")
    if a=="1":
        # 弹出保存对话框，让用户自己选位置和命名文件
        save_path = filedialog.asksaveasfilename(
            title="选择歌曲保存位置",
            defaultextension=".mp3",
            filetypes=[("MP3 音乐文件", "*.mp3")],
            initialfile=f"{id}.mp3"  # 默认文件名：音乐ID.mp3
        )
        # 判断用户有没有选择路径
        if save_path:
            download(res.text,save_path)
    if a=="2":
        print(res.text)
elif res.status_code==404:
    print("未找到歌曲，请重新启动程序尝试")