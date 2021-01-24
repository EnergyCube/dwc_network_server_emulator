"""DWC Network Server Emulator

    Copyright (C) 2014 SMTDDR
    Copyright (C) 2014 kyle95wm
    Copyright (C) 2014 AdmiralCurtiss
    Copyright (C) 2015 Sepalani
    Copyright (C) 2020 EnergyCube

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Configuration module.
"""

try:
    # Python 2
    import ConfigParser
except ImportError:
    # Python 3 PEP8 guidelines (all lowercase for module names)
    import configparser as ConfigParser
import other.utils as utils
import os

# For some unknown reason, we need to specify the absolute location of the file,
# otherwise it will be impossible to read the file sometimes.
def get_config_filename(filename='altwfc.cfg'):
    """Return the config filename that will be used."""
    try:
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        thisfolder = os.path.dirname(os.path.abspath(__file__))
        initfile = os.path.join(thisfolder, filename)
        config.read(initfile)
        if config.getboolean('Config', 'AlternativeConfig'):
            initfile = os.path.join(thisfolder,
                config.get('Config', 'AlternativeConfigFile'))
            config.read(initfile)
            return initfile
        else:
            return initfile
    except Exception:
        pass
    return filename

def get_ip_port(section, filename='altwfc.cfg'):
    """Return a tuple (IP, Port) of the corresponding section."""
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(get_config_filename(filename))
    return (config.get(section, 'IP'), config.getint(section, 'Port'))

def get_ip(section, filename='altwfc.cfg'):
    """Return the IP of the corresponding section."""
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(get_config_filename(filename))
    return config.get(section, 'IP')

def get_port(section, filename='altwfc.cfg'):
    """Return the port of the corresponding section."""
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(get_config_filename(filename))
    return config.getint(section, 'Port')

def get_logger(section, filename='altwfc.cfg'):
    """Return the logger of the corresponding section."""
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(get_config_filename(filename))
    return utils.create_logger(
        config.get(section, 'LoggerName'),
        config.get(section, 'LoggerFilename'),
        config.getint(section, 'LoggerLevel'),
        config.getboolean(section, 'LoggerOutputConsole'),
        config.getboolean(section, 'LoggerOutputFile')
    )

def get_svchost(section, filename='altwfc.cfg'):
    """Return the svchost of the corresponding section."""
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(get_config_filename(filename))
    return config.get(section, 'SvcHost')

def get_server_name(filename='altwfc.cfg'):
    """Return the server name set in the Settings section"""
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(get_config_filename(filename))
    return config.get("Settings", 'ServerName')

def get_manual_activation(filename='altwfc.cfg'):
    """Return if ManualConsoleActivation is enable in Settings"""
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(get_config_filename(filename))
    return config.getboolean("Settings", 'ManualConsoleActivation')

def get_auto_console_activation(filename='altwfc.cfg'):
    """Return if AutoConsoleActivation is enable in Settings"""
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(get_config_filename(filename))
    return config.getboolean("Settings", 'AutoConsoleActivation')

def get_unregister_on_ban(filename='altwfc.cfg'):
    """Return if UnRegisterOnBan is enable in Settings"""
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(get_config_filename(filename))
    return config.getboolean("Settings", 'UnRegisterOnBan')

def get_server_ban_overwrite_game_ban(filename='altwfc.cfg'):
    """Return if ServerBanOverwriteGameBan is enable in Settings"""
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(get_config_filename(filename))
    return config.getboolean("Settings", 'ServerBanOverwriteGameBan')