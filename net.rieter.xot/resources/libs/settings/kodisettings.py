#===============================================================================
# LICENSE Retrospect-Framework - CC BY-NC-ND
#===============================================================================
# This work is licenced under the Creative Commons
# Attribution-Non-Commercial-No Derivative Works 3.0 Unported License. To view a
# copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/3.0/
# or send a letter to Creative Commons, 171 Second Street, Suite 300,
# San Francisco, California 94105, USA.
#===============================================================================

import settingsstore


class KodiSettings(settingsstore.SettingsStore):
    __settings = None

    def __init__(self, logger):
        super(KodiSettings, self).__init__(logger)

    def set_setting(self, setting_id, setting_value, channel=None):
        pass

    def get_boolean_setting(self, setting_id, channel=None, default=None):
        pass

    def get_integer_setting(self, setting_id, channel=None, default=None):
        pass

    def get_setting(self, setting_id, channel=None, default=None):
        pass

    def clear_settings(self):
        KodiSettings.__settings = None
