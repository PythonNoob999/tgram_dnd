
<div align="center"> <img src="resources/tgram_dnd.svg" width=250 width=250> <a href="https://github.com/PythonNoob999/tgram_dnd"><h1>Tgram-DND</h1></a>  <b>a helper/utils library to help build Telegram Bot Drag-And-Drop Applications</b> <br> <a href="https://tgram-dnd.readthedocs.io/en/latest/index.html">Documentation</a> • <a href="https://github.com/PythonNoob999/tgram_dnd/tree/main/examples">Examples</a> </div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About Project

tgram_dnd is a helper/utils library to help build Telegram Bot Drag-And-Drop application
or just simply code bots faster :)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With
* [tgram](https://github.com/z44d/tgram) (Bot API Interaction)
* [jinja2](https://jinja.palletsprojects.com/en/stable/) (string templating)
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

### Prerequisites

* [python<=3.10](https://www.python.org/)
* [tgram<=1.12.16](https://github.com/z44d/tgram/releases/tag/v1.12.6)
* [jinja2<=3.1.5](https://github.com/pallets/jinja/releases/tag/3.1.5)

### Installation

    1. Clone From Source (Not Recommended)
        * git clone https://github.com/PythonNoob999/tgram_dnd.git
        * cd tgram_dnd
        * python3 -m pip install . -U
        * done✅
    
    2. Installing From PIP (Recommended)
        * python3 -m pip install tgram_dnd
        * done ✅

## Usage

#### Bot Setup
```python
from tgram_dnd import (
  App, BotConfig, MessageFlow, MessageBlock, Reply
)
from tgram import TgBot

bot = TgBot("INSERT_BOT_TOKEN")
app = App(
  bot=bot,
  config=BotConfig(
    strings="text.json",
    default_lang="en"
  ),
)

app.add_flow(
  MessageFlow(
    ...
  )
)

app.run()
```

[Examples](https://github.com/PythonNoob999/tgram_dnd/tree/main/examples)

## Roadmap
- Adding More Abstracted Methods
- Configuration System (db_setup, strings, etc) (50%)
- JsonToBlocks Converter
- Add Documentaion
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GPL-3 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

SpicyPenguin - [telegram](https://t.me/kerolis55463)

<p align="right">(<a href="#readme-top">back to top</a>)</p>