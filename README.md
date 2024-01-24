
# Franco_Bot

Franco_bot is an easy plug and play bot for discord, it is still in development but a lot of functionality are already available.




## Authors

- [@Gabriel](https://github.com/Gabixel)
- [@BananaPilot](https://github.com/BananaPilot)



## Documentation




## Reaquirements

As said Franco_Bot is a plug and play bot so but still it needs a bit of configuration before.

## For Linux

- Having python installed and working on your machine

- Python must run with the command python and not python3 otherwise the shell script won't work (same thing with pip)

## For Windows

- Having python installed and working on your machine

- Python must run with the command python and not python3 otherwise the shell script won't work (same thing with pip)

- Having [ffmpeg](https://ffmpeg.org/) installed and added to your enviroment variables [tutorial](https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10)








## Installation for Linux

you simply need to clone the repostry and run this commands:

```bash
# Clone the repostry:
git clone https://github.com/BananaPilot/pythonBotDiscord.git
```

then create a file .env and copy this lines in to it 

```env
DISCORD_TOKEN = <yout discord token>

FFMPEG_PATH = ffmpeg
```

If you don't know how to get your own discord token follow this [tutorial](https://www.androidauthority.com/get-discord-token-3149920/): 

Intead for the ffmpeg path for linux you can just leave it as ffmpeg it will autamitacally translate to the path

and finally make the shell script runnable and run the command

```bash
# Make the bash file runnable with:
chmod u+x launch.sh
# Then run:
./launch.sh
```



## Intallation for Windows

you simply need to clone the repostry and run this commands:

```bash
# Clone the repostry:
git clone https://github.com/BananaPilot/pythonBotDiscord.git
```

then create a file .env and copy this lines in to it 

```env
DISCORD_TOKEN = <yout discord token>

FFMPEG_PATH = <path to ffmpeg.exe>
```

If you don't know how to get your own discord token follow this [tutorial](https://www.androidauthority.com/get-discord-token-3149920/)

And finally run the shell script

```bash
# Run the shell script
./launch.ps1
```







    
## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

## Special thanks

- [@Gabriel](https://github.com/Gabixel)

without you this project would have been hell! 💪