# 大彩无需VisualTFT运行模拟器
1. 解决了编写串口上位机的工作
2. 无需大彩屏幕硬件 和 `VisualTFT` 直接pc即可
3. 内部测试人员无需屏幕即可完成测试



---

@[TOC](文章目录)

---

# 前言

编写这个软件的初心是因为公司里有些测试工作, 但是公司的大彩屏幕申请流程复杂
测试人员又不想在pc上装 `VisualTFT` 
于是产生了能不能不要  `VisualTFT` 直接运行模拟器.
亦或是方便直接给客户展示`demo`
便有了这个工具.

---

`提示：以下是本篇文章正文内容，下面案例可供参考`

# 一、效果展示

双击运行 exe 即可
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/378d658c92ee47618c79ce9db3e66e08.png)




# 二、📱使用方法

1. 将Dacia  `VisualTFT` 项目目录下编译完成的 `dciot_build` 目录复制。
2. 替换本程序(DCTools.exe)目录下的 `dciot_build` 即可。
3. 双击运行本程序 (DCTools.exe)。

---

# 三、下载地址

[https://ahsd.lanzoub.com/ioTKA3cqxpyj](https://ahsd.lanzoub.com/ioTKA3cqxpyj)

# 总结
 预祝各位同行开发愉快.

若对对方造成负面影响可联系本人删除



# DCTools

# pack cmd

```
pyinstaller --onefile --add-data "depends;depends" --icon="logo.ico" --name=demo2.exe pack.py
```
