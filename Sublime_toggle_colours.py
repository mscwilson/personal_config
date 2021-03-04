# ToggleColorsThemesCommand.py

import sublime
import sublime_plugin


class ToggleColorsThemesCommand(sublime_plugin.TextCommand):
  def run(self, edit, **args):
    settings = sublime.load_settings("Preferences.sublime-settings")

    light_theme = args["light_theme"]
    dark_theme = args["dark_theme"]

    light_color_scheme = args["light_color_scheme"]
    dark_color_scheme = args["dark_color_scheme"]

    current_theme = settings.get("theme", light_theme)

    if current_theme == light_theme:
      settings.set("theme", dark_theme)
      settings.set("color_scheme", dark_color_scheme)
    else:
      settings.set("theme", light_theme)
      settings.set("color_scheme", light_color_scheme)

    sublime.save_settings("Preferences.sublime-settings")
