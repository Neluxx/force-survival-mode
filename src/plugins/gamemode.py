from beet import Context, DataPack, Function, FunctionTag

FUNCTION_ID = "no_creative_mode:trigger"
COMMANDS = ["gamemode survival @a"]


def beet_default(ctx: Context):
    apply_patch(ctx.data)

    overlay_versions = ctx.meta.get("overlay_versions", {})
    for directory in overlay_versions:
        overlay = ctx.data.overlays[directory]
        apply_patch(overlay)


def apply_patch(pack: DataPack):
    pack[Function][FUNCTION_ID] = Function(COMMANDS)
    pack["minecraft:tick"] = FunctionTag({"values": [FUNCTION_ID]})
