def print_with_newline(message):
    __info(message)
    print("")

def write_log(message, var_name="") -> None:
    __debug(
        f"{var_name}={message}" if len(var_name) > 0\
        else message)

def __debug(message):
    __write(message, "debug")

def __info(message):
    __write(message, "info")

def __warn(message):
    __write(message, "warn")

def __error(message):
    __write(message, "error")

def __fatal(message):
    __write(message, "fatal")

def __write(message, logtype: str):
    print(f"[{logtype}]{message}")