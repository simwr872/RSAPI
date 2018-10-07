def error(code, message):
    return {"error":{"code":code,"message":message}}

def success(data):
    return {"data":data}
