# TAS Recorder

A really simple tool for creating tool-assisted content or simple macros

## Changelog

See the [CHANGELOG file](CHANGELOG.md) for details on version changes.

## Features

- Recorder - Record keyboard inputs and mouse clicks and output to a JSON file
- Player - Play recorded file with set playback speed

## Getting started

### For users
To install it, run this command in the terminal
```
pip install tas-recorder
```
That's it for installing it!

### For Developers:
If you're interested in running tests or contributing to the development:
1. Clone the repository:
`git clone https://github.com/sabifiedsab/TAS-Recorder.git`
2. Navigate to the cloned directory and install the package in editable mode:
`pip install -e`
3. Run tests as described in the [Testing files](#testing-files) section.

### Testing files
Inside the folder `/tests/` there is a file called `test.py`
When you run it you can choose between `Recorder Mode` or `Playback Mode`

When you choose one of them it will wait 3 seconds before starting. 

You can use this file as a sandbox before making your own

## Usage

### Record to a file:
```python
from tas import recorder

filename = "output_file.json" # must end in .json, optional

recorder.record(filename)
```
Now press ESC to stop the recording and a json file will be created in your directory

### Play recorded file
```python
from tas import playback

filename = "output_file.json"

playback.play(filename)
```

## Additional Parameters
When you call `recorder.record()` you can specify the output file and if you want to also record mouse inputs

**It's not required to specify filename, but is highly recommended**

If you want to disable mouse inputs add this parameter in your `recorder.record()` like this
```python
recorder.record(include_mouse = False)
```

When you call `playback.play()` you can specify playback and recording speed. 

**Beware that if you specify a playback speed, the record speed will be ignored!**

#### Record Speed
If you record your inputs at a certain game speed you can specify that with `record_speed`
Example if you recorded with game at half speed:
```python
playback.play(record_speed = 0.5)
```

#### Playback Speed
If you want to specify how fast your input file should execute at a custom playback speed
Example if you want to execute inputs at 2 times speed:
```python
playback.play(playback_speed = 2)
```

## Limitations

- This tool isn't really suited for 3d applications but will work in any 2d game

### Dependencies

- pynput

## License

[MIT](LICENSE)
