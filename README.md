# Final---Zombies

# Zombies
![Zombies Demo](assets/ZombiesDemo.mp4)

Zombies is a two-player game where the goal is to capture the golden orb that randomly moves around the playing area. When a player touches the orb, it relocates to another random location on the playing area and two "zombies" are spawned. Each player is then pursued by one zombie. The number of zombies in the game increases every time the orb is touched.

Players can defend themselves by shooting and removing the zombies from the game. If any of the zombies touch either player, the game ends, and a messeage appears celebrating the winning player.

## Player Class:
- Will constantly move forward 5 pixels each time the display is updated.
- Will remain within the defined playing area. If the player touches the boundary, it will reflect off the boundary and continue moving forward.
- The user will use key presses to control the player: turn left, turn right, fire bullet.
- A player object will be hidden("die"), when it collides with a Zombie object.
- Extra Credit: Player can drop a "bomb" which kills all zombies within a 100 pixels of the player. The player should draw circle which represent the blast radius.

## Prize Class:
- Will move randomly around the defined playing area. 
- If the player touches the prize:
	- The prize will relocated to a random position in the playing area
    - Two Zombie objects will be instantiated at random locations in the playing area.
    - One Zombie object will follow and attack player 1 while the second Zombie object will attack player 2.
## Zombie Class:
- Objects of the Zombie class will continuously face the player. Using the towards() method.
```python
zombie.setheading((zombie.towards(p1)))
zombie.forward(2)
```
- Zombie objects will continuously move towards the player at 2 to 3 pixels per update.
- A zombie objects will be instantiated (created) every time the player touches the prize.
- A Zombie object  will be destroyed and removed from the list when it is hit by a Bullet object.

## Bullet Class:
- Will originate at the location of the Player object which fired it.
- Each Bullet object will have the heading of the player object.
- Bullet objects will move in straight lines.
- Bullet objects will be destroyed if they collide with a zombie or when they leave the playing area.


## RUBRIC
|**Description**|**Pts**|
|---|---|
|**Player Class**||
|Player moves continuously around the playing area|1|
|User can turn the player left and right|2|
|User can fire a bullet|1|
|*Extra Credit*: Player can drop one bomb during a game. The bomb kills all zombies within a 100 pixel radius of the player.|2|
|**Prize Class**||
|Prize moves randomly around the playing area|1|
|Prize relocates to a random location when touched by a player object|1|
|**Zombie Class**||
|Spawns at random locations on the playing area|1|
|Each zombie will continually pursue a designated player|1|
|**Bullet Class**||
|A bullet will appear at the player which "fires" it|1|
|A bullet will travel in a straigh line until it collides with a zombie or leaves the playing area|1|
|**Game Play**||
|
