<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/knitbone/master/game/gui/window_icon.png" alt="KnitBone">
</p>

# KnitBone

![release](https://img.shields.io/github/v/release/remarkablegames/knitbone)
[![build](https://github.com/remarkablegames/knitbone/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/knitbone/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/knitbone/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/knitbone/actions/workflows/lint.yml)

🦴 KnitBone

Play the game on:

- [remarkablegames](https://remarkablegames.org/knitbone)

## Credits

### Art

- [aespipu](https://aespipu.itch.io/)

### Audio

- [Kenney](https://kenney.nl/assets/interface-sounds)
- Pixabay
  - [Footsteps Male](https://pixabay.com/sound-effects/footsteps-male-362053/)
  - [Glass Breaking Sound Effect](https://pixabay.com/sound-effects/glass-breaking-sound-effect-240679/)
  - [Open and Close Door](https://pixabay.com/sound-effects/open-and-close-door-405453/)
  - [Tension Stinger - Ambience](https://pixabay.com/sound-effects/tension-stinger-ambience-355381/)
  - [Wind chime small](https://pixabay.com/sound-effects/wind-chime-small-64660/)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

Check the version:

```sh
renpy --version
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/knitbone.git
cd knitbone
```

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to open the developer menu.

## Cache

Clear the cache:

```sh
find game -name "*.rpyc" -delete
```

Or open `Ren'Py Launcher` > `Force Recompile`:

```sh
renpy
```

## Lint

Lint the game:

```sh
renpy game lint
```
