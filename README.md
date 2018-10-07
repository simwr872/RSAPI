## RSAPI
RSAPI uses functions stowed away in the Companion App. The Companion App actually comes with some great functionality but it is hidden behind a terrible application structure with dynamic loading of vital assets and uglified code such as;
```javascript
if(false){}
if(false){}
if(false){}
```
Every week the Companion App gets a new obfuscation done upon it, which in turn makes the functions have different names and be placed upon different locations. Another albeit easier issue is the client parameters are changed on every use. RSAPI not only handles the obfuscation but also strips out non-essential UI code.

## Requirements
Use Python 3.6, install [tornado](https://www.tornadoweb.org/).

    $ pip install tornado

## Using RSAPI
    $ python server.py

## Features
Here are webm's of some features that were recorded in early development.
* [Bank evaluator](https://giant.gfycat.com/FavoriteFabulousEasternglasslizard.webm)
* [Buy and sell items](https://giant.gfycat.com/NimbleGiantDwarfmongoose.webm)
* [Checking item values](https://giant.gfycat.com/NeglectedShamelessDairycow.webm)
  * Note: Capable of checking **every** tradeable item in less than 25 seconds.
* [Chat](https://giant.gfycat.com/DecisiveDismalFinwhale.webm)

RSAPI has endless potential, it can automate anything companion app can do. Examples of possible implementations:
* Todays ____. _(Vis wax, araxxor path, travelling merchant...)_
* Sit in multiple friends chat and PM upon event. _(Ghost peng, portables...)_
* Merchanting bot.
* PM multiple people at the same time. _(Personalized clan notification, raid group notifier...)_
* World tracker. (Build a databse of users world preferences?)
* Reliable name tracker. (Adding a friend reveals their last name)

## Unfortunate news
![Mod Lyon news 1](https://i.gyazo.com/e899cd54ab3dfc339e294340607b694d.png)
![Mod Lyon news 1](https://i.gyazo.com/ef1a0a39368a44cebd2a6db75b625158.png)
![Mod Lyon news 1](https://i.gyazo.com/1365377d6bc925ea5e750b2406458fb9.png)
