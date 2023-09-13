package game.actors;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actions.ActionList;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.items.PickUpItemAction;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.displays.Menu;
import edu.monash.fit2099.engine.positions.Ground;
import edu.monash.fit2099.engine.positions.Location;
import edu.monash.fit2099.engine.weapons.IntrinsicWeapon;
import game.*;
import game.classes.*;
import game.grounds.Cliff;
import game.items.FlaskOfCrimsonTears;
import game.reset.Resettable;
import game.runes.Runes;

import java.util.Scanner;


/**
 * Class representing the Player. It implements the Resettable interface.
 * Allows player to choose role, equipping the player with its respective weapon and HP.
 * Created by: FIT2099 Team
 * @author Adrian Kristanto
 *
 * Modified by: Ashi Dhandia, Shosuke Asano, Seah Thern Fong
 */
public class Player extends Actor implements Resettable {

	/**
	 * menu for player
	 */
	private final Menu menu = new Menu();
	/**
	 * runes for player
	 */
	Runes runes = new Runes(this);

	/**
	 * pick up action for player
	 */
	private PickUpItemAction pickUpItemAction = new PickUpItemAction(runes);


	/**
	 * Constructor for player
	 */
	public Player(CombatArchetypes combatArchetypes) {
		super("Tarnished", '@', combatArchetypes.getStartingHP());
		this.addCapability(Status.HOSTILE_TO_ENEMY);
		this.addWeaponToInventory(combatArchetypes.getStartingWeapon());
		this.addItemToInventory(new FlaskOfCrimsonTears());
		this.addItemToInventory(new Runes(this));
	}

	/**
	 * At each turn, select a valid action to perform and show the menu to users.
	 *
	 * @param actions    collection of possible Actions for this Actor
	 * @param lastAction The Action this Actor took last turn. Can do interesting things in conjunction with Action.getNextAction()
	 * @param map        the map containing the Actor
	 * @param display    the I/O object to which messages may be written
	 * @return the valid action that can be performed in that iteration or null if no valid action is found
	 */
	@Override
	public Action playTurn(ActionList actions, Action lastAction, GameMap map, Display display) {
		// handle multi-turn actions
		if (map.locationOf(this).getDisplayChar() == '$') {
			pickUpItemAction.execute(this, map);
		}
		// calls boolean method to check if player is at cliff, if true, hurt player's max hp
		Location playerLocation = map.locationOf(this);

		if (isPlayerAtCliff(playerLocation)) {
			hurt(getMaxHp());
			map.removeActor(this);
			map.addActor(this, map.at(36,10));
			runes.droppedRunes(this.getCurrentRunes());
		}

		System.out.println(this.printHp() + "hp, " + this.showCurrentRunesMessage());
		if (lastAction.getNextAction() != null)
			return lastAction.getNextAction();

		// return/print the console menu
		return menu.showMenu(this, actions, display);
	}

	/**
	 * checks whether player is at cliff
	 * @param location the location of the cliff
	 * @return boolean if the player is on cliff, true.
	 */
	public boolean isPlayerAtCliff(Location location) {
		boolean isTrue = false;
		Ground ground = location.getGround();
		if (ground instanceof Cliff){
			isTrue = true;
		}
		return isTrue;
	}

	/**
	 * Return intrinsic weapon for player
	 *
	 * @return intrinsic weapon for player
	 */
	public IntrinsicWeapon getIntrinsicWeapon() {
		return new IntrinsicWeapon(11, "punch", 100);
	}

	/**
	 * Updates the runes based on the dropped runes
	 *
	 * @param droppedRunes the number of dropped runes
	 */
	public void pickUpRunes(int droppedRunes) {
		runes.pickUpRunes(droppedRunes);
	}

	/**
	 * Returns the dropped runes message
	 *
	 * @param num the dropped runes
	 * @return message for the dropped runes
	 */
	public String showDroppedRunesMessage(int num){
		return runes.droppedRunes(num);
	}

	/**
	 * Returns current number of runes and shows the message
	 *
	 * @return message of current runes
	 */
	public String showCurrentRunesMessage(){
		return runes.currentRunes();
	}

	/**
	 * Returns current number of runes
	 *
	 * @return number of runes
	 */
	public int getCurrentRunes(){
		return runes.getRunes();
	}

	/**
	 * Updates the runes based on the runes that is used
	 *
	 * @param rune the runes that is used
	 */
	public void useRunes(int rune){
		runes.useRunes(rune);
	}

	/**
	 * Allows the user to choose their starting class in the game
	 *
	 * @return the chosen CombatArchetypes object
	 */
	public static CombatArchetypes chooseStartingClass() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Select your role:");
		System.out.println("a: Astrologer");
		System.out.println("b: Bandit");
		System.out.println("s: Samurai");
		System.out.println("w: Wretch");
		String archetype = scanner.next();

		CombatArchetypes combatArchetype = null;
		switch (archetype) {
			case "a" -> combatArchetype = new Astrologer();
			case "b" -> combatArchetype = new Bandit();
			case "s" -> combatArchetype = new Samurai();
			case "w" -> combatArchetype = new Wretch();
			default -> {
				System.out.println("Invalid choice!");
				chooseStartingClass();
			}
		}
		return combatArchetype;
	}

	/**
	 * Resets the player's hit points to its maximum value
	 */
	public void reset() {
		this.heal(this.getMaxHp() - this.hitPoints);
	}
}
