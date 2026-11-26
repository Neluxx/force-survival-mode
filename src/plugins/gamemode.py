from beet import Context, Function, FunctionTag

from beet_datapack_utils import versioned_packs

FUNCTION_ID = "no_creative_mode:trigger"
COMMANDS = ["gamemode survival @a"]


def beet_default(ctx: Context):
    for pack in versioned_packs(ctx):
        pack.data[Function][FUNCTION_ID] = Function(COMMANDS)
        pack.data["minecraft:tick"] = FunctionTag({"values": [FUNCTION_ID]})