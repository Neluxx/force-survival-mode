from beet import Context, Function, FunctionTag

from beet_datapack_utils import versioned_packs

FUNCTION_ID = "force_survival_mode:tick"
COMMANDS = ["gamemode survival @a[gamemode=!survival]"]


def beet_default(ctx: Context) -> None:
    for pack in versioned_packs(ctx):
        pack.data[Function][FUNCTION_ID] = Function(COMMANDS)
        pack.data["minecraft:tick"] = FunctionTag({"values": [FUNCTION_ID]})