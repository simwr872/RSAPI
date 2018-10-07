## RSAPI
RSAPI uses functions stowed away in the Companion App. The Companion App actually comes with some great functionality but it is hidden behind a terrible application structure with dynamic loading of vital assets and uglified code such as;
```javascript
if(false){}
if(false){}
if(false){}
```
Every week the Companion App gets a new obfuscation done upon it. Making the functions have different names and be placed upon different locations. Another albeit easier issue is the client parameters changed upon every use. RSAPI handles everything for you and renames the wanted functions into a more sensible format.

## Requirements
Use Python 3.6, install [tornado](https://www.tornadoweb.org/).
    $ pip install tornado

## Using RSAPI
    $ python server.py
