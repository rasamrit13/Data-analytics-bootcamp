{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37699835-daa2-4ce5-a81c-eaf4e22c6b12",
   "metadata": {},
   "outputs": [],
   "source": [
    "#password"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fc0eb456-5e65-4252-84a9-ca05e8093055",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the password 345\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the correct password 3 attempts left\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the password 1309\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "unlocked\n"
     ]
    }
   ],
   "source": [
    "password=\"1309\"\n",
    "attempt=4\n",
    "while attempt>0:\n",
    "    user_input= input(\"enter the password\")\n",
    "    if user_input== password:\n",
    "        print(\"unlocked\")\n",
    "        break\n",
    "    else:\n",
    "        attempt-=1\n",
    "        print(f\"enter the correct password {attempt} attempts left\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f094223f-717b-483f-a4c6-94198e4d7134",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
