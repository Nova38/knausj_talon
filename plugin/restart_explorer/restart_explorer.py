import ctypes
import subprocess
from talon import Context, Module, actions

ctx = Context()
# ctx.matches = r"""
# os: windows
# """

mod=Module()
@mod.action_class
# @ctx.action_class("win")
class WinActions:
    def restart_explorer():
        """Restart Windows"""
        subprocess.call(["taskkill", "/F", "/IM", "explorer.exe"])
        subprocess.Popen("explorer.exe")


