package game.actions;

import edu.monash.fit2099.engine.actors.Actor;
import game.actors.Player;

/**
 * This is an interface "Consumable", this interface will provide methods for consuming a consumable item
 * @author Seah Thern Fong
 */
public interface Consumable {

    /**
     * This will consume an item
     */
    void consume(Player actor);
}

