import pathlib as _pl
import configparser as _cp

settings = """
[twilio]
account_sid = xyz
auth_token = xyz

"""

def generate_config(p2sf):
    if not p2sf.parent.is_dir():
        p2sf.parent.mkdir()
    with open(p2sf, 'w') as raus:
        raus.write(settings)

def load_config():
    p2sf = _pl.Path.home().joinpath('.recreationdotgov/config.ini')

    if not p2sf.is_file():
        generate_config(p2sf)

    config = _cp.ConfigParser()
    config.read(p2sf)
    return config