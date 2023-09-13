package game.actions;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.items.Item;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.Location;
import edu.monash.fit2099.engine.weapons.WeaponItem;
import game.Status;
import game.actors.Enemy;
import game.actors.Invader;
import game.actors.Player;

import java.util.ArrayList;
import java.util.List;

/**
 * An action executed if an actor is killed.
 * Created by: FIT2099 Team
 * @author Adrian Kristanto
 *
 * Modified by: Shosuke Asano and Ashi Dhandia
 */
public class DeathAction extends Action {

    /**
     * The actor that execute death action
     */
    private Actor attacker;

    /**
     * Constructor for DeathAction
     *
     * @param actor The actor that executes death action
     */
    public DeathAction(Actor actor) {
        this.attacker = actor;
    }

    /**
     * When the enemy is killed by player, the dropped runes is added to the player.
     * When the Player is killed by the enemy, the runes is dropped to the location in the game map.
     *
     * @param target the actor performing the action
     * @param map the map the actor is on
     * @return string result of the action to be displayed on the UI
     */
    @Override
    public String execute(Actor target, GameMap map) {
        String result = "";
        ActionList dropActions = new ActionList();

        // when the attacker is enemy and the target is player
        if (target.hasCapability(Status.HOSTILE_TO_ENEMY)) {
            Player player = (Player)target;
            for (Item item : target.getItemInventory())
                dropActions.add(item.getDropAction(target));
            for (Action drop : dropActions)
                drop.execute(target, map);
            System.out.println(player.getCurrentRunes() + " runes dropped.");
            System.out.println("YOU DIED!");

            // if the player dies, remove all invaders and allies from map
            for (int x = 0; x < map.getXRange().max(); x++) {
                for (int y = 0; y < map.getYRange().max(); y++) {
                    Location location = map.at(x, y);
                    if (location.containsAnActor() && location.getActor() != null) {
                        Actor actorOnMap = location.getActor();
                        if (actorOnMap.hasCapability(Status.INVADER) | actorOnMap.hasCapability(Status.ALLY)) {
                            map.removeActor(actorOnMap);
                        }
                    }
                }
            }

        } else if (target.hasCapability(Status.ALLY) & !this.attacker.hasCapability(Status.HOSTILE_TO_ENEMY)) {
            for (WeaponItem weapon : target.getWeaponInventory())
                dropActions.add(weapon.getDropAction(target));
        }
//        // if the target is LAND type, pile of bones action should occur
//        else if (target.hasCapability(Status.LAND)) {
//            // * yet to implement
//        }

        // when the attacker is a player and the target is invader
        else if (this.attacker.hasCapability(Status.HOSTILE_TO_ENEMY) & target.hasCapability(Status.INVADER)) {
            for (WeaponItem weapon : target.getWeaponInventory())
                dropActions.add(weapon.getDropAction(target));
            Player player = (Player)this.attacker;
            Invader invader = (Invader)target;
            int runesGranted = invader.runesCalculated();
            player.pickUpRunes(runesGranted);
            player.showCurrentRunesMessage();
        }

        // when the attacker is a player and the target is enemy
        else if (this.attacker.hasCapability(Status.HOSTILE_TO_ENEMY)) {
            for (WeaponItem weapon : target.getWeaponInventory())
                dropActions.add(weapon.getDropAction(target));
            for (Action drop : dropActions)
                drop.execute(target, map);

            Player player = (Player)this.attacker;
            Enemy enemy = (Enemy)target;
            int droppedRunes = enemy.droppedRunes();
            player.showDroppedRunesMessage(droppedRunes);
            player.pickUpRunes(droppedRunes);
            player.showCurrentRunesMessage();
        }

        map.removeActor(target);
        result += System.lineSeparator() + menuDescription(target);
        return result;
    }

    /**
     * Describes which target is killed
     *
     * @param actor the actor performing the action
     * @return a string description used for the menu UI
     */
    @Override
    public String menuDescription(Actor actor) {
        return actor + " is killed.";
    }
}
