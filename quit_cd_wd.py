import os
from ranger.api.commands import Command

class quitall_cd_wd(Command):
    """:chdir to working directory of ranger after quitalling on ranger.

    """
    def _exit_no_work(self):
        if self.fm.loader.has_work():
            self.fm.notify('Not quitting: Tasks in progress: Use `quitall!` to force quit')
        else:
            self.fm.exit()

    def execute(self):
        self.save_wd()
        self._exit_no_work()

    def save_wd(self):
        if len(self.args) > 1:
            wd_file_path=os.path.expanduser(self.arg(1))
        else:
            wd_file_path=os.path.expanduser('~/.cache/ranger/quit_cd_wd')
        wd_dir_path = os.path.dirname(wd_file_path)
        if not os.path.exists(wd_dir_path):
            os.makedirs(wd_dir_path)
        with open(wd_file_path, 'w') as f:
            f.write(self.fm.thisdir.path);
