# Changelog

## [1.1.0-alpha](https://github.com/remarkablegames/knitbone/compare/v1.0.0-alpha...v1.1.0-alpha) (2025-09-27)


### Features

* add artwork assets (entity) ([f649131](https://github.com/remarkablegames/knitbone/commit/f64913121f8cae07c48167cb5e87e46b0a773048))
* add new folder with initial files ([0f5c56d](https://github.com/remarkablegames/knitbone/commit/0f5c56d0684a263a1faf161eed50943add859918))
* add personality_test.rpy for minigames(session1) ([c819ad1](https://github.com/remarkablegames/knitbone/commit/c819ad1c1846679b0ea5091c23dd78f0c49d2bb9))
* add sprites ([75c066f](https://github.com/remarkablegames/knitbone/commit/75c066f14e09bcca86fca8e622e64bbfed8cd204))
* **audio:** play flash sound and fade to white in session1 flashback ([6c3fb2e](https://github.com/remarkablegames/knitbone/commit/6c3fb2e6c1e6769f32ff9192d40e6261c55ef84e))
* **audio:** play footsteps in prologue when ryohei enters the bar ([0c03a77](https://github.com/remarkablegames/knitbone/commit/0c03a7782b62f2ca61347e2b61a73d49d329f00d))
* **audio:** play music terror in prologue ([fd39402](https://github.com/remarkablegames/knitbone/commit/fd39402fef439e842c0d8a615b1237ca3621b241))
* **audio:** play music ticking in hypnosis minigame ([5b7def9](https://github.com/remarkablegames/knitbone/commit/5b7def9934bd508abb98c624dd1422063451d75e))
* **audio:** play sfx ice in bar ([69a9233](https://github.com/remarkablegames/knitbone/commit/69a92337f64f788385a56695c4118ed57801d233))
* **audio:** play sfx stab in ending ([490f470](https://github.com/remarkablegames/knitbone/commit/490f47005212b131a558f17274448cb4278a70af))
* **audio:** play sfx thud ([d219dcf](https://github.com/remarkablegames/knitbone/commit/d219dcf1fb64187416ccca32e4cd61667cf1b5c1))
* **audio:** play sounds chime and door in prologue ([6ce27cf](https://github.com/remarkablegames/knitbone/commit/6ce27cfa44e9e782b0d7ac4bbfe34e4e7e91ffc7))
* **audio:** play tension sfx in prologue intro ([2f6a587](https://github.com/remarkablegames/knitbone/commit/2f6a587e168a20dd3473dbe4ca55bb3a0fced1e4))
* **audio:** play woosh sound when ryohei and eden enters the screen ([a53cbc6](https://github.com/remarkablegames/knitbone/commit/a53cbc65b9a6c1e70056c72716647d7df41b74c5))
* **characters:** add who color and outline to eden and ryohei ([bfe0d7f](https://github.com/remarkablegames/knitbone/commit/bfe0d7f5ace223fcb0d2fe0cf2b6cfd9bf437e5b))
* **game:** add prologue ([9dcf44c](https://github.com/remarkablegames/knitbone/commit/9dcf44c0c9bd09565a995b4d713f38993973da6a))
* minigame (personality test) ([651e698](https://github.com/remarkablegames/knitbone/commit/651e6986a89e1d30ee5d0e0e0c354fa7d30ebdf6))
* **minigames:** add candle win state ([a93d7a0](https://github.com/remarkablegames/knitbone/commit/a93d7a0808a26a6880bf598f85699ed549d320db))
* **minigames:** add hypnosis ([ecb2954](https://github.com/remarkablegames/knitbone/commit/ecb2954e38b8c00c06b51faac6fc8e835402e911))
* **minigames:** add jumpscare in personality_test ([17b3a8d](https://github.com/remarkablegames/knitbone/commit/17b3a8db5a0c6fd7594f6bdd5a20c1a5c12cd69d))
* **minigames:** display moves and play sound for candle ([6a2af47](https://github.com/remarkablegames/knitbone/commit/6a2af47b16a6a25598d57a317e87bd3495dccdbb))
* replace choice background images ([527fd00](https://github.com/remarkablegames/knitbone/commit/527fd00fc40321c8e0cd23916b67c6f626b41431))
* replace choice button background ([8c76136](https://github.com/remarkablegames/knitbone/commit/8c76136902eb1684497efaf53794e5b9524e9111))
* **story:** add candle minigame ([d52f5d8](https://github.com/remarkablegames/knitbone/commit/d52f5d806cb9c6a83243653c177c469af846dade))
* **story:** add ending attack ([e33e178](https://github.com/remarkablegames/knitbone/commit/e33e1785e2b36d3f8cf1d89d75ab7c4b3e4633a4))
* **story:** add scary text from kinetic text tags to ending ([a600f96](https://github.com/remarkablegames/knitbone/commit/a600f96f8ea90d066b0886771f15283101b0e8a4))
* **story:** flip ryohei in prologue ([93e10fe](https://github.com/remarkablegames/knitbone/commit/93e10fe7c41dd2f1c97119ffb08a09dafc518164))


### Bug Fixes

* **characters:** fix music channel in character callback ([85eb2ea](https://github.com/remarkablegames/knitbone/commit/85eb2ea69791c1c615bf125795c7d1d7218f7723))
* **countdown:** set current to length so player can still go back ([ebf94f2](https://github.com/remarkablegames/knitbone/commit/ebf94f2deb27d4f0a1dcc7b0c6d0f60f910cf10c))
* **gui:** update hover_color to blue so it's more accessible ([53a5b44](https://github.com/remarkablegames/knitbone/commit/53a5b44ded21e563c7a95b07b00ca35992787a76))
* **images:** resize images so slow_zoom works in prologue ([8799f9b](https://github.com/remarkablegames/knitbone/commit/8799f9b22cab61b6e77e2799bc7ad051c52be4d9))
* **minigames:** resize cg hypnosis images and add stop button ([9acf0b0](https://github.com/remarkablegames/knitbone/commit/9acf0b0fc4870c98a04465fc27fa6a0c97279f91))
* **minigames:** set text color to white and ensure candles are random ([7706e93](https://github.com/remarkablegames/knitbone/commit/7706e9314af80d175d6a919c56bda15a300711a2))
* **screens:** rename "Preferences" to "Preference" ([e721c0f](https://github.com/remarkablegames/knitbone/commit/e721c0f057c7f5416664f60f8c1e116dabfe9da3))
* **story:** fix indentation mismatch in session1 ([2b02493](https://github.com/remarkablegames/knitbone/commit/2b024932d00b1266853f33478a73316cd2c3e2d0))
