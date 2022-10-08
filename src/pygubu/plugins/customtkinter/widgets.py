from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
    register_custom_property,
)
from pygubu.i18n import _
from pygubu.plugins.tk.tkstdwidgets import TKFrame as TKFrameBO
from pygubu.plugins.tk.tkstdwidgets import TKLabel as TKLabelBO
from pygubu.plugins.tk.tkstdwidgets import TKEntry as TKEntryBO
from customtkinter import (
    CTkFrame,
    CTkLabel,
    CTkButton,
    CTkProgressBar,
    CTkSlider,
    CTkEntry,
    CTkOptionMenu,
    CTkComboBox,
    CTkCheckBox,
    CTkRadioButton,
    CTkSwitch,
)

from ..customtkinter import _designer_tab_label, _plugin_uid
from .ctkbase import CTkBaseMixin


class CTkFrameBO(CTkBaseMixin, TKFrameBO):
    class_ = CTkFrame
    OPTIONS_CUSTOM = (
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "corner_radius",
    )
    properties = (
        TKFrameBO.OPTIONS_STANDARD + TKFrameBO.OPTIONS_SPECIFIC + OPTIONS_CUSTOM
    )


_builder_uid = f"{_plugin_uid}.CTkFrame"
register_widget(
    _builder_uid,
    CTkFrameBO,
    "CTkFrame",
    ("ttk", _designer_tab_label),
    group=0,
)
register_custom_property(_builder_uid, "bg_color", "colorentry")
register_custom_property(_builder_uid, "fg_color", "colorentry")
register_custom_property(_builder_uid, "border_color", "colorentry")
register_custom_property(_builder_uid, "border_width", "entry")
register_custom_property(_builder_uid, "corner_radius", "entry")


class CTkLabelBO(CTkBaseMixin, TKLabelBO):
    class_ = CTkLabel
    OPTIONS_CUSTOM = (
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "corner_radius",
    )
    properties = (
        TKLabelBO.OPTIONS_STANDARD + TKLabelBO.OPTIONS_SPECIFIC + OPTIONS_CUSTOM
    )


_builder_uid = f"{_plugin_uid}.CTkLabel"
register_widget(
    _builder_uid,
    CTkLabelBO,
    "CTkLabel",
    ("ttk", _designer_tab_label),
    group=1,
)
register_custom_property(_builder_uid, "bg_color", "colorentry")
register_custom_property(_builder_uid, "fg_color", "colorentry")
register_custom_property(_builder_uid, "border_color", "colorentry")
register_custom_property(_builder_uid, "border_width", "entry")
register_custom_property(_builder_uid, "corner_radius", "entry")


class CTkProgressBarBO(CTkBaseMixin, BuilderObject):
    class_ = CTkProgressBar
    allow_bindings = False
    OPTIONS_SPECIFIC = ("width", "height", "variable", "orient", "mode")
    OPTIONS_CUSTOM = (
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "corner_radius",
        "progress_color",
        "determinate_speed",
        "indeterminate_speed",
    )
    properties = OPTIONS_SPECIFIC + OPTIONS_CUSTOM
    ro_properties = ("orient",)


_builder_uid = f"{_plugin_uid}.CTkProgressBar"
register_widget(
    _builder_uid,
    CTkProgressBarBO,
    "CTkProgressBar",
    ("ttk", _designer_tab_label),
    group=1,
)


class CTkButtonBO(CTkBaseMixin, BuilderObject):
    class_ = CTkButton
    allow_bindings = False
    OPTIONS_SPECIFIC = (
        "text",
        "width",
        "height",
        "textvariable",
        "image",
        "compound",
        "state",
        "command",
    )
    OPTIONS_CUSTOM = (
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "corner_radius",
        "hover_color",
        "text_color",
        "text_color_disabled",
        "text_font",
        "hover",
    )
    properties = OPTIONS_SPECIFIC + OPTIONS_CUSTOM
    ro_properties = ("hover",)


_builder_uid = f"{_plugin_uid}.CTkButton"
register_widget(
    _builder_uid,
    CTkButtonBO,
    "CTkButton",
    ("ttk", _designer_tab_label),
    group=1,
)

register_custom_property(_builder_uid, "bg_color", "colorentry")
register_custom_property(_builder_uid, "fg_color", "colorentry")
register_custom_property(_builder_uid, "border_color", "colorentry")
register_custom_property(_builder_uid, "border_width", "entry")
register_custom_property(_builder_uid, "corner_radius", "entry")
register_custom_property(_builder_uid, "hover_color", "colorentry")
register_custom_property(_builder_uid, "text_color", "colorentry")
register_custom_property(_builder_uid, "text_color_disabled", "colorentry")
register_custom_property(_builder_uid, "text_font", "fontentry")
register_custom_property(
    _builder_uid,
    "hover",
    "choice",
    values=("", "True", "False"),
    state="readonly",
)


class CTkSliderBO(CTkBaseMixin, BuilderObject):
    class_ = CTkSlider
    allow_bindings = False
    OPTIONS_SPECIFIC = (
        "width",
        "height",
        "orient",
        "variable",
        "from_",
        "to",
        "command",
        "state",
    )
    OPTIONS_CUSTOM = (
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "corner_radius",
        "progress_color",
        "button_color",
        "button_hover_color",
        "button_corner_radius",
        "button_length",
        "number_of_steps",
    )
    properties = OPTIONS_SPECIFIC + OPTIONS_CUSTOM
    ro_properties = ("orient", "button_length")


_builder_uid = f"{_plugin_uid}.CTkSlider"
register_widget(
    _builder_uid,
    CTkSliderBO,
    "CTkSlider",
    ("ttk", _designer_tab_label),
    group=1,
)

register_custom_property(_builder_uid, "bg_color", "colorentry")
register_custom_property(_builder_uid, "fg_color", "colorentry")
register_custom_property(_builder_uid, "border_color", "colorentry")
register_custom_property(_builder_uid, "border_width", "entry")
register_custom_property(_builder_uid, "corner_radius", "entry")
register_custom_property(_builder_uid, "progress_color", "colorentry")
register_custom_property(_builder_uid, "button_color", "colorentry")
register_custom_property(_builder_uid, "button_hover_color", "colorentry")
register_custom_property(_builder_uid, "button_corner_radius", "entry")
register_custom_property(_builder_uid, "button_length", "entry")
register_custom_property(_builder_uid, "number_of_steps", "entry")


class CTkEntryBO(CTkBaseMixin, TKEntryBO):
    class_ = CTkEntry
    allow_bindings = False
    OPTIONS_CUSTOM = TKEntryBO.OPTIONS_CUSTOM + (
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "corner_radius",
        "text_color",
        "placeholder_text_color",
        "text_font",
        "placeholder_text",
    )
    properties = (
        TKEntryBO.OPTIONS_STANDARD + TKEntryBO.OPTIONS_SPECIFIC + OPTIONS_CUSTOM
    )

    def _set_property(self, target_widget, pname, value):
        real_entry = target_widget.entry
        if pname == "text":
            wstate = str(real_entry["state"])
            if wstate != "normal":
                # change state temporarily
                real_entry["state"] = "normal"
            real_entry.delete(0, "end")
            real_entry.insert(0, value)
            real_entry["state"] = wstate
        else:
            super()._set_property(target_widget, pname, value)


_builder_uid = f"{_plugin_uid}.CTkEntry"
register_widget(
    _builder_uid,
    CTkEntryBO,
    "CTkEntry",
    ("ttk", _designer_tab_label),
    group=1,
)

register_custom_property(_builder_uid, "bg_color", "colorentry")
register_custom_property(_builder_uid, "fg_color", "colorentry")
register_custom_property(_builder_uid, "border_color", "colorentry")
register_custom_property(_builder_uid, "border_width", "entry")
register_custom_property(_builder_uid, "corner_radius", "entry")
register_custom_property(_builder_uid, "text_color", "colorentry")
register_custom_property(_builder_uid, "placeholder_text_color", "colorentry")
register_custom_property(_builder_uid, "text_font", "fontentry")
register_custom_property(_builder_uid, "placeholder_text", "entry")


class CTkOptionMenuBO(CTkBaseMixin, BuilderObject):
    class_ = CTkOptionMenu
    allow_bindings = False
    OPTIONS_SPECIFIC = ("command", "variable", "values")
    OPTIONS_CUSTOM = (
        "bg_color",
        "fg_color",
        "button_color",
        "button_hover_color",
        "text_color",
        "text_color_disabled",
        "dropdown_hover_color",
        "dropdown_text_color",
        "dropdown_color",
        "width",
        "height",
        "corner_radius",
        "text_font",
        "state",
        "dynamic_resizing",
    )
    properties = (
        BuilderObject.OPTIONS_STANDARD + OPTIONS_SPECIFIC + OPTIONS_CUSTOM
    )
    command_properties = ("command",)

    def _code_define_callback_args(self, cmd_pname, cmd):
        return ("current_value",)


_builder_uid = f"{_plugin_uid}.CTkOptionMenu"
register_widget(
    _builder_uid,
    CTkOptionMenuBO,
    "CTkOptionMenu",
    ("ttk", _designer_tab_label),
    group=1,
)
register_custom_property(_builder_uid, "bg_color", "colorentry")
register_custom_property(_builder_uid, "fg_color", "colorentry")
register_custom_property(_builder_uid, "button_color", "colorentry")
register_custom_property(_builder_uid, "button_hover_color", "colorentry")
register_custom_property(_builder_uid, "text_color", "colorentry")
register_custom_property(_builder_uid, "text_color_disabled", "colorentry")
register_custom_property(_builder_uid, "dropdown_hover_color", "colorentry")
register_custom_property(_builder_uid, "dropdown_text_color", "colorentry")
register_custom_property(_builder_uid, "dropdown_color", "colorentry")
register_custom_property(_builder_uid, "width", "dimensionentry")
register_custom_property(_builder_uid, "height", "dimensionentry")
register_custom_property(_builder_uid, "corner_radius", "entry")
register_custom_property(_builder_uid, "text_font", "fontentry")
register_custom_property(
    _builder_uid,
    "state",
    "choice",
    values=("", "normal", "active", "disabled"),
    state="readonly",
)
register_custom_property(
    _builder_uid,
    "dynamic_resizing",
    "choice",
    values=("", "True", "False"),
    state="readonly",
)
register_custom_property(_builder_uid, "command", "simplecommandentry")
register_custom_property(_builder_uid, "variable", "tkvarentry")
register_custom_property(_builder_uid, "values", "entry")


class CTkComboBoxBO(CTkBaseMixin, BuilderObject):
    class_ = CTkComboBox
    allow_bindings = False
    OPTIONS_SPECIFIC = ("command", "variable", "values")
    OPTIONS_CUSTOM = (
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "button_color",
        "button_hover_color",
        "text_color",
        "text_color_disabled",
        "dropdown_hover_color",
        "dropdown_text_color",
        "dropdown_color",
        "width",
        "height",
        "corner_radius",
        "text_font",
        "dropdown_text_font",
        "state",
        "hover",
    )
    properties = (
        BuilderObject.OPTIONS_STANDARD + OPTIONS_SPECIFIC + OPTIONS_CUSTOM
    )
    command_properties = ("command",)
    ro_properties = ("hover",)

    def _code_define_callback_args(self, cmd_pname, cmd):
        return ("value",)


_builder_uid = f"{_plugin_uid}.CTkComboBox"
register_widget(
    _builder_uid,
    CTkComboBoxBO,
    "CTkComboBox",
    ("ttk", _designer_tab_label),
    group=1,
)
register_custom_property(_builder_uid, "bg_color", "colorentry")
register_custom_property(_builder_uid, "fg_color", "colorentry")
register_custom_property(_builder_uid, "border_color", "colorentry")
register_custom_property(_builder_uid, "border_width", "entry")
register_custom_property(_builder_uid, "button_color", "colorentry")
register_custom_property(_builder_uid, "button_hover_color", "colorentry")
register_custom_property(_builder_uid, "text_color", "colorentry")
register_custom_property(_builder_uid, "text_color_disabled", "colorentry")
register_custom_property(_builder_uid, "dropdown_hover_color", "colorentry")
register_custom_property(_builder_uid, "dropdown_text_color", "colorentry")
register_custom_property(_builder_uid, "dropdown_color", "colorentry")
register_custom_property(_builder_uid, "width", "dimensionentry")
register_custom_property(_builder_uid, "height", "dimensionentry")
register_custom_property(_builder_uid, "corner_radius", "entry")
register_custom_property(_builder_uid, "text_font", "fontentry")
register_custom_property(_builder_uid, "dropdown_text_font", "fontentry")
register_custom_property(
    _builder_uid,
    "state",
    "choice",
    values=("", "normal", "active", "disabled"),
    state="readonly",
)
register_custom_property(
    _builder_uid,
    "dynamic_resizing",
    "choice",
    values=("", "True", "False"),
    state="readonly",
)
register_custom_property(_builder_uid, "command", "simplecommandentry")
register_custom_property(_builder_uid, "variable", "tkvarentry")
register_custom_property(_builder_uid, "values", "entry")
register_custom_property(
    _builder_uid,
    "hover",
    "choice",
    values=("", "True", "False"),
    state="readonly",
)


class CTkCheckBoxBO(CTkBaseMixin, BuilderObject):
    class_ = CTkCheckBox
    allow_bindings = False
    OPTIONS_STANDARD = ("textvariable",)
    OPTIONS_SPECIFIC = (
        "command",
        "variable",
        "variable",
        "onvalue",
        "offvalue",
        "state",
        "width",
        "height",
    )
    OPTIONS_CUSTOM = (
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "checkmark_color",
        "text",
        "text_font",
        "text_color",
        "text_color_disabled",
        "corner_radius",
        "hover",
        "hover_color",
    )
    properties = OPTIONS_STANDARD + OPTIONS_SPECIFIC + OPTIONS_CUSTOM
    command_properties = ("command",)
    ro_properties = ("hover",)


_builder_uid = f"{_plugin_uid}.CTkCheckBox"
register_widget(
    _builder_uid,
    CTkCheckBoxBO,
    "CTkCheckBox",
    ("ttk", _designer_tab_label),
    group=1,
)

register_custom_property(_builder_uid, "bg_color", "colorentry")
register_custom_property(_builder_uid, "fg_color", "colorentry")
register_custom_property(_builder_uid, "border_color", "colorentry")
register_custom_property(_builder_uid, "border_width", "entry")
register_custom_property(_builder_uid, "text", "text")
register_custom_property(_builder_uid, "text_font", "fontentry")
register_custom_property(_builder_uid, "text_color", "colorentry")
register_custom_property(_builder_uid, "text_color_disabled", "colorentry")
register_custom_property(_builder_uid, "checkmark_color", "colorentry")
register_custom_property(_builder_uid, "width", "dimensionentry")
register_custom_property(_builder_uid, "height", "dimensionentry")
register_custom_property(_builder_uid, "corner_radius", "entry")
register_custom_property(_builder_uid, "command", "simplecommandentry")
register_custom_property(
    _builder_uid,
    "hover",
    "choice",
    values=("", "True", "False"),
    state="readonly",
)
register_custom_property(_builder_uid, "hover_color", "colorentry")


class CTkRadioButtonBO(CTkBaseMixin, BuilderObject):
    class_ = CTkRadioButton
    allow_bindings = False
    OPTIONS_STANDARD = ("textvariable",)
    OPTIONS_SPECIFIC = (
        "command",
        "variable",
        "variable",
        "onvalue",
        "offvalue",
        "state",
        "width",
        "height",
    )
    OPTIONS_CUSTOM = (
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "checkmark_color",
        "text",
        "text_font",
        "text_color",
        "text_color_disabled",
        "corner_radius",
        "hover",
        "hover_color",
    )
    properties = OPTIONS_STANDARD + OPTIONS_SPECIFIC + OPTIONS_CUSTOM
    command_properties = ("command",)
    ro_properties = ("hover",)


_builder_uid = f"{_plugin_uid}.CTkRadioButton"
register_widget(
    _builder_uid,
    CTkRadioButtonBO,
    "CTkRadioButton",
    ("ttk", _designer_tab_label),
    group=1,
)

register_custom_property(_builder_uid, "bg_color", "colorentry")
register_custom_property(_builder_uid, "fg_color", "colorentry")
register_custom_property(_builder_uid, "border_color", "colorentry")
register_custom_property(_builder_uid, "border_width", "entry")
register_custom_property(_builder_uid, "text", "text")
register_custom_property(_builder_uid, "text_font", "fontentry")
register_custom_property(_builder_uid, "text_color", "colorentry")
register_custom_property(_builder_uid, "text_color_disabled", "colorentry")
register_custom_property(_builder_uid, "checkmark_color", "colorentry")
register_custom_property(_builder_uid, "width", "dimensionentry")
register_custom_property(_builder_uid, "height", "dimensionentry")
register_custom_property(_builder_uid, "corner_radius", "entry")
register_custom_property(_builder_uid, "command", "simplecommandentry")
register_custom_property(
    _builder_uid,
    "hover",
    "choice",
    values=("", "True", "False"),
    state="readonly",
)
register_custom_property(_builder_uid, "hover_color", "colorentry")


class CTkSwitchBO(CTkBaseMixin, BuilderObject):
    class_ = CTkSwitch
    allow_bindings = False
    OPTIONS_STANDARD = ("textvariable",)
    OPTIONS_SPECIFIC = (
        "command",
        "variable",
        "variable",
        "onvalue",
        "offvalue",
        "state",
        "width",
        "height",
    )
    OPTIONS_CUSTOM = (
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "checkmark_color",
        "text",
        "text_font",
        "text_color",
        "text_color_disabled",
        "corner_radius",
        "hover",
        "hover_color",
        "progress_color",
        "button_color",
        "button_hover_color",
        "button_length",
    )
    properties = OPTIONS_STANDARD + OPTIONS_SPECIFIC + OPTIONS_CUSTOM
    command_properties = ("command",)
    ro_properties = ("hover", "text_color", "text_color_disabled")


_builder_uid = f"{_plugin_uid}.CTkSwitch"
register_widget(
    _builder_uid,
    CTkSwitchBO,
    "CTkSwitch",
    ("ttk", _designer_tab_label),
    group=1,
)

register_custom_property(_builder_uid, "bg_color", "colorentry")
register_custom_property(_builder_uid, "fg_color", "colorentry")
register_custom_property(_builder_uid, "border_color", "colorentry")
register_custom_property(_builder_uid, "border_width", "entry")
register_custom_property(_builder_uid, "text", "text")
register_custom_property(_builder_uid, "text_font", "fontentry")
register_custom_property(_builder_uid, "text_color", "colorentry")
register_custom_property(_builder_uid, "text_color_disabled", "colorentry")
register_custom_property(_builder_uid, "checkmark_color", "colorentry")
register_custom_property(_builder_uid, "width", "dimensionentry")
register_custom_property(_builder_uid, "height", "dimensionentry")
register_custom_property(_builder_uid, "corner_radius", "entry")
register_custom_property(_builder_uid, "command", "simplecommandentry")
register_custom_property(
    _builder_uid,
    "hover",
    "choice",
    values=("", "True", "False"),
    state="readonly",
)
register_custom_property(_builder_uid, "hover_color", "colorentry")
register_custom_property(_builder_uid, "progress_color", "colorentry")
register_custom_property(_builder_uid, "button_color", "colorentry")
register_custom_property(_builder_uid, "button_hover_color", "colorentry")
register_custom_property(_builder_uid, "button_length", "colorentry")
