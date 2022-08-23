import ranger.api
from ranger.api.commands import *
import os

QUIT_CD_WD_FILE = '$HOME/.ranger_quit_cd_wd'

class quit_cd_wd(Command):
    """:chdir to working directory of ranger after quiting on ranger.

    """
    def _exit_no_work(self):
        if self.fm.loader.has_work():
            self.fm.notify('Not quitting: Tasks in progress: Use `quit!` to force quit')
        else:
            self.fm.exit()

    def execute(self):
        if len(self.fm.tabs) >= 2:
            self.fm.tab_close()
        else:
            os.system('echo $PWD > ' + QUIT_CD_WD_FILE)
            self._exit_no_work()

class quitall_cd_wd(Command):
    """:chdir to working directory of ranger after quitalling on ranger.

    """
    def _exit_no_work(self):
        if self.fm.loader.has_work():
            self.fm.notify('Not quitting: Tasks in progress: Use `quitall!` to force quit')
        else:
            self.fm.exit()

    def execute(self):
        os.system('echo $PWD > ' + QUIT_CD_WD_FILE)
        self._exit_no_work()
