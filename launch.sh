#!/bin/sh

check_apt_package() {
	if ! dpkg -s $1 >/dev/null 2>&1; then
		echo $1 not found, installing...
		sudo apt install $1
	else
		echo $1 is already installed
	fi
}

# check_python_package() {
# 	if ! pip show $1 >/dev/null 2>&1; then
# 		echo $1 not found, installing...
# 		pip install $1
# 	fi
# #   else
# #     echo $1 is already installed
# #   fi
# }

echo checking dependencies...

while read package; do
	check_apt_package $package
done < dependencies.txt

echo creating .venv for python...

python -m venv .venv

. .venv/bin/activate

echo virtual environment created.

echo checking python requirements...

# while read package; do
# 	check_python_package $package
# done < requirements.txt
pip install -r requirements.txt

echo dependencies installed.

echo checking for screen...

process_name="discord_bot"
if [ "$TERM" = "screen" ]; then
	echo user is already in a screen.
	echo running the script...
	python main.py
else
	echo creating screen...
	session_number=1
	while screen -list | grep -q "${process_name}_$session_number"; do
	session_number=$((session_number+1))
	done
	echo running the script...
	screen -dmS ${process_name}_$session_number python main.py
fi
