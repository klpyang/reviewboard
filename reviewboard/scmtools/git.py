from reviewboard.scmtools import sshutils
sshutils.register_rbssh('GIT_SSH')

        if self._is_new_file(linenum):
            linenum += 1
        elif self._is_deleted_file(linenum):
            file_info.deleted = True
    def _is_new_file(self, linenum):
        line = self.lines[linenum]

        return self.lines[linenum].startswith("new file mode")

    def _is_deleted_file(self, linenum):
        return self.lines[linenum].startswith("deleted file mode")
            p = self._run_git(['--git-dir=%s' % self.git_dir, 'config',
                               'core.repositoryformatversion'])
        p = self._run_git(['ls-remote', self.path, 'HEAD'])
    def _run_git(self, args):
        """Runs a git command, returning a subprocess.Popen."""
        return subprocess.Popen(
            ['git'] + args,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            close_fds=(os.name != 'nt')
        )

        p = self._run_git(['--git-dir=%s' % self.git_dir, 'cat-file',
                           option, commit])