package game.actions;

import edu.monash.fit2099.engine.actions.Action;
import edu.monash.fit2099.engine.actors.Actor;
import edu.monash.fit2099.engine.positions.GameMap;
import game.reset.ResetManager;

public class RestAction extends Action {

    @Override
    public String execute(Actor actor, GameMap map) {
        ResetManager.getInstance().run();
        return actor + " rests and the game is reset.";
    }

    @Override
    public String menuDescription(Actor actor) {
        return actor + " rests at The First Step Lost Site of Grace";
    }
}
