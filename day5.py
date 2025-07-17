{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23f5a4d0-f625-43f9-aa97-22458476b970",
   "metadata": {},
   "outputs": [],
   "source": [
    "#tuples are immutable\n",
    "#sets are mutable\n",
    "set1.union(set2)\n",
    "set1.intersection(set2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e49d8e84-91b7-4cea-a3b2-5e5570c1ed63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number 1:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The final list is: [2]\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number 2:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The final list is: [2, 3]\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number 3:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The final list is: [2, 3, 4]\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number 4:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The final list is: [2, 3, 4, 5]\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number 5:  6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The final list is: [2, 3, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "#Create an empty list and take 5 numbers as input from the user. Append each number to the list and display the final list\n",
    "list1=[]\n",
    "for i in range(5):\n",
    "    num = int(input(f\"Enter number {i+1}: \"))\n",
    "    list1.append(num)\n",
    "    print(\"The final list is:\", list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1e8d307e-3093-44ed-bf76-240afdee3546",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Updated List: [1, 2, 3, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "#Create two lists: list1 = [1, 2, 3] and list2 = [4, 5, 6]. Extend list1 using list2 and print the updated list.\n",
    "list1 = [1, 2, 3]\n",
    "list2 = [4, 5, 6]\n",
    "list1.extend(list2)\n",
    "print(\"Updated List:\", list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "37fd588a-96b4-4c4f-9fd2-91e45fa9ec89",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 20, 25, 30, 40]\n"
     ]
    }
   ],
   "source": [
    "#Insert the value 25 at index 2 in the list: l = [10, 20, 30, 40].\n",
    "l = [10, 20, 30, 40]\n",
    "l.insert(2, 25)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "048ea229-e58a-4d4f-9690-856abe6003bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 30, 20, 40]\n"
     ]
    }
   ],
   "source": [
    "#Remove the first occurrence of the value 20 from the list: l = [10, 20, 30, 20, 40].\n",
    "l = [10, 20, 30, 20, 40]\n",
    "l.remove(20)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "027a0050-b328-4352-9eab-79c3c0cfac6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Popped Item: 4\n",
      "Updated List: [1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "#Pop the last element from the list [1, 2, 3, 4, 5] and display both the popped item and the updated list.\n",
    "list = [1, 2, 3, 4, 5]\n",
    "poppeditem = listt.pop()\n",
    "print(\"Popped Item:\", poppeditem)\n",
    "print(\"Updated List:\", list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b3526ec3-753d-4f09-9866-29aa8524d9a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Find and print the index of the element 15 in the list [5, 10, 15, 20, 25].\n",
    "list = [5, 10, 15, 20, 25]\n",
    "list.index(15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e66aa6cc-941f-4438-8f7e-a97b96afe2c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Count how many times the number 2 appears in the list [1, 2, 2, 3, 2, 4, 2].\n",
    "list=[1, 2, 2, 3, 2, 4, 2]\n",
    "list.count(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "86efa2ba-f768-4811-b414-6bda27f0cda4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 5, 7, 10]\n",
      "[10, 7, 5, 3]\n"
     ]
    }
   ],
   "source": [
    "#Sort the list [10, 5, 7, 3] in both ascending and descending order.\n",
    "list=[10, 5, 7, 3]\n",
    "list.sort()\n",
    "print(list)\n",
    "list.sort(reverse=True)\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7e5dd701-be6d-4901-8ddd-419fb70797fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 4, 3, 2, 1]\n"
     ]
    }
   ],
   "source": [
    "#Reverse the list [1, 2, 3, 4, 5] using the reverse() method.\n",
    "list=[1, 2, 3, 4, 5]\n",
    "list.reverse()\n",
    "print(list)"
   ]
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
