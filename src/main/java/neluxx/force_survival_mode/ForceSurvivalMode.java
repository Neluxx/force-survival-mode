package neluxx.force_survival_mode;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.resource.ResourceManagerHelper;
import net.fabricmc.fabric.api.resource.ResourcePackActivationType;
import net.fabricmc.loader.api.FabricLoader;
import net.minecraft.util.Identifier;

public class ForceSurvivalMode implements ModInitializer {
	public static final String MOD_ID = "force-survival-mode";

	@Override
	public void onInitialize() {
        // Register the datapack
        ResourceManagerHelper.registerBuiltinResourcePack(
                Identifier.of(MOD_ID, "datapack"),
                FabricLoader.getInstance().getModContainer(MOD_ID).orElseThrow(),
                ResourcePackActivationType.ALWAYS_ENABLED
        );
	}
}