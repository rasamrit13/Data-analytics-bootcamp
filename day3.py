{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f37780c-0ba8-4e4c-8028-cd2e6fcc095e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#while loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "00e74bfe-1bb6-43c8-83b9-d4b10ccb06e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7 x 1 = 7\n",
      "7 x 2 = 14\n",
      "7 x 3 = 21\n",
      "7 x 4 = 28\n",
      "7 x 5 = 35\n",
      "7 x 6 = 42\n",
      "7 x 7 = 49\n",
      "7 x 8 = 56\n",
      "7 x 9 = 63\n",
      "7 x 10 = 70\n"
     ]
    }
   ],
   "source": [
    "num= int(input(\"enter a number\"))\n",
    "i=1\n",
    "while i<= 10:\n",
    "    print(f\"{num} x {i} = {num * i}\")\n",
    "    i+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3408b061-c593-468f-ae6c-ace99733307e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#user has 4 attempts to enter the password"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "cf54d544-b7d2-488d-8564-7d7b63111e78",
   "metadata": {},
   "outputs": [
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
   "id": "8ed56dfb-4416-4acc-a7e5-d2f8cdf22510",
   "metadata": {},
   "outputs": [],
   "source": [
    "#for loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "b40c5261-cca6-4df7-8814-19dcceaccc22",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4 x 1= 4\n",
      "4 x 2= 8\n",
      "4 x 3= 12\n",
      "4 x 4= 16\n",
      "4 x 5= 20\n",
      "4 x 6= 24\n",
      "4 x 7= 28\n",
      "4 x 8= 32\n",
      "4 x 9= 36\n"
     ]
    }
   ],
   "source": [
    "num=int(input(\"enter a number\"))\n",
    "for i in range (1, 10):\n",
    "       print(f\"{num} x {i}= {num * i}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "6cb90140-ee80-4488-afc7-32cc30cf976f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "a= 2 ** 3\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "f6533c56-eaa7-402f-afe8-99195b081927",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Go\n"
     ]
    }
   ],
   "source": [
    "if 1: print('Go')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "f39f2912-35bd-4452-9841-77598e0c0f38",
   "metadata": {},
   "outputs": [],
   "source": [
    "if 0: print('Yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "32a2eed7-6cac-486f-8117-73d4257e2639",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "7415d69c-846b-4016-b16b-0d4a384f3e17",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bool(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "a475fcee-b80e-40ad-9db6-de26095e09e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yes\n"
     ]
    }
   ],
   "source": [
    " if 5 > 3: print('Yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "92b50bfc-3143-422d-a843-255abac1b894",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "for i in range(3): \n",
    "    if i == 1: \n",
    "        continue; \n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "e2e098e5-1ccb-44c5-a0f1-237b08c1b475",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 > 3 and 2 < 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "b443f6b6-d4f6-42f2-bc62-462849f3d47d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 == 10 and 5 < 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "2ed976d8-9836-48e7-ad49-fe04cfb4be11",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len('Hi')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "8eee172f-d29d-4919-8f35-66d799002c95",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " 2 ** 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "65199a76-a0f0-4616-856a-d2afba00fd12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range(1, 10, 3)"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range(1, 10, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "fb83e0d5-5b66-4f54-a72a-876468a67383",
   "metadata": {},
   "outputs": [],
   "source": [
    "if 0: \n",
    "    print('Yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "8935eb6f-0f9d-4178-af29-2aa619b4b6ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 > 3 and 2 < 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "27172434-aefb-49b4-b065-665dc4de44c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 == 10 and 5 < 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "589d5d04-610c-4e6c-8c1c-5ce08d0c0f9d",
   "metadata": {},
   "outputs": [
    {
     "ename": "_IncompleteInputError",
     "evalue": "incomplete input (2014374604.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[87], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    if x == 5 and x < 10:\u001b[0m\n\u001b[0m                         ^\u001b[0m\n\u001b[0;31m_IncompleteInputError\u001b[0m\u001b[0;31m:\u001b[0m incomplete input\n"
     ]
    }
   ],
   "source": [
    "if x == 5 and x < 10:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "0d9869cb-3dc6-497e-a5e0-b1cc2b01fb24",
   "metadata": {},
   "outputs": [
    {
     "ename": "_IncompleteInputError",
     "evalue": "incomplete input (1586706856.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[88], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    if (x == 5):\u001b[0m\n\u001b[0m                ^\u001b[0m\n\u001b[0;31m_IncompleteInputError\u001b[0m\u001b[0;31m:\u001b[0m incomplete input\n"
     ]
    }
   ],
   "source": [
    " if (x == 5):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "de6e9bf8-afcf-4239-afc7-49709920a384",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 % 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "30e72add-7f44-4063-af30-fb1038d4d695",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3 + 2 * 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "3968d24c-6f60-40bf-9329-b16727eb711c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yes\n"
     ]
    }
   ],
   "source": [
    " if 5 > 3: print('Yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "3a12945b-1a5b-4061-941b-24b74c9ff6d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "4 != 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "84f6f8f0-bbd1-4b09-a630-17f339c1bc67",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type('True')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "ec0b3c35-5b64-4a5f-9dd4-e662e4101ab0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 21\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "divisible\n"
     ]
    }
   ],
   "source": [
    "#Write a Python program to check if a number is divisible by both 3 and 7\n",
    "num= int(input(\"enter a number\" ))\n",
    "if num%3== 0 and num% 7==0:\n",
    "                print(\"divisible\")\n",
    "else:\n",
    "                print(\"not divisble\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "08569488-9509-4061-9058-6cb00dbfc779",
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
      "50\n",
      "52\n",
      "54\n",
      "56\n",
      "58\n",
      "60\n",
      "62\n",
      "64\n",
      "66\n",
      "68\n",
      "70\n",
      "72\n",
      "74\n",
      "76\n",
      "78\n",
      "80\n",
      "82\n",
      "84\n",
      "86\n",
      "88\n",
      "90\n",
      "92\n",
      "94\n",
      "96\n",
      "98\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "#Write a program to print all even numbers between 1 and 100 using a for loop.\n",
    "for num in range (1,101):\n",
    "    if num %2==0:\n",
    "        print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "96db51b7-dbcc-41fa-8fa3-ac5179dc865d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number 8\n",
      "Enter second number 7\n",
      "Enter third number 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Greatest number is 8\n"
     ]
    }
   ],
   "source": [
    "#Write a Python program to input three numbers and print the greatest one using nested if-else.\n",
    "a = int(input(\"Enter first number\"))\n",
    "b = int(input(\"Enter second number\"))\n",
    "c = int(input(\"Enter third number\"))\n",
    "\n",
    "if a > b:\n",
    "    if a > c:\n",
    "        print(\"Greatest number is\", a)\n",
    "    else:\n",
    "        print(\"Greatest number is\", c)\n",
    "else:\n",
    "    if b > c:\n",
    "        print(\"Greatest number is\", b)\n",
    "    else:\n",
    "        print(\"Greatest number is\", c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "bb54abc9-9e2a-4ee6-ad9f-46d8b8bde504",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50\n",
      "49\n",
      "48\n",
      "47\n",
      "46\n",
      "45\n",
      "44\n",
      "43\n",
      "42\n",
      "41\n",
      "40\n",
      "39\n",
      "38\n",
      "37\n",
      "36\n",
      "35\n",
      "34\n",
      "33\n",
      "32\n",
      "31\n",
      "30\n",
      "29\n",
      "28\n",
      "27\n",
      "26\n",
      "25\n",
      "24\n",
      "23\n",
      "22\n",
      "21\n",
      "20\n",
      "19\n",
      "18\n",
      "17\n",
      "16\n",
      "15\n",
      "14\n",
      "13\n",
      "12\n",
      "11\n",
      "10\n",
      "9\n",
      "8\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "#WAP to print numbers from 50 to 1 in reverse using a while loop.\n",
    "num= 50\n",
    "while num>=1:\n",
    "    print(num)\n",
    "    num-=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "5363788b-6a56-4223-aa47-f8ae7bdbd47e",
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
      "9 x 1 = 9\n",
      "9 x 2 = 18\n",
      "9 x 3 = 27\n",
      "9 x 4 = 36\n",
      "9 x 5 = 45\n",
      "9 x 6 = 54\n",
      "9 x 7 = 63\n",
      "9 x 8 = 72\n",
      "9 x 9 = 81\n",
      "9 x 10 = 90\n"
     ]
    }
   ],
   "source": [
    "#WAP to take a number and print its multiplication table up to 10.\n",
    "num= int(input(\"enter a number\"))\n",
    "i=1\n",
    "while i<= 10:\n",
    "    print(f\"{num} x {i} = {num * i}\")\n",
    "    i+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "18be75f5-86c1-47ff-8a67-07bafe6799ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "10\n",
      "15\n",
      "20\n",
      "25\n",
      "30\n",
      "35\n",
      "40\n",
      "45\n",
      "50\n",
      "55\n",
      "60\n",
      "65\n",
      "70\n",
      "75\n",
      "80\n",
      "85\n",
      "90\n",
      "95\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "#Write a program to count how many numbers between 1 to 100 are divisible by 5.\n",
    "for num in range (1,101):\n",
    "    if num %5==0:\n",
    "        print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "01232f38-b9c1-4537-aa6a-2b1fac21a682",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the year 2022\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "not a leap year\n"
     ]
    }
   ],
   "source": [
    "#WAP to check whether a given year is a leap year.\n",
    "year= int(input(\"enter the year\"))\n",
    "if year%4==0:\n",
    "    print(\"leap year\")\n",
    "else:\n",
    "    print(\"not a leap year\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "029d59b7-5d81-4d7d-8053-3aa0f308c07b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the factorial of 8 is 40320\n"
     ]
    }
   ],
   "source": [
    "# WAP to print the factorial of a number using for loop.\n",
    "num= int(input(\"enter a number\"))\n",
    "if num<0:\n",
    "    print(\"enter a positive number\")\n",
    "else:\n",
    "    factorial=1\n",
    "    for i in range(1, num+1):\n",
    "        factorial *= i\n",
    "    print(f\"the factorial of {num} is {factorial}\")    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "eb57029a-17fe-46d2-868f-92cc4d5d1e35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number -9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "negative\n"
     ]
    }
   ],
   "source": [
    "# WAP to check if a number is positive, negative or zero using if-elif-else.\n",
    "a= int(input(\"enter a number\"))\n",
    "if a>0:\n",
    "    print(\"positive\")\n",
    "elif a==0:\n",
    "    print(\" no. is zero\")\n",
    "else:\n",
    "    print(\"negative\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "f21e722c-2335-47f3-a714-6f162e039dfd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 12\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "even \n"
     ]
    }
   ],
   "source": [
    "#WAP to take a number as input and print whether it's even and greater than 10.\n",
    "num= int(input(\"enter a number\"))\n",
    "if num %2==0:\n",
    "    print(\"even \")\n",
    "elif num %2==0 and num<10:\n",
    "    print(\"even and greater than 10\")\n",
    "else:\n",
    "    print(\"odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "67055b57-976c-4cfe-acb6-7e86482ad0ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "4\n",
      "5\n",
      "7\n",
      "8\n",
      "10\n",
      "11\n",
      "13\n",
      "14\n",
      "16\n",
      "17\n",
      "19\n",
      "20\n",
      "22\n",
      "23\n",
      "25\n",
      "26\n",
      "28\n",
      "29\n",
      "31\n",
      "32\n",
      "34\n",
      "35\n",
      "37\n",
      "38\n",
      "40\n",
      "41\n",
      "43\n",
      "44\n",
      "46\n",
      "47\n",
      "49\n",
      "50\n"
     ]
    }
   ],
   "source": [
    "for num in range(1, 51):\n",
    "    if num % 3 == 0:\n",
    "        continue \n",
    "    print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "f66342e6-3197-4b78-ae3e-a54621cf67c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string:  z\n"
     ]
    }
   ],
   "source": [
    "String = str(input(\"Enter a string: \"))\n",
    "for char in String:\n",
    "    if char == 'z':\n",
    "        break \n",
    "    print(char)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "bb35b565-c77c-4b95-8fca-2389e54009aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  5432\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reversed number of 5432 is 2345\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "reversednum = 0\n",
    "original = num\n",
    "n = abs(num)\n",
    "\n",
    "while n > 0:\n",
    "    digit = n % 10          \n",
    "    reversednum = reversednum * 10 + digit  \n",
    "    n //= 10                  \n",
    "if num < 0:\n",
    "    reversednum = -reversednum\n",
    "print(f\"Reversed number of {original} is {reversednum}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d78d8f9-ca54-4ae6-9dd7-0904a5f92830",
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
