# npm-get-user-info
npm html profile parser


# Launch instructions for Linux

### The easiest:

1. Download zip archive and extract it (or clone this repository) to your system

2. Add a Directory with your executable (file `pm-grabber` is stored in `'YOUR PATH'/npm-get-user-info/dist/npm-grabber`) to $PATH: permanently by running the following in Terminal: `nano ~/.bashrc`

3. Add in the end of the file `PATH=$PATH:~/YOUR NEW PATH TO SCRIPT`, mark it with ##PATH## for further needs

4. Save & exit wtih: `ctrl+O` `ctrl+X`

5. Run: `source ~/.bashrc`

6. Confirm changes with: `echo $PATH`. You'll see the path to your new directory in the end of the line.

7. Launch it from terminal with `npm-grabber` command. That's all.
 

### If you want to have it in your App List and on the App Dock:

1. Choose the directory which is in your `$PATH` or create your own directory and just add it in your `$PATH`

2. Open `npm.desktop` file and replace `'PATH TO THE FILE'` in `Exec=`, `Path=` and `Icon=` with your real path to these files.

3. Move `npm.desktop` to `~/.local/share/applications/`

4. If you setup the `npm.desktop` file correctly, you will now be able to see it in your App List and will be able to move an app to your App Dock. 

> 🐧 You may also just use the source code `npm-grabber.py` file
For more instructions of how to launch  `.py` scripts --> [see here in my other repo](https://github.com/Cacodemon503/hackerrank-parser/blob/source/README.md)


# #----------------------OTHER OPTIONS-----------------------#

### [Code for Windows](https://github.com/Cacodemon503/npm-get-user-info/tree/master)  
