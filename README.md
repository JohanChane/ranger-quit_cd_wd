# Quit ranger then cd working directory

## Description

Sometime you need to open a terminal on ranger working directory to do some jobs. Ranger provides `S` shortcut to do this, but I don't like this. And the `quit` command in ranger doesn't keep the working directory in ranger. So I make this plugin. I can also jump to my bookmarks (paths) in ranger quickly.

## Installation

1.  Copy `quit_cd_wd.py` to `${XDG_CONFIG_HOME}/ranger/plugins`.

    ```sh
    curl -fLo ${XDG_CONFIG_HOME:-~/.config}/ranger/plugins/quit_cd_wd.py --create-dirs \
            https://raw.githubusercontent.com/JohanChane/ranger-quit_cd_wd/main/quit_cd_wd.py
    ```

2.  [optional] Add the following mapping to the `rc.conf`

    ```
    # Equivalent to `map X quitall_cd_wd ~/.cache/ranger/quit_cd_wd`
    map     X quitall_cd_wd
    # OR customize the path
    map     X quitall_cd_wd <file_saved_wd>
    ```

3.  Add the following to your shell rcfile (e.g. `.bashrc, .zshrc`)

    ```sh
    function ranger {
      local quit_cd_wd_file="$HOME/.cache/ranger/quit_cd_wd"        # The path must be the same as <file_saved_wd> in map.
      #command ranger "$@"              # If you have already added the map to rc.conf
      # OR add `map X quitall_cd_wd ...` if you don't want to add the map in rc.conf
      command ranger --cmd="map X quitall_cd_wd $quit_cd_wd_file" "$@"
      if [ -s "$quit_cd_wd_file" ]; then
        cd "$(cat $quit_cd_wd_file)"
        true > "$quit_cd_wd_file"
      fi
    }
    ```
