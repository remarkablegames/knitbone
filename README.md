<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/knitbone/master/game/gui/window_icon.png" alt="KnitBone">
</p>

# KnitBone

![release](https://img.shields.io/github/v/release/remarkablegames/knitbone)
[![build](https://github.com/remarkablegames/knitbone/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/knitbone/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/knitbone/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/knitbone/actions/workflows/lint.yml)

🦴 KnitBone is a psychological horror visual novel where the therapist is more traumatized than the patient.

Play the game on:

- [remarkablegames](https://remarkablegames.org/knitbone)
- [itch.io](https://remarkablegames.itch.io/knitbone)

## Credits

### Art

- [aespipu](https://aespipu.itch.io/)

### Writing

- [meo](https://github.com/mizphawu)
- [The Sloth](https://a-villarroel.itch.io/)

### Development

- [remarkablemark](https://github.com/remarkablemark)

### Music

- [seamus](https://seemvevo.itch.io/)

### Sounds

- [Kenney](https://kenney.nl/assets/interface-sounds)
- Pixabay
  - [Bone snap](https://pixabay.com/sound-effects/bone-snap-408148/)
  - [Camera Flash](https://pixabay.com/sound-effects/camera-flash-204151/)
  - [Door Creak 02](https://pixabay.com/sound-effects/door-creak-02-79920/)
  - [Footsteps Male](https://pixabay.com/sound-effects/footsteps-male-362053/)
  - [Glass Breaking Sound Effect](https://pixabay.com/sound-effects/glass-breaking-sound-effect-240679/)
  - [Heartbeat 01 - BRVHRTZ](https://pixabay.com/sound-effects/heartbeat-01-brvhrtz-225058/)
  - [Jump scare sound 2](https://pixabay.com/sound-effects/jump-scare-sound-2-82831/)
  - [Knock knock knock](https://pixabay.com/sound-effects/knock-knock-knock-40474/)
  - [Lighting a Fire](https://pixabay.com/sound-effects/lighting-a-fire-14421/)
  - [Main Door Opening-Closing](https://pixabay.com/sound-effects/main-door-opening-closing-38280/)
  - [Radio Static](https://pixabay.com/sound-effects/radio-static-323621/)
  - [Screamer Jumpscare](https://pixabay.com/sound-effects/screamer-jumpscare-66896/)
  - [Tension Stinger - Ambience](https://pixabay.com/sound-effects/tension-stinger-ambience-355381/)
  - [Thud Impact Sound SFX](https://pixabay.com/sound-effects/thud-impact-sound-sfx-379990/)
  - [Ticking Clock_1](https://pixabay.com/sound-effects/ticking-clock-1-27477/)
  - [Wind chime small](https://pixabay.com/sound-effects/wind-chime-small-64660/)
  - [Wrapping Paper Rustle](https://pixabay.com/sound-effects/wrapping-paper-rustle-72405/)

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
