package game.items;

import edu.monash.fit2099.engine.items.Item;
import game.RandomNumberGenerator;
import game.actions.Consumable;
import game.actions.ConsumeAction;
import game.actors.Player;

/**
 * Golden runes item
 * @author Shosuke Asano
 */
public class GoldenRunes extends Item implements Consumable {
    /***
     * Constructor for golden runes
     */
    public GoldenRunes() {
        super("Golden Runes", '*', true);
        this.addAction(new ConsumeAction(this));
    }

    /**
     * The number of runes will be randomly decided.
     *
     * @param player a player who consume the golden runes
     */
    @Override
    public void consume(Player player) {
        player.removeItemFromInventory(this);
        int randomRunes = RandomNumberGenerator.getRandomInt(200, 10000);
        player.pickUpRunes(randomRunes);
    }

}
