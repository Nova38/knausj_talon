import json

from talon import Context, Module, actions, app

key = actions.key
insert = actions.insert
edit = actions.edit
vscode = actions.user.vscode


is_mac = app.platform == "mac"

ctx = Context()
mac_ctx = Context()
mod = Module()
mod.apps.vscode = """
os: mac
and app.bundle: com.microsoft.VSCode
os: mac
and app.bundle: com.microsoft.VSCodeInsiders
os: mac
and app.bundle: com.visualstudio.code.oss
"""
mod.apps.vscode = """
os: linux
and app.name: Code
os: linux
and app.name: code-oss
os: linux
and app.name: code-insiders
os: linux
and app.name: VSCodium
os: linux
and app.name: Codium
"""
mod.apps.vscode = r"""
os: windows
and app.name: Visual Studio Code
os: windows
and app.name: Visual Studio Code Insiders
os: windows
and app.name: Visual Studio Code - Insiders
os: windows
and app.exe: /^code\.exe$/i
os: windows
and app.exe: /^code-insiders\.exe$/i
os: windows
and app.name: VSCodium
os: windows
and app.exe: /^vscodium\.exe$/i
os: windows
and app.name: Azure Data Studio
os: windows
and app.exe: azuredatastudio.exe
"""

ctx.matches = r"""
app: vscode
"""
mac_ctx.matches = r"""
os: mac
app: vscode
"""


@ctx.action_class("app")
class AppActions:
    # talon app actions
    def tab_open():
        vscode("workbench.action.files.newUntitledFile")

    def tab_close():
        vscode("workbench.action.closeActiveEditor")

    def tab_next():
        vscode("workbench.action.nextEditorInGroup")

    def tab_previous():
        vscode("workbench.action.previousEditorInGroup")

    def tab_reopen():
        vscode("workbench.action.reopenClosedEditor")

    def window_close():
        vscode("workbench.action.closeWindow")

    def window_open():
        vscode("workbench.action.newWindow")


@ctx.action_class("code")
class CodeActions:
    # talon code actions
    def toggle_comment():
        vscode("editor.action.commentLine")


@ctx.action_class("edit")
class EditActions:
    # talon edit actions
    def indent_more():
        vscode("editor.action.indentLines")

    def indent_less():
        vscode("editor.action.outdentLines")

    def save_all():
        vscode("workbench.action.files.saveAll")

    def find(text=None):
        if is_mac:
            key("cmd-f")
        else:
            key("ctrl-f")
        if text is not None:
            actions.insert(text)

    def line_swap_up():
        key("alt-up")

    def line_swap_down():
        key("alt-down")

    def line_clone():
        key("shift-alt-down")

    def line_insert_down():
        vscode("editor.action.insertLineAfter")

    def line_insert_up():
        vscode("editor.action.insertLineBefore")

    def jump_line(n: int):
        vscode("workbench.action.gotoLine")
        actions.insert(str(n))
        key("enter")
        actions.edit.line_start()


@ctx.action_class("win")
class WinActions:
    def filename():
        title = actions.win.title()
        # this doesn't seem to be necessary on VSCode for Mac
        # if title == "":
        #    title = ui.active_window().doc

        if is_mac:
            result = title.split(" — ")[0]
        else:
            result = title.split(" - ")[0]

        if "." in result:
            return result

        return ""


@mod.action_class
class Actions:
    def vscode_terminal(number: int):
        """Activate a terminal by number"""
        vscode(f"workbench.action.terminal.focusAtIndex{number}")

    def command_palette():
        """Show command palette"""
        key("ctrl-shift-p")

    def copy_command_id():
        """
        Copy the command id of the focused menu item

        From: https://github.com/AndreasArvidsson/andreas-talon/blob/ef049e9cf50b2694ee1b2f039fc102bd488ca1ae/apps/vscode/vscode.py#L382-L389
        """
        key("tab:2 enter")
        actions.sleep("500ms")
        json_text = actions.edit.selected_text()
        command_id = json.loads(json_text)["command"]
        print(command_id)
        actions.app.tab_close()
        actions.clip.set_text(command_id)


@mac_ctx.action_class("user")
class MacUserActions:
    def command_palette():
        key("cmd-shift-p")


@ctx.action_class("user")
class UserActions:
    # splits.py support begin
    def split_clear_all():
        vscode("workbench.action.editorLayoutSingle")

    def split_clear():
        vscode("workbench.action.joinTwoGroups")

    def split_flip():
        vscode("workbench.action.toggleEditorGroupLayout")

    def split_maximize():
        vscode("workbench.action.maximizeEditor")

    def split_reset():
        vscode("workbench.action.evenEditorWidths")

    def split_last():
        vscode("workbench.action.focusLeftGroup")

    def split_next():
        actions.user.vscode_and_wait("workbench.action.focusRightGroup")

    def split_window_down():
        vscode("workbench.action.moveEditorToBelowGroup")

    def split_window_horizontally():
        vscode("workbench.action.splitEditorOrthogonal")

    def split_window_left():
        vscode("workbench.action.moveEditorToLeftGroup")

    def split_window_right():
        vscode("workbench.action.moveEditorToRightGroup")

    def split_window_up():
        vscode("workbench.action.moveEditorToAboveGroup")

    def split_window_vertically():
        vscode("workbench.action.splitEditor")

    def split_window():
        vscode("workbench.action.splitEditor")

    # splits.py support end

    # multiple_cursor.py support begin
    # note: vscode has no explicit mode for multiple cursors
    def multi_cursor_add_above():
        vscode("editor.action.insertCursorAbove")

    def multi_cursor_add_below():
        vscode("editor.action.insertCursorBelow")

    def multi_cursor_add_to_line_ends():
        vscode("editor.action.insertCursorAtEndOfEachLineSelected")

    def multi_cursor_disable():
        key("escape")

    def multi_cursor_enable():
        actions.skip()

    def multi_cursor_select_all_occurrences():
        vscode("editor.action.selectHighlights")

    def multi_cursor_select_fewer_occurrences():
        vscode("cursorUndo")

    def multi_cursor_select_more_occurrences():
        vscode("editor.action.addSelectionToNextFindMatch")

    def multi_cursor_skip_occurrence():
        vscode("editor.action.moveSelectionToNextFindMatch")

    def tab_jump(number: int):
        if number < 10:
            if is_mac:
                actions.user.vscode_with_plugin(
                    f"workbench.action.openEditorAtIndex{number}"
                )
            else:
                key(f"alt-{number}")
        else:
            actions.user.vscode_with_plugin(
                "workbench.action.openEditorAtIndex", number
            )

    def tab_final():
        if is_mac:
            vscode("workbench.action.lastEditorInGroup")
        else:
            key("alt-0")

    # splits.py support begin
    def split_number(index: int):
        """Navigates to a the specified split"""
        if index < 9:
            if is_mac:
                key(f"cmd-{index}")
            else:
                key(f"ctrl-{index}")

    # splits.py support end

    # find_and_replace.py support begin

    def find(text: str):
        """Triggers find in current editor"""
        if is_mac:
            key("cmd-f")
        else:
            key("ctrl-f")

        if text:
            actions.insert(text)

    def find_next():
        vscode("editor.action.nextMatchFindAction")

    def find_previous():
        vscode("editor.action.previousMatchFindAction")

    def find_everywhere(text: str):
        """Triggers find across project"""
        if is_mac:
            key("cmd-shift-f")
        else:
            key("ctrl-shift-f")

        if text:
            actions.insert(text)

    def find_toggle_match_by_case():
        """Toggles find match by case sensitivity"""
        if is_mac:
            key("alt-cmd-c")
        else:
            key("alt-c")

    def find_toggle_match_by_word():
        """Toggles find match by whole words"""
        if is_mac:
            key("cmd-alt-w")
        else:
            key("alt-w")

    def find_toggle_match_by_regex():
        """Toggles find match by regex"""
        if is_mac:
            key("cmd-alt-r")
        else:
            key("alt-r")

    def replace(text: str):
        """Search and replaces in the active editor"""
        if is_mac:
            key("alt-cmd-f")
        else:
            key("ctrl-h")

        if text:
            actions.insert(text)

    def replace_everywhere(text: str):
        """Search and replaces in the entire project"""
        if is_mac:
            key("cmd-shift-h")
        else:
            key("ctrl-shift-h")

        if text:
            actions.insert(text)

    def replace_confirm():
        """Confirm replace at current position"""
        if is_mac:
            key("shift-cmd-1")
        else:
            key("ctrl-shift-1")

    def replace_confirm_all():
        """Confirm replace all"""
        if is_mac:
            key("cmd-enter")
        else:
            key("ctrl-alt-enter")

    def select_previous_occurrence(text: str):
        actions.edit.find(text)
        actions.sleep("100ms")
        key("shift-enter esc")

    def select_next_occurrence(text: str):
        actions.edit.find(text)
        actions.sleep("100ms")
        key("esc")

    def insert_snippet(body: str):
        actions.user.run_rpc_command("editor.action.insertSnippet", {"snippet": body})

    # def vscode_add_missing_imports():
    #     """Add all missing imports"""
    #     vscode(
    #         "editor.action.sourceAction",
    #         {"kind": "source.addMissingImports", "apply": "first"},
    #     )
