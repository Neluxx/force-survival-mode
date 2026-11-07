from beet import Context, Function, FunctionTag

from datapack_utils import Targets

FUNCTION_ID = "no_creative_mode:trigger"
COMMANDS = ["gamemode survival @a"]


def beet_default(ctx: Context):
    for target in ctx.inject(Targets):
        target.pack[Function][FUNCTION_ID] = Function(COMMANDS)
        target.pack["minecraft:tick"] = FunctionTag({"values": [FUNCTION_ID]})