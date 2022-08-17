import libtmux
import random
import string
import typer
from functools import wraps
from rich.prompt import Prompt



def tmux(func_in=None, session_name = None):
    """
    Sends the command to a new tmux window
    """
    def internal(f):
        @wraps(f)
        def wrapper(*args, **kwargs):

            result = f(*args, **kwargs)

            server = libtmux.Server()
            session = server.new_session(session_name = session_name, attach=False)
            window = session.attached_window
            pane = session.attached_pane
            pane.send_keys(result, enter = True)
            server.attach_session(target_session = session_name)

            return result
        return wrapper
    if func_in is None:
        return internal
    else:
        return internal(func_in)


@tmux()
def l2s():
    return('python3 -m venv venv && . ./venv/bin/activate && python3 -m pip install typer')


@tmux()
def ls():
    return('python3 -m venv venv && . ./venv/bin/activate && python3 -m pip install typer')



if __name__=="__main__":
    app()

