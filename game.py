import urllib
import yaml
from dataclasses import dataclass
from typing import Hashable, List, Tuple, Union
import time
import sys

@dataclass
class Event:
    event_text: str
    options: List[Tuple[str, Hashable]] = None


class Game:
    def __init__(self, config_source: Union[str, dict]):
        if isinstance(config_source, str):
            if config_source.startswith("http"):
                content = response = urllib.urlopen(config_source)
                config = yaml.safe_load(f)
            else:
                with open(config_source, "r") as f:
                    config = yaml.safe_load(f)

        self.events = {identifier: Event(**event_config) for identifier, event_config in config["events"].items()}
        self.question_text = config.get("question_text") or "\nWhat will you do? \n"
        self.text_only = config.get("text_only") or True

    def play(self):
        if self.text_only:
            first_event = next(iter(self.events))
            self._text_event_loop(self.events[first_event])
            time.sleep(1)
            self._clear_terminal()

    def _text_event_loop(self, event):
        self._clear_terminal()
        print(event.event_text.strip() + "\n")
        time.sleep(0.3 * len(event.event_text.strip()) / 10)
        if event.options is None:
            return
        
        selection = None
        while selection not in [str(num) for num in range(len(event.options))]:

            for index, option in enumerate(event.options):
                print(f"{index}: {option[0]}")
            time.sleep(0.4 * len(event.options))

            selection = input(self.question_text)
                
        self._text_event_loop(self.events[event.options[int(selection)][1]])
    
    @staticmethod
    def _clear_terminal():
        print("\033[H\033[J", end="")


if __name__ == "__main__":
    game = Game(sys.argv[1])
    game.play()
