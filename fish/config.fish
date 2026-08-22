if status is-interactive
    # Commands to run in interactive sessions can go here
	set -g fish_greeting ""
	alias ls='lsd'
	alias l='ls -l'
	alias la='ls -a'
	alias lla='ls -la'
	alias lt='ls --tree'
	alias cat='bat'
end
