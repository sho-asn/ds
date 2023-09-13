package game;

import java.util.Arrays;
import java.util.List;

import edu.monash.fit2099.engine.displays.Display;
import edu.monash.fit2099.engine.positions.FancyGroundFactory;
import edu.monash.fit2099.engine.positions.GameMap;
import edu.monash.fit2099.engine.positions.World;
import game.actors.Player;
import game.actors.trader.FingerReaderEnia;
import game.actors.trader.Trader;
import game.grounds.*;
import game.items.FlaskOfCrimsonTears;
import game.items.GoldenRunes;
import game.items.RemembranceOfTheGrafted;
import game.reset.ResetManager;

/**
 * The main class to start the game.
 * Created by: FIT2099 Team
 * @author Adrian Kristanto
 *
 * Modified by: Ashi Dhandia and Seah Thern Fong
 */
public class Application {

	public static void main(String[] args) {

		World world = new World(new Display());

		FancyGroundFactory groundFactory = new FancyGroundFactory(new Dirt(), new Wall(), new Floor(), new Graveyard(),
				new GustOfWind(), new PuddleOfWater(), new SiteOfLostGrace(), new Cliff(), new Cage(), new Barrack(),
				new Lava(), new SummonSign());

		List<String> Limgrave = Arrays.asList(
				"......................#.............#..........................+++.........",
				"......................#.............#.......................+++++..........",
				"......................#..___....____#.........................+++++........",
				"......................#...........__#............................++........",
				"......................#_____........#.............................+++......",
				"......................#............_#..............................+++.....",
				"......................######...######......................................",
				"...........................................................................",
				"...........................=...............................................",
				"........++++......................###___###................................",
				"........+++++++...................________#................................",
				"..........+++.....................#________................................",
				"............+++...................#_______#................................",
				".............+....................###___###................................",
				"............++......................#___#..................................",
				"..............+...................=........................................",
				"..............++.................................................=.........",
				"..............................................++...........................",
				"..................++++......................+++...............######..##...",
				"#####___######....++...........................+++............#....____....",
				"_____________#.....++++..........................+..............__.....#...",
				"_____________#.....+....++........................++.........._.....__.#...",
				"_____________#.........+..+.....................+++...........###..__###...",
				"_____________#.............++..............................................");

		GameMap gameMap1 = new GameMap(groundFactory, Limgrave);
		world.addGameMap(gameMap1);

		List<String> Stormveil_Castle = Arrays.asList(
				"...........................................................................",
				".m................<...............<.................................m......",
				"...........................................................................",
				"##############################################...##########################",
				"............................#................#.......B..............B......",
				".....B...............B......#................#.............................",
				"...............................<.........<.................................",
				".....B...............B......#................#.......B..............B......",
				"............................#................#.............................",
				"#####################..#############...############.####..#########...#####",
				"...............#++++++++++++#................#++++++++++++#................",
				"...............#++++++++++++...<.........<...#++++++++++++#................",
				"...............#++++++++++++..................++++++++++++#................",
				"...............#++++++++++++#................#++++++++++++#................",
				"#####...##########.....#############...#############..#############...#####",
				".._______........................B......B........................B.....B...",
				"_____..._..____....&&........<..............<.......................m......",
				".........____......&&......................................................",
				".m.._______..................<..............<....................<.....<...",
				"#####....##...###..#####...##########___###############......##.....####...",
				"+++++++++++++++++++++++++++#...................#+++++++++++++++++++++++++++",
				"+++++++++++++++++++++++++++....................#+++++++++++++++++++++++++++",
				"+++++++++++++++++++++++++++#....................+++++++++++++++++++++++++++",
				"+++++++++++++++++++++++++++#...................#+++++++++++++++++++++++++++");

		GameMap gameMap2 = new GameMap(groundFactory, Stormveil_Castle);
		world.addGameMap(gameMap2);

		List<String> Roundtable_Hold = Arrays.asList(
				"##################",
				"#________________#",
				"#________________#",
				"#________________#",
				"#________________#",
				"#________________#",
				"#________________#",
				"#________________#",
				"#________________#",
				"#________________#",
				"########___#######");
		GameMap gameMap3 = new GameMap(groundFactory, Roundtable_Hold);
		world.addGameMap(gameMap3);

		List<String> Boss_Room = Arrays.asList(
				"+++++++++++++++++++++++++",
				".........................",
				".._......................",
				".........................",
				".........................",
				".........................",
				".........................",
				".........................",
				"+++++++++++++++++++++++++");

		GameMap gameMap4 = new GameMap(groundFactory, Boss_Room);
		world.addGameMap(gameMap4);

		GoldenFogDoor goldenFogDoor1 = new GoldenFogDoor(gameMap1);
		GoldenFogDoor goldenFogDoor2 = new GoldenFogDoor(gameMap2);
		GoldenFogDoor goldenFogDoor3 = new GoldenFogDoor(gameMap3);
		GoldenFogDoor goldenFogDoor4 = new GoldenFogDoor(gameMap4);

		gameMap1.at(39, 16).setGround(goldenFogDoor2);
		gameMap1.at(14, 7).setGround(goldenFogDoor3);

		gameMap2.at(68, 12).setGround(goldenFogDoor1);
		gameMap2.at(6, 6).setGround(goldenFogDoor4);

		gameMap3.at(4, 4).setGround(goldenFogDoor1);

		// BEHOLD, ELDEN RING
		for (String line : FancyMessage.ELDEN_RING.split("\n")) {
			new Display().println(line);
			try {
				Thread.sleep(200);
			} catch (Exception exception) {
				exception.printStackTrace();
			}
		}

//		gameMap.at(23, 17).addActor(new LoneWolf());

		// create instance of player and allow it to choose its role
		Player player = new Player(Player.chooseStartingClass());

		// Create a new ResetManager instance
		ResetManager resetManager = ResetManager.getInstance();
		resetManager.registerResettable(player);
		resetManager.registerResettable(new FlaskOfCrimsonTears());

		world.addPlayer(player, gameMap1.at(36, 10));

		Trader trader = new Trader();
		gameMap1.at(40, 12).addActor(trader);

		FingerReaderEnia fingerReaderEnia = new FingerReaderEnia();
		gameMap1.at(40, 11).addActor(fingerReaderEnia);


		GoldenRunes goldenRunes = new GoldenRunes();
		RemembranceOfTheGrafted remembranceOfTheGrafted = new RemembranceOfTheGrafted();
		gameMap1.at(30, 10).addItem(goldenRunes);
		gameMap1.at(30, 11).addItem(remembranceOfTheGrafted);


		world.run();
	}
}

