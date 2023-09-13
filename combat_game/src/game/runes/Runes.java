package game.runes;

import edu.monash.fit2099.engine.items.Item;
import game.actors.Player;

/**
 * A class that represents the Runes
 * @author Shosuke Asano
 *
 */
public class Runes extends Item {
    /**
     * numer of runes
     */
    private int runes;
    /**
     * player has runes
     */
    private Player player;

    /***
     * Constructor.
     */
    public Runes(Player player) {
        super("Runes", '$', false);
        this.runes = 0;
        this.player = player;
    }

    /**
     * get the number of runes
     * @return the number of runes
     */
    public int getRunes() {
        return runes;
    }

    /**
     * set the number of runes
     * @param runes the number of runes
     */
    public void setRunes(int runes) {
        this.runes = runes;
    }

    /**
     * Runes is picked up
     * @param runes the number of runes that is picked up
     */
    public void pickUpRunes(int runes) {
        this.setRunes(this.getRunes() + runes);
    }

    /**
     * Runes is used
     * @param runes the number of runes that is used
     */
    public void useRunes(int runes) {
        this.setRunes(this.getRunes() - runes);
    }

    /**
     * Show the message of the current number of runes
     * @return message of the current number of runes
     */
    public String currentRunes() {
        return "Current runes: " + this.getRunes();
    }

    /**
     * Show the message of the current number of runes that is dropped
     * @param runes the number of runes that is dropped
     * @return message of the number of runes that is dropped
     */
    public String droppedRunes(int runes) {
        return runes + " runes is dropped.";
    }
}
