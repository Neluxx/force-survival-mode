from beet import Context, Function, FunctionTag

from src.plugins.utils import iterate_versions

FUNCTION_ID = "no_creative_mode:trigger"
COMMANDS = ["gamemode survival @a"]


def beet_default(ctx: Context):
    for pack, version in iterate_versions(ctx):
        pack[Function][FUNCTION_ID] = Function(COMMANDS)
        pack["minecraft:tick"] = FunctionTag({"values": [FUNCTION_ID]})
