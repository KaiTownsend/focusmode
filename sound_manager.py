# Copyright 2023 Kai Townsend

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import threading
import simpleaudio as sa


class SoundManager:
    def __init__(self):
        self.current_play_objects = {}
        self.play_objects_lock = threading.Lock()

    def play_sound(self, sound_file):
        if sound_file and sound_file != "None":
            threading.Thread(
                target=self._play_sound_in_thread, args=(sound_file,)
            ).start()

    def _play_sound_in_thread(self, sound_file):
        play_obj = sa.WaveObject.from_wave_file(sound_file).play()

        with self.play_objects_lock:
            self.current_play_objects[sound_file] = play_obj

        play_obj.wait_done()

        with self.play_objects_lock:
            if sound_file in self.current_play_objects:
                del self.current_play_objects[sound_file]
