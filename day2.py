{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5dd4216d-c80e-4594-948d-e96f547295ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "#billing management system"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "be690210-3157-4f94-9d7d-76c5ae30d885",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the product name lays\n",
      "enter the quantity  10\n",
      "enter the price 20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the total price of the product is\n",
      "lays 200\n"
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
   "id": "8707c376-1ae2-466a-8fd3-6e716c11d557",
   "metadata": {},
   "outputs": [],
   "source": [
    "#addition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "96c06d29-d932-42b9-b0c4-41df7c3b1d62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "17.6\n"
     ]
    }
   ],
   "source": [
    "a= 5\n",
    "b= 7\n",
    "c= 5.6\n",
    "d= a+b+c\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7a7f8c70-30b6-47c4-a980-f1591f538dc5",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for +: 'int' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[9], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m a\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m7\u001b[39m \n\u001b[1;32m      2\u001b[0m b\u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhello\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m----> 3\u001b[0m c\u001b[38;5;241m=\u001b[39m a\u001b[38;5;241m+\u001b[39mb\n",
      "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for +: 'int' and 'str'"
     ]
    }
   ],
   "source": [
    "a= 7 \n",
    "b= \"hello\"\n",
    "c= a+b\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f13762da-c50d-4791-ad40-72cbbb83dfa1",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for +: 'int' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[10], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m a\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m7\u001b[39m\n\u001b[1;32m      2\u001b[0m b\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m9\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m----> 3\u001b[0m c\u001b[38;5;241m=\u001b[39ma\u001b[38;5;241m+\u001b[39mb\n",
      "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for +: 'int' and 'str'"
     ]
    }
   ],
   "source": [
    "a= 7\n",
    "b=\"9\"\n",
    "c=a+b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5708bf42-92ee-4648-b4e6-9201b83c73fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bye\n"
     ]
    }
   ],
   "source": [
    "a= 10\n",
    "if a>15:\n",
    "    print(\"hello\")\n",
    "else:\n",
    "    print(\"bye\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a0015e3-d82b-4a22-b9ee-c5055caf49b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#eligibity for voting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d247595c-ab2c-41d3-b9c5-c46aa2cddf68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter age 65\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you are eligible\n"
     ]
    }
   ],
   "source": [
    "age= int(input(\"enter age\"))\n",
    "if age>=18:\n",
    "    print(\"you are eligible\")\n",
    "else:\n",
    "    print(\"you're not eligible\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5694a96-c2eb-4777-9d5f-3fed4c03bea6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#assignment 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5cd121f3-0874-410b-90b2-79191167f16f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "B\n"
     ]
    }
   ],
   "source": [
    "if 10 < 2:\n",
    "    print('A')\n",
    "else:\n",
    "    print('B')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7d31d0d0-9946-4730-9664-778bdb230cc1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'123'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " str(123)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "bc0771b3-090f-48fe-826c-c5e913f991bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "x = 0\n",
    "if x:\n",
    "    print('True')\n",
    "else:\n",
    "    print('False')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "d5f66fdf-dfb1-4da4-89ec-ce88a9a36c2a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "x = '10'\n",
    "print(int(x) + 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa89e1b6-f247-4177-bc0b-29513135ba37",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Write a Python program to check whether a number entered by the user is positive or negative."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "81bcbbbd-1bad-4486-9d23-e6a7f6de8ddf",
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
    "a= int(input(\"enter a number\"))\n",
    "if a>=0:\n",
    "    print(\"positive\")\n",
    "else:\n",
    "    print(\"negative\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0293e40-0284-484b-8588-faaa11765e52",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Take user input for age. If age is >= 18, print 'Eligible to vote' else print 'Not eligible'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "bb068491-094d-4f3e-981d-51463f661518",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter age 9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Not eligible\n"
     ]
    }
   ],
   "source": [
    "age= int(input(\"enter age\"))\n",
    "if age>=18:\n",
    "    print(\"Eligible to vote\")\n",
    "else:\n",
    "    print(\"Not eligible\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ede5980-229b-4a34-9b5a-31ccb893d7d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Write a Python program that checks if a number is even or odd using if-else."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "596a45b6-641a-4da7-bd65-873e2715e200",
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
    "a= int(input(\"enter a number\"))\n",
    "if a%2==0:\n",
    "    print(\"even\")\n",
    "else:\n",
    "    print(\"odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afc04a78-afca-4729-9f9c-225d48225d1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Ask user to enter a string and check if its length is greater than 5. Print accordingly."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "2b06a5bc-7923-410c-879d-aa16af52eac3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter hi\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "less than 5\n"
     ]
    }
   ],
   "source": [
    "a= str(input(\"enter\"))\n",
    "if len(a) >5:\n",
    "    print(a)\n",
    "else:\n",
    "    print(\"less than 5\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b82c376e-280c-47f5-9c9f-1b3f3b4260e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Take marks input from user and print 'Pass' if marks >= 40, else print 'Fail"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "fa0d239f-54b3-4091-9ad2-0ecbd1d09aef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter marks 39\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fail\n"
     ]
    }
   ],
   "source": [
    "marks= int(input(\"enter marks\"))\n",
    "if marks >= 40:\n",
    "    print('Pass')\n",
    "else:\n",
    "    print('Fail')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43f4da9d-3123-48ce-96f4-1f572246f6bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#tell weather acc to month by user"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "505ac946-1baa-4243-bc82-3566107c338d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter month sept\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "autumn\n"
     ]
    }
   ],
   "source": [
    "month= str(input(\"enter month\"))\n",
    "if month in [\"nov\", \"dec\", \"jan\", \"feb\"]:\n",
    "     print(\"winter\")\n",
    "elif month in [ \"march\", \"april\", \"may\", \"june\", \"july\"]:\n",
    "     print(\"summers\")\n",
    "elif month in [\"august\", \"sept\",\"oct\"]:\n",
    "     print(\"autumn\")\n",
    "else :\n",
    "     print(\"wrong input\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4b4f1f1-aa8f-4c69-9d87-7873b1475d93",
   "metadata": {},
   "outputs": [],
   "source": [
    "#modes on transport"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "3680550f-26af-4dd2-a580-0868e12d731e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the mode of transport air\n",
      "enter the vehicle name hot air balloon\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you are dead\n"
     ]
    }
   ],
   "source": [
    "mode=input(\"enter the mode of transport\")\n",
    "vehicle=input(\"enter the vehicle name\")\n",
    "if mode ==\"air\":\n",
    "    if vehicle==\"aeroplane\":\n",
    "        print(\"you are in aeroplane please fasten your seat belt\")\n",
    "    elif vehicle==\"hot air balloon\":\n",
    "        print(\"you are in hot air balloon please stay put \")\n",
    "    else:\n",
    "        print(\"you are dead\")\n",
    "elif mode==\"water\":\n",
    "    if vehicle==\"ship\":\n",
    "        print(\"you are in a ship so please carry vomit bag\")\n",
    "    elif vehicle==\"boat\" :\n",
    "        print(\"you are on a boat dont jump so that you cant drown\")\n",
    "    else:\n",
    "        print(\"you are drowning\")\n",
    "elif mode==\"land\":\n",
    "    if vehicle==\"car\":\n",
    "        print(\"you are in a car so fasten your seatbelt\")\n",
    "    elif vehicle==\"bus\":\n",
    "        print(\"lets go you got company and talk to ticket collector\")\n",
    "    elif vehicle==\"Train\":\n",
    "        print(\"you are on a train travel with ticket and be aware of tc\")\n",
    "    else:\n",
    "        print(\"dont worry take lift\")\n",
    "else:\n",
    "    print(\"how are you going mannnnnn\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f56a1635-b52e-4344-abca-a8ac41cce499",
   "metadata": {},
   "outputs": [],
   "source": [
    "# assignment 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "e967fd60-4ebd-4a92-bb2b-1021bc6e09e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n"
     ]
    }
   ],
   "source": [
    "x = 10\n",
    "if x > 5:\n",
    "    print('A')\n",
    "elif x > 3:\n",
    "    print('B')\n",
    "else:\n",
    "    print('C')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "286e741d-e965-45f7-b9ee-836b4d67eee7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No\n"
     ]
    }
   ],
   "source": [
    "x = 4\n",
    "y = 2\n",
    "if x > 2:\n",
    "    if y > 3:\n",
    "        print('Yes')\n",
    "    else:\n",
    "        print('No')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "a3fd3819-7db5-4553-aab4-e04b94aaa8b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "High\n"
     ]
    }
   ],
   "source": [
    "x = 7\n",
    "if x > 5:\n",
    "    print('High')\n",
    "else:\n",
    "    print('Low')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "f3c0d5ca-4027-400d-b1d3-7f7cdaeea7e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pass\n"
     ]
    }
   ],
   "source": [
    "marks = 45\n",
    "if marks >= 40:\n",
    "    print('Pass')\n",
    "else:\n",
    "    print('Fail')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "927b82ed-a0c3-48c9-a507-00bf40816108",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Three\n"
     ]
    }
   ],
   "source": [
    "x = 3\n",
    "if x == 5:\n",
    "    print('Five')\n",
    "elif x == 3:\n",
    "    print('Three')\n",
    "else:\n",
    "    print('Other')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27181ca4-c991-4b3f-80bd-4f349e84da54",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Write a Python program to check whether a number is positive, negative or zero using if-elif-else."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "cd8473ef-e075-41a8-b96e-3edb2fbdf34a",
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
      "positive\n"
     ]
    }
   ],
   "source": [
    "a= int(input(\"enter a number\"))\n",
    "if a>0:\n",
    "    print(\"positive\")\n",
    "elif a==0:\n",
    "    print(\" no. is zero\")\n",
    "else:\n",
    "    print(\"negative\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5654adfe-f355-41e6-a36a-23f2ccc1b98c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Take user input for age. Print 'Child' if age < 13, 'Teen' if age < 18, 'Adult' otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "54c4dbba-def1-4611-ab1a-7c57426e10e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter age 11\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "child\n"
     ]
    }
   ],
   "source": [
    "age= int(input(\"enter age\"))\n",
    "if age < 13:\n",
    "    print (\"child\")\n",
    "elif age <18:\n",
    "    print(\"teen\")\n",
    "else:\n",
    "    print(\"adult\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fadce763-8797-4b7f-a1b8-fb22572e4498",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create a nested if program to check if a number is even, and if yes, also check if it's greater than 10."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "5315ef13-0d0c-4e9d-9e90-cd8c4bbe3d8d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 30\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yes\n",
      "greater\n"
     ]
    }
   ],
   "source": [
    "a= int(input(\"enter a number\"))\n",
    "if a%2==0:\n",
    "    print(\"yes\")\n",
    "    if a>10:\n",
    "        print(\"greater\")\n",
    "    else:\n",
    "        print(\"smaller\")\n",
    "else: \n",
    "    print(\"no. is odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d0289c1-7ed4-4688-aad8-7752b7b21150",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Write a program to check grades:\n",
    " #>90: A\n",
    " #>75: B\n",
    " #>60: C\n",
    " #Else: Fail"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "e1994fde-721a-407e-b466-d20248cf305c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number 73\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C\n"
     ]
    }
   ],
   "source": [
    "a= int(input(\"enter a number\"))\n",
    "if a>90:\n",
    "    print(\"A\")\n",
    "elif a>75:\n",
    "    print(\"B\")\n",
    "elif a>60:\n",
    "    print(\"C\")\n",
    "else:\n",
    "    print(\"fail\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee4479e7-682b-4494-8b8a-3b261ea50a9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Ask user to input 3 numbers and print the greatest using nested if."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6338d31c-46f7-4eb5-a33e-7572ee7b43d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number:  9\n",
      "Enter second number:  8\n",
      "Enter third number:  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Greatest number is: 9\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"Enter first number: \"))\n",
    "b = int(input(\"Enter second number: \"))\n",
    "c = int(input(\"Enter third number: \"))\n",
    "\n",
    "if a > b:\n",
    "    if a > c:\n",
    "        print(\"Greatest number is:\", a)\n",
    "    else:\n",
    "        print(\"Greatest number is:\", c)\n",
    "else:\n",
    "    if b > c:\n",
    "        print(\"Greatest number is:\", b)\n",
    "    else:\n",
    "        print(\"Greatest number is:\", c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0364df9-6f83-4313-93f1-9973aacda18d",
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
