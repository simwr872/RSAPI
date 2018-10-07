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
