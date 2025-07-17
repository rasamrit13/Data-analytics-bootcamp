{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "549e420d-52d2-4111-a7f9-b46e3ede1d7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16\n"
     ]
    }
   ],
   "source": [
    "def sum(a,b):\n",
    "    print(a+b)\n",
    "\n",
    "sum(9, 7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "75b7fc24-a22d-4900-89ed-03596a432929",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n"
     ]
    }
   ],
   "source": [
    "def evennaturals():\n",
    "    for i in range(1, 26):\n",
    "        print(i * 2)\n",
    "\n",
    "evennaturals()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "817e8e90-d619-4840-a750-0d1cc95f589c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ras is 18 years old\n"
     ]
    }
   ],
   "source": [
    "def student( name, age):\n",
    "    print( name, \"is\", age, \"years old\")\n",
    "    \n",
    "student(age=18, name=\"ras\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4770ce86-340d-4b01-81bf-99850fedbcbc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81\n"
     ]
    }
   ],
   "source": [
    "def square(a):\n",
    "    print(a*a)\n",
    "\n",
    "square (9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "80f61f14-a746-4348-a6ba-3300d6b21cb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "odd\n"
     ]
    }
   ],
   "source": [
    "# Write a function to check if a number is even.\n",
    "def even(a):\n",
    "    if a%2==0:\n",
    "        print(\"even\")\n",
    "    else:\n",
    "        print(\"odd\")\n",
    "a= int(input(\"enter a number\"))\n",
    "       \n",
    "even(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "ba9f1e34-48e9-4fc6-93e5-5b0b88db97c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Greatest number is: 8\n"
     ]
    }
   ],
   "source": [
    "#Write a function to return the largest element in a list.\n",
    "def largest(a, b, c):\n",
    "    if a > b:\n",
    "        if a > c:\n",
    "            print(\"Greatest number is:\", a)\n",
    "        else:\n",
    "            print(\"Greatest number is:\", c)\n",
    "    else:\n",
    "        if b > c:\n",
    "            print(\"Greatest number is:\", b)\n",
    "        else:\n",
    "            print(\"Greatest number is:\", c)\n",
    "\n",
    "largest(4,8,7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "73adad12-ef8e-4b33-920e-68c201f029ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "def foo(a, b=1): \n",
    "    return a+b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "e888283c-123a-4c61-975f-7b4f4c4028fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "362880"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def factorial(n):\n",
    "    if n == 0 or n == 1:\n",
    "        return 1  \n",
    "    else:\n",
    "        return n * factorial(n - 1) \n",
    "\n",
    "factorial(9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "5be431eb-17bd-42b7-aa3a-6b019d31348a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string:  helloooo\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of vowels: 5\n"
     ]
    }
   ],
   "source": [
    "def countvowels(a):\n",
    "    vowels = \"aeiouAEIOU\"\n",
    "    count = 0\n",
    "    for char in a:\n",
    "        if char in vowels:\n",
    "            count += 1\n",
    "    print(\"Number of vowels:\", count)\n",
    "\n",
    "string = str(input(\"Enter a string: \"))\n",
    "countvowels(string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "7e416cf0-f349-4165-b6c3-1fab3a2e7d78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number of terms:  8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n"
     ]
    }
   ],
   "source": [
    "def fibonacci(n):\n",
    "    a = 0\n",
    "    b = 1\n",
    "    for i in range(n):\n",
    "        print(a)\n",
    "        a, b = b, a + b\n",
    "\n",
    "n = int(input(\"Enter number of terms: \"))\n",
    "fibonacci(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "5a40620c-cbab-481b-9020-aabba56b936f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apap\n"
     ]
    }
   ],
   "source": [
    "def reverse_string(s):\n",
    "    reversed_str=\"\"\n",
    "    for char in s:\n",
    "        reversed_str=char+reversed_str\n",
    "    return reversed_str\n",
    "\n",
    "print(reverse_string(\"papa\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "4d532aad-4efe-48d8-8c72-3410cb275fe2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string:  madam\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "It is a palindrome.\n"
     ]
    }
   ],
   "source": [
    "def palindrome(a):\n",
    "    reverseds = \"\"\n",
    "    for char in a:\n",
    "        reverseds = char + reverseds\n",
    "    if a == reverseds:\n",
    "        print(\"It is a palindrome.\")\n",
    "    else:\n",
    "        print(\"It is not a palindrome.\")\n",
    "\n",
    "String = str(input(\"Enter a string: \"))\n",
    "palindrome(String)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "0f6040ee-bad6-43ff-87b1-2d7c34d31519",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum is: 50\n"
     ]
    }
   ],
   "source": [
    "def sum_values(*args):\n",
    "    total = 0\n",
    "    for num in args:\n",
    "        total += num\n",
    "    print(\"Sum is:\", total)\n",
    "\n",
    "sum_values(10, 20, 5, 15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "808d5420-5ed7-4010-b4d2-2c74d02c3e19",
   "metadata": {},
   "outputs": [],
   "source": [
    "#properties: mutable, ordered, collection of multiple data types, duplicates allowed\n",
    "#insert, append, extend, pop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "e7dd723c-452b-43bb-8144-be06bed6a521",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 1, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "#append()\n",
    "list=[3,4,5]\n",
    "list.insert(1,1)\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "a85ea967-b5d3-431d-87ba-cc9db5a37ec0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 4, 5, 1, 3]\n"
     ]
    }
   ],
   "source": [
    "#extend\n",
    "list=[3,4,5]\n",
    "list.extend([1,3])\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "033b6d56-02dd-4cdc-9731-2e27c838e4b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 5]\n"
     ]
    }
   ],
   "source": [
    "#pop\n",
    "list=[3,4,5]\n",
    "list.pop(1)\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "ff0e88d3-354e-46b5-a03f-5a73872fbeb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 5]\n"
     ]
    }
   ],
   "source": [
    "list=[3,4,5]\n",
    "list.remove(3)\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "e5daefc6-cc49-403d-8956-43fb38e5143f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "list=[3,4,5]\n",
    "list.clear()\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "d1cd9150-9bfc-4d53-8d1b-81cb1d9cd6d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list=[3,4,5]\n",
    "list.index(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "f9824b80-0eb2-4a26-a47b-0cfc592effbf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list=[3,4,5,4,4,5]\n",
    "list.count(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "d65a6c4e-bef9-4d45-8558-b5a67213e2c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 6, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "list=[5,7,9,6]\n",
    "list.sort()\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "af68c2ca-4444-4c02-8348-ba9d56723286",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 4, 3]\n"
     ]
    }
   ],
   "source": [
    "list=[3,4,5]\n",
    "list.reverse()\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "7dbc2912-991b-4797-950a-1beaf250fb32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 5]\n"
     ]
    }
   ],
   "source": [
    "list=[3,5]\n",
    "b=list.copy()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35fa9f0c-7e97-4540-b269-c4caaacf9415",
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
