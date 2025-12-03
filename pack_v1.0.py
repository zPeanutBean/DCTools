import os
import sys
import subprocess
import time
import qrcode 


QR_README = """
==============================================
📱 使用方法
==============================================
1. 将Dacia项目编译完成的 `dciot_build` 目录复制。
2. 放到本程序(DCTools.exe)放在同一目录下。
3. 双击运行本程序 (DCTools.exe)。
good luck to you!
"""


# --- 核心辅助函数 ---

def resource_path(relative):
    """用于访问 PyInstaller 解压后的资源（depends/）"""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.abspath(relative)


def current_dir():
    """EXE 所在目录（用于访问 dciot_build）"""
    return os.path.dirname(os.path.abspath(sys.argv[0]))



# --- 程序启动逻辑 ---
def launch():
    # DCIOT.exe 在 depends/ 中被打包
    depends_path = resource_path("depends")
    exe_path = os.path.join(depends_path, "DCIOT.exe")

    # dciot_build 在 EXE 所在目录
    project_path = os.path.join(current_dir(), "dciot_build")
    print(f"项目目录: {project_path}")

    if not os.path.exists(exe_path):
        print("❌ 未找到 DCIOT.exe:", exe_path)
        return

    if not os.path.isdir(project_path):
        print("❌ 未找到 dciot_build 目录:", project_path)
        return

    # 设置 DLL 搜索路径
    env = os.environ.copy()
    env["PATH"] = depends_path + ";" + env["PATH"]

    # --- 启动 DCIOT.exe ---
    try:
        # **【关键修改】**：
        # 传递包含两个元素的列表：[可执行文件路径, 参数路径]
        # 对应命令行： "DCIOT.exe" "dciot_build_path"
        subprocess.Popen([exe_path, project_path], env=env)
        
        print("✅ 已启动 DCTools@Tfei！\n")

        print(QR_README)

        print("\n" + "="*50)
        print("🐼 前往主页查看最近更新和更多工具！")
        print("="*50)
        print("🏠 主页：https://github.com/zPeanutBean")
        print("📢 QQ群：1003899431")
        


    except Exception as e:
        print(f"❌ 启动 DCIOT.exe 失败: {e}")


if __name__ == "__main__":
    launch()
    # 保持主进程运行
    while True:
        time.sleep(1)