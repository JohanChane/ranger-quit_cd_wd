# Quit ranger then cd working directory

## Description

Sometime you need to open a terminal on ranger working directory to do some jobs. Ranger provides `S` shortcut to do this, but I don't like this. And the `quit` command in ranger doesn't keep the working directory in ranger. So I make this plugin. I can also jump to my bookmarks (paths) in ranger quickly.

## Installation

1.  Copy `quit_cd_wd.py` to `${XDG_CONFIG_HOME}/ranger/plugins`.
2.  Add the following mapping to the `rc.conf`

    ```
    map     x quit_cd_wd
    map     X quitall_cd_wd
    ```
3.  Add the following to your shell rcfile (e.g. `.bashrc, .zshrc`)

    ```sh
    function ranger_func {
        ranger $*
        local quit_cd_wd_file="$HOME/.ranger_quit_cd_wd"
        local quit_cd_wd="$(cat $quit_cd_wd_file)"
        if [ -n $quit_cd_wd ]; then
            cd $quit_cd_wd
            true > $quit_cd_wd_file
        fi
    }

    alias ranger='ranger_func'
    ```
