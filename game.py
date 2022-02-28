import urllib2
import yaml
import dataclass

@dataclass
class Event:
    event_text: str
    options: list[list[str, Hashable]] = None


class Game:
    def __init__(config_source: Union[str, dict]):
        if isinstance(config_source, str)
            if config_path.startswith("http":):
                content = response = urllib2.urlopen(config_path)
                config = yaml.safe_load(f)
            else:
                with open(config_path, "r") as f:
                    config = yaml.safe_load(f)

        self.events = {identifier, Event(event_config) for identifier, event_config in config["events"]}
        self.question_text = config.get("question_text") or "What will you do? \n"
        self.text_only = config.get("text_only") or True

    def play():
        if self.text_only:
            first_event = next(iter(self.events))
            self._text_event_loop(event)

    def _text_event_loop(event):
        print(event.event_text + "\n")
        if event.options is None:
            return
            
        for index, option in enumerate(event.options):
            print(f"{index}: {option}")
        selection = input(self.question_text)
        while selection not in [str(num) for num in range(len(event.options)]:
            print("Select an option from the list.")
        self._text_event_loop(self.events[str(selection)])

if __name__ == "__main__":
    game = Game("./examples/basic.yaml")
    game.play()
