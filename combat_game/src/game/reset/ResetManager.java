package game.reset;

import java.util.ArrayList;
import java.util.List;

/**
 * A reset manager class that manages a list of resettables.
 * Created by: FIT2099 Team
 * @author Adrian Kristanto
 * Modified by: Ashi Dhandia
 *
 */
public class ResetManager {
    private List<Resettable> resettables;
    private static ResetManager instance;

    /**
     * Constructor
     */
    private ResetManager() {
        this.resettables = new ArrayList<>();
    }

    public static ResetManager getInstance() {
        if (instance == null) {
            instance = new ResetManager();
        }
        return instance;
    }

    public void run() {
        for (Resettable resettable : resettables) {
            resettable.reset();
        }
    }

    public void registerResettable(Resettable resettable) {
        resettables.add(resettable);
    }

    public void removeResettable(Resettable resettable) {
        resettables.remove(resettable);
    }
}
