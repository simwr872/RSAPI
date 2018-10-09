class Service {
    /**
     * Creates a service object from an existing variable with a list of
     * function names. Names are used to remap function names but provide
     * the same functionality as the original object.
     * @param {*} object - Defined variable
     * @param {Array.<string>} names - Name map
     */
    constructor(object, names) {
        this.object = object;
        this.names = names;
    }

    /**
     * Retrieves a variable from the object.
     * @param {string} name - Variable to get
     * @returns {*} Variable from object
     */
    get(name) {
        let index = this.names.indexOf(name);
        let key = Object.keys(this.object)[index];
        return this.object[key];
    }

    /**
     * Sets a variable to a new value.
     * @param {string} name Name of variable to set
     * @param {*} value New value
     */
    set(name, value) {
        let index = this.names.indexOf(name);
        let key = Object.keys(this.object)[index];
        this.object[key] = value;
    }
}

class Player {
    /**
     * Creates a new player object. A player object exists to make interaction
     * easier with the player.
     * @param {string} name Player name
     */
    constructor(name) {
        this.name = name.toLowerCase();
    }

    /**
     * Returns true if player is on our friendslist.
     * @returns {boolean} True if on friendslist
     */
    isFriend() {
        return user.get("isFriend")(this.name);
    }

    /**
     * Asynchronous.
     * Adds the player to our friendslist.
     *
     * Note that spooky stuff happens if you access friendlist too
     * fast. Friends seem to still be on the friendslist after
     * a successful removal.
     */
    addFriend() {
        return new Promise((resolve, reject) => {
            user.get("addFriend")(this.name, data => {
                if (!data[Object.keys(data)[0]]) resolve(data);
                reject(data);
            });
        });
    }

    /**
     * Retrieves the ID for this player on our friendslist. Used when removing
     * a friend.
     * @returns {number} Friendlist ID
     */
    id() {
        for(var i = 0; i < user.get("friendCount")(); i++) {
            if (user.get("friend")(i).displayName.toLowerCase() == name) return i;
        }
    }

    /**
     * Asynchronous.
     * Removes the player to from friendslist. Bugged(?)
     */
    removeFriend() {
        return new Promise((resolve, reject) => {
            user.get("removeFriend")(this.id(), data => {
                resolve(data);
            });
        });
    }

    /**
     * Asynchronous.
     * Messages the player.
     * @param {string} text Text to send
     */
    message(text) {
        return new Promise((resolve, reject) => {
            authentication.get("message")(this.name, text, data => {
                if (!data[Object.keys(data)[0]]) resolve(data);
                reject(data);
            });
        });
    }
}


let authentication = new Service(window.authentication, [".","login",".","online","loginCallback","logout","logoutCallback",".","username",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","message","messageCallback",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]);
let user = new Service(window.user,[".","friend","addFriend","removeFriend","friendCount",".",".","isFriend",".",".",".",".",".",".",".",".",".","isIgnored",".","."]);
let message = new Service(window.message,[".",".",".","PM_IN",".","ONLINE","PM_OUT",".","FC_IN_OUT","FC_KICK",".",".",".",".",".",".",".",".",".",".",".",".",".",".","CC_OUT",".",".",".",".",".",".",".",".",".",".",]);


let login = function(email, password) {
    return new Promise((resolve, reject) => {
        authentication.set("loginCallback", data => {
            if (data.success) resolve(data);
            reject(data);
        });
        // Callback funciton for logout must also be non-null
        authentication.set("logoutCallback", () => {});
        authentication.get("login")(email, password, "", false);
    });
}

let chat = async function(name, message) {
    let player = new Player(name);
    if (!player.isFriend()) await player.addFriend();
    await player.message(message);
}

authentication.set("messageCallback", function(data) {
    // Decode payload functions
    let payload = new Service(data, [".",".",".","identifier",".",".",".","stranger",".",".","message",".",".",".","."]);
    switch(payload.get("identifier")()) {
        case message.get("ONLINE"):
            break;
        case message.get("PM_IN"):
            chat(payload.get("stranger")(), payload.get("message")());
            break;
        case message.get("PM_OUT"):
            break;
        default:
    }
});

window.warmup = setInterval(() => {
    if (window.ready.ready()) {
        console.log("Bootstrap complete.");
        clearInterval(window.warmup);
    }
}, 50);

let socket = new WebSocket("ws://localhost/ws?auth=3WeAHJVaS0yMfHFI");
socket.onopen = function(event){
    console.log("Websocket connected.");
}

socket.onmessage = async function(event) {
    let data = JSON.parse(event.data);
    let id = data[0];
    let command = data[1];
    let response = "";
    switch(command.split(" ")[0]) {
        case "msg":
            let message = command.split(" ");
            let name = message[1];
            await chat(name, message.splice(2, message.length).join(" "));
            response = "ok";
            break;
        default:
            response = "not reckognized";
            break;
    }
    socket.send(JSON.stringify([id, response]));
}
