# bbsrc

Source files for Play by Play baseball game simulations for all MLB games between 1964-2018. These files are required for [bbcmd](https://github.com/luciancooper/bbcmd) and are divided info 5 types:

- **ctx**: supplementary contextual information generated by retrosheet's BEVENT tool that act as training wheels during the debugging process.
- **eve**: the formatted play by play data for all games in a given year
- **gid**: schedule files - contains all game ids and the number of events that occured in each of those games for a given year
- **ros**: contains rows of all the player codes for all players who appeared in an MLB game in a given year
- **team**: contain a list of the team codes for all MLB teams in the league in a given year

All raw files are located in the `files` folder

____

## Commands

 * The following are descriptions of the four command line tools used in the generation of all the data in the `files` folder of this repository.

## `bbretro`

 - Downloads and unzips play by play data from [retrosheet.org](https://www.retrosheet.org/). Retrosheet is an amazing organization that has painstakingly compiled the play by play data for every MLB game dating back to 1921.
 - Find out more about the Retrosheet project [here](https://www.retrosheet.org/about.htm).
 - Their index of compiled play by play files (from which this tool draws from) can be found [Here](https://www.retrosheet.org/game.htm).

###### Command syntax:

```bash
bbretro years outdir
```

 - `years` - **required**: the specified MLB seasons, can be a single year (`2016`), range of years (`2014-2016`) or comma separated combination of the two (`2012-2014,2016` or `2012-2014,2015-2017`, etc.)
 - `outdir` - **optional**: the folder to download retrosheet files to. If not specified, the current working directory will be used

## `bbcat`

 * concatenates all the retrosheet event files (.EVA & .EVN) for a year into a single file
 * command takes an input of a range of years, and an output folder
 * retrosheet event files must exist in current directory or command is useless

###### Command syntax:

```bash
bbcat outdir start end
```

- `outdir` - **required**: the directory to output concatenated files to
- `start` - **required**: the first year in the range of years
- `end` - **optional**: the last year in the range of years. If not provided, then range consists of a single year: `start`

## `bbraw`

* A debugging tool for intermediate files that are parsed in memory in the `bbsrc` command.

###### Command syntax:

```bash
bbraw type year > outfile
```
 - `type` - **required** : the type of raw file, choices: *eve*,*mod*,*dfn*,*hnd*,*ros*,*ctx*,*ecode*
 - `year` - **required** : a single year to parse the raw file for
 - `outfile` - **optional**: but strongly recomended, if this is not included, all lines of the file will be written out to the command prompt


## `bbsrc`

 * takes input in the form of retrosheet play by play files and files outputted by retrosheets `BEVENT` tool to form the 5 types of files (*gid* , *eve* , *ros* , *ctx* , *team*) found in the `files` directory of this repository.  

###### Command syntax:
```bash
bbraw type years outdir
```

 - `type` - **required** : the type of compilation to run, choices: *gid* , *eve* , *ros* , *ctx* , *team*
 - `years` - **required** : the seasons for which the specified file type will be compiled for
 - `outdir` - **required** : the folder into which the compiled files will be written
