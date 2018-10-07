import tornado.httpclient
import tornado.escape
import re

async def fetch_bootstrap():
    client = tornado.httpclient.AsyncHTTPClient()
    try:
        response = await client.fetch("http://world5.runescape.com/html5/comapp/Bootstrap.js")
    except:
        return await fetch_bootstrap()
    return tornado.escape.to_unicode(response.body)

async def fetch_parameters():
    client = tornado.httpclient.AsyncHTTPClient()
    try:
        response = await client.fetch("http://secure.runescape.com/m=world5/html5/comapp/")
    except:
        return await fetch_parameters()
    match = re.search(r"clientParametersObfuscated={([^}]+)", tornado.escape.to_unicode(response.body))
    return "window.clientParametersObfuscated={" + re.sub(r"\s", "", match.group(1)) + "};"

def read_object(text):
        # Find the matching bracket and until semicolon
        score = 0
        for i, c in enumerate(text):
            if c in ["{","}"]:
                score += ["{","}"].index(c)*2 - 1
            if not score:
                return i + text[i:].find(";") + 1
        return len(text)

def valid(removed, variable):
        # Assert that our latest object is not invalid
        blacklist = ["controller", "directive", "factory", "config", "module", "filter"]
        if any(string in variable['data'] for string in blacklist):
            return False
        # Check if the found variable is a shell-function for a blacklisted one
        if re.search(r"\.(?:" + "|".join(blacklist) + ")", variable['content']):
            return False

        for obj in removed:
            if re.search("=" + obj['name'] + "[;}]", variable['content']):
                return False

        return True

def next_object(text):
        # Find next object definition
        match = re.search(r"var ([^=,]+)(=[^;{]*)\{", text)
        if not match:
            return "", {}
        # Since we have to include { in the pattern we must subtract one
        start = match.end(0) - 1
        end = start + read_object(text[start:])
        variable = {
            "name": match.group(1),
            "data": match.group(2),
            "content": text[start:end]
        }
        return text[end:], variable

async def bootstrap(patterns):
    text = await fetch_bootstrap()
    variables = []
    removed = []
    while True:
        text, variable = next_object(text)
        if not valid(removed, variable):
            removed.append(variable)
        else:
            variables.append(variable)
        if not text:
            break

    # Restore the last variable
    variables.append(removed[-1])
    # We only need the 3rd line of the last variable
    # Silly python format escape complicates "{_str_}()"
    variables[-1]['content'] = "{{{}}}()".format(variables[-1]['content'].split(";")[2])

    custom = await fetch_parameters()
    for variable in variables:
        custom += "var {}{}{}".format(variable['name'], variable['data'], variable['content'])
        # Check if we are trying to match the content of this variable
        for key, pattern in patterns.items():
            if re.search(pattern, variable['content']):
                custom += "window.{}={};".format(key, variable['name'])
                del patterns[key]
                break
    return custom
