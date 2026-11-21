import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"


    def test_power(self):
        self.tv1.power()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tv1.power()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"


    def test_mute(self):
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert "Volume = 0" in self.tv1.__str__()
        
    def test_channel_up(self):
        self.tv1.channel_up()
        assert "Channel = 0" in self.tv1.__str__()

        self.tv1.power()
        self.tv1.channel_up()
        assert "Channel = 1" in self.tv1.__str__()

        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert "Channel = 0" in self.tv1.__str__()


    def test_channel_down(self):
        self.tv1.channel_down()
        assert "Channel = 0" in self.tv1.__str__()

        self.tv1.power()
        self.tv1.channel_down()
        assert "Channel = 3" in self.tv1.__str__()


    def test_volume_up(self):
        self.tv1.volume_up()
        assert "Volume = 0" in self.tv1.__str__()

        self.tv1.power()
        self.tv1.volume_up()
        assert "Volume = 1" in self.tv1.__str__()

        self.tv1.mute()
        self.tv1.volume_up()
        assert "Volume = 2" in self.tv1.__str__()

        self.tv1.volume_up()
        assert "Volume = 2" in self.tv1.__str__()


    def test_volume_down(self):
        self.tv1.volume_down()
        assert "Volume = 0" in self.tv1.__str__()

        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert "Volume = 1" in self.tv1.__str__()

        self.tv1.mute()
        self.tv1.volume_down()
        assert "Volume = 0" in self.tv1.__str__()
