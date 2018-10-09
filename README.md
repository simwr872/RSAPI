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
Note that what is uploaded to GitHub is the core of RSAPI. This includes the deobfuscator, function mapping and patterns for some features bundled into a concept to provide it as a web-service. This is far from all RSAPI is capable of, see section [expanding](https://github.com/simwr872/RSAPI#expanding) for more information.

1. Start the server `python server.py`.
2. Open `docs/comapp.html` in a browser. _(Use FireFox. Chrome is too secure...)_
3. Open the FireFox console and login with a RuneScape account `login("<email>", "<passwd>")`. _(Authenticator? Edit [`docs/comapp.js:124`](https://github.com/simwr872/RSAPI/blob/master/rsapi/docs/comapp.js#L124), 3rd parameter is the authenticator code)_.

If you now login with a different account on RuneScape you should see the RSAPI account sitting in lobby. Messaging the RSAPI account should give you the exact same message back. You can also message anyone from the RSAPI account by visiting [http://localhost/msg?name=NAME&message=MESSAGE](#).

## Expanding
I recommend using the official Companion App in Google Chrome and using the breakpoints function. The file you are looking for is `Bootstrap.js`. Jagex decided to on every update change _(almost)_ every function- and variable-name aswell as the order of the code. However, the code is separated into major objects in which their internal structure does not change. What RSAPI does is find a pattern in this parent object and simply create a global variabe to point there. The user then only needs to know in what spot the desired function comes. See [`docs/comapp.js:111`](https://github.com/simwr872/RSAPI/blob/master/rsapi/docs/comapp.js#L111) for examples of function name remapping.

To add your own functions, write a pattern that matches a child function inside a parent function regardless of variables names (to withstand updates). Add this pattern in `server.py` and add a function name map inside `docs/comapp.js`.

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
* World tracker. _(Build a database of users world preferences?)_
* Reliable name tracker. _(Adding a friend reveals their last name)_

## Unfortunate news
![Mod Lyon news 1](https://i.gyazo.com/e899cd54ab3dfc339e294340607b694d.png)
![Mod Lyon news 1](https://i.gyazo.com/ef1a0a39368a44cebd2a6db75b625158.png)
![Mod Lyon news 1](https://i.gyazo.com/1365377d6bc925ea5e750b2406458fb9.png)
