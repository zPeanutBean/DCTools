import os
import sys
import subprocess
import time

def resource_path(relative):
    """用于访问 PyInstaller 解压后的资源（depends/）"""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.abspath(relative)


def current_dir():
    """EXE 所在目录（用于访问 dciot_build）"""
    return os.path.dirname(os.path.abspath(sys.argv[0]))


def launch():
    # DCIOT.exe 在 depends/ 中被打包
    depends_path = resource_path("depends")
    exe_path = os.path.join(depends_path, "DCIOT.exe")

    # dciot_build 在 EXE 所在目录
    project_path = os.path.join(current_dir(), "dciot_build")

    if not os.path.exists(exe_path):
        print("❌ 未找到 DCIOT.exe:", exe_path)
        return

    if not os.path.isdir(project_path):
        print("❌ 未找到 dciot_build 目录:", project_path)
        return

    # 设置 DLL 搜索路径
    env = os.environ.copy()
    env["PATH"] = depends_path + ";" + env["PATH"]

    print("启动:", exe_path)

    # 直接启动，无需参数
    subprocess.Popen([exe_path], shell=True, env=env)

    print("✅ 已启动 DCIOT！")


if __name__ == "__main__":
    launch()
    while True:
        time.sleep(1)
        print("✅ 已启动 DCIOT！")