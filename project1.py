{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4784d96a-a491-4d6f-b136-55c4515d4ac1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#billing management system project"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c6513246-d248-4ecf-b758-d6f3979434e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the product name car\n",
      "enter the quantity  9\n",
      "enter the price 800000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the total price of the product is\n",
      "car 7200000\n"
     ]
    }
   ],
   "source": [
    "product= str(input (\"enter the product name\"))\n",
    "quantity= int(input (\"enter the quantity \"))\n",
    "price= int(input (\"enter the price\"))\n",
    "bill= quantity * price\n",
    "print(\"the total price of the product is\")\n",
    "print(product,bill)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9e87c8a-f04a-423b-aa72-42f83923bfef",
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
