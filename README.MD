# Manhunt Compass
Mincraft Spigot plugin that adds compass from Dream's manhunts to track players.
It also contains a hunters and runners team support.

## Instalation
Copy `Manhunt_compass.jar` file from `/out/artifacts` and paste it in `plugins` folder in your server directory.

## Commands
Commands in the plugin require arguments and are grouped by their usage.

### getCompass
Can only be executed by **hutners**. Adds to the inventory _Manhunt Compass_ which is used to track runners. Clicking RMB points compass to the closest **runner**.
- `/getCompass` - gives a manhunt compass

### Manhunt
Command that is resposible for the game. `start` gives every hunter _Manhunt Compass_ and start the game. `stop` ends manhunt game.
- `/manhunt start` - starts manhunt game
- `/mahunt stop` - ends manhunt

### Hunter
Everything realted to **hunters**. Hunters have to kill all runners in order to win the game.
- `/hunter` - add a player executing that command to hunters
- `/hunter add <player>` - add <player> to hunters
- `/hunter remove <player>` - remove <player> from hunters
- `/hunter clear` - remove all hunters
- `/hunter list` - returns nicks of hunters
### Runner
Everything related to **runners**. Runners have to survive and kill ender dragon but you can choose whatever objective you want.
- `/hunter` - add a player executing that command to runners
- `/runner add <player>` - add <player> to runners
- `/runner remove <player>` - remove <player> from runners
- `/runner clear` - remove all players from runners
- `/runner list` - returns nicks of runners

##### In progress
- [ ] Dragon death detection
- [ ] Toggle compass in nether
- [ ] Auto end game when all runners die