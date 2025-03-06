# No Single-Player Cheats
This datapack ensures that players cannot switch to Creative mode or use OP commands, even if they open a Singleplayer world to LAN with cheats enabled.

---

# Features
- Forces all players into Survival mode (/gamemode survival @a)
- Automatically removes OP permissions (/deop @a)
- Runs continuously like a repeating command block
- Works in Singleplayer & Multiplayer (LAN / Servers)
- Lightweight & efficient – no lag!

---

# Installation
- Download the NoCheat.zip file.
- Move it into your world’s datapacks folder: ``.minecraft/saves/YOUR_WORLD/datapacks/``
- Start your world & type: ``/reload``
- (Optional) Verify it’s active: ``/datapack list``

--- 

# How It Works
- The datapack uses tick.json to run 20 times per second (just like a repeating command block).
- It constantly checks and reverts any attempt to change game mode or gain OP permissions.
- Even if you enable cheats in a LAN world, you will always stay in Survival mode.

---

# Uninstalling

To remove the datapack:

- Run: ``/datapack disable "file:nocheat"``
- Delete the NoCheat folder inside your datapacks directory.
- Restart the world.
