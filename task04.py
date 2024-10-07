{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89cb0363-f097-46f7-9884-6988d25f866c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Task 4\n",
    "from pynput import keyboard\n",
    "\n",
    "def on_press(key):\n",
    "    try:\n",
    "        print(f'Key {key.char} pressed')\n",
    "    except AttributeError:\n",
    "        print(f'Special key {key} pressed')\n",
    "\n",
    "def on_release(key):\n",
    "    print(f'Key {key} released')\n",
    "    # Stop listener if 'esc' is pressed\n",
    "    if key == keyboard.Key.esc:\n",
    "        return False\n",
    "\n",
    "# Collect events until released\n",
    "with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:\n",
    "    listener.join()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
