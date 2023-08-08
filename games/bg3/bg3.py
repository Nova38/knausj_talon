from talon import Context, Module, actions, app
ctx = Context()
mod = Module()
apps = mod.apps
apps.bg3 = "app.name: bg3.exe"
apps.bg3 = """
os: windows
and app.name: bg3.exe
os: windows
and app.exe: bg3.exe
"""


ctx.matches = r"""
os: windows
os: linux
os: mac
tag: game
app: bg3
"""