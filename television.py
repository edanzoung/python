class Television:
    """constants"""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self)-> None:
        """default settings"""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """Turn the TV on or off"""
        self.__status = not self.__status

    def mute(self)-> None:
        """Mute or unmute"""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """Increase channel"""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """Decrease channel"""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """Increase volume"""
        if self.__status:
            self.__muted = False

            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Decrease volume"""
        if self.__status:
            self.__muted = False

            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self)-> str:
        """TV status"""
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}" 
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
