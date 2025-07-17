{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b37a75ee-f34f-4056-aea0-acf0db53c069",
   "metadata": {},
   "outputs": [],
   "source": [
    "#datatypes(basic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "08cc7d92-44a2-4798-864d-13c0e1259d3a",
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
   "execution_count": 2,
   "id": "d8dc9c78-364c-4e3a-9691-a51e8035d9cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "a=3.891\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "035dc137-3ff3-4672-9cee-de1ec974051f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "a=True\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0e63692a-281b-4fe9-9820-c356b9f2ed88",
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
    "a=3.9922\n",
    "b=int(a)\n",
    "print(type(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8013ec73-9950-4809-ac92-76d2d7a4afdb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "a=6\n",
    "print(type(str(a)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "87fff5fd-fcde-4d5e-9607-1a135576b054",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "a=9\n",
    "print(type(float(a)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2fc34541-43f4-4d35-9d0c-7db9d8245d63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "a=3\n",
    "print(type(str(a)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "dd7700d6-0d9b-4d43-bd37-ce98798e1f41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "a=3\n",
    "print(type(bool(a)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96e8d96c-2815-40d4-a6ab-d933dbca920b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#arthimetic operators"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b03863b-106f-47d2-991e-c2ffbd1ee365",
   "metadata": {},
   "outputs": [],
   "source": [
    "+,-,*,/,%,//,**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "eb898c62-662c-4221-b6a7-19ee1a7375e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "a=3\n",
    "b=4\n",
    "print(a+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7d75b78e-3b98-41bf-af48-ba8d1f055568",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-1\n"
     ]
    }
   ],
   "source": [
    "a=3\n",
    "b=4\n",
    "print(a-b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "520ca1a9-3dd2-43b0-81e2-fb15d3efafbb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.75\n"
     ]
    }
   ],
   "source": [
    "a=3\n",
    "b=4\n",
    "print(a/b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a33a977c-d6e8-4965-8a58-44a95e278ecf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "a=3\n",
    "b=4\n",
    "print(a*b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5438088f-3139-4b4c-ba43-f7803f0c44e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "a=3\n",
    "b=4\n",
    "print(a%b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "52d08953-1a0e-4576-95d5-74e62c6a241a",
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
    "a=3\n",
    "b=4\n",
    "print(a**b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "92df6014-2f14-41e4-9386-11e9d01af09b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "a=3\n",
    "b=4\n",
    "print(a//b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9553cab2-f69d-4fbf-a7dc-78e49ed6146f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the number 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"Enter the number\"))\n",
    "b=4\n",
    "print(a+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "ab75ba06-c748-4351-b1c8-9fe4400dc9e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the number 45\n",
      "Enter the number 32\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "77\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"Enter the number\"))\n",
    "b=int(input(\"Enter the number\"))\n",
    "print(a+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7f1ca1a-2224-4550-a200-9bb4f2ef8486",
   "metadata": {},
   "outputs": [],
   "source": [
    "#comparison operators"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bfc6b5fe-6f54-450b-8595-58e5e07e3b2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "<,>,<=,>=,=="
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "30324b1e-72f0-4e52-87c0-5fe3c4454df3",
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
    "a=10\n",
    "b=15\n",
    "print(a>b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "523bba4b-169b-415a-af32-878d6c9de38f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=15\n",
    "print(a<b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "6d567dbd-e38f-42ec-b69f-035e9462d7bc",
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
    "a=10\n",
    "b=15\n",
    "print(a==b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "32b5ac4a-204a-4561-86da-b2b24b88936e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=15\n",
    "print(a<=b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "9a720311-de41-4763-8a8c-5f609326bcf8",
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
    "a=10\n",
    "b=15\n",
    "print(a>=b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "5d495d37-759d-42cc-8270-f474a973effa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the number 5\n",
      "Enter the number 6\n",
      "Enter the number 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "18\n",
      "13.333333333333334\n"
     ]
    }
   ],
   "source": [
    "x=int(input(\"Enter the number\"))\n",
    "y=int(input(\"Enter the number\"))\n",
    "z=int(input(\"Enter the number\"))\n",
    "print(x+y+z)\n",
    "print(x+y+z/3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "2f8768de-c7f7-4d2b-97f1-8cace2e396c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the number 4\n",
      "Enter the number 5\n",
      "Enter the number 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16\n",
      "5.333333333333333\n",
      "False\n",
      "3.2\n"
     ]
    }
   ],
   "source": [
    "#Question\n",
    "x=int(input(\"Enter the number\"))\n",
    "y=int(input(\"Enter the number\"))\n",
    "z=int(input(\"Enter the number\"))\n",
    "b=(x+y+z)\n",
    "c=(b/3)\n",
    "print(b)\n",
    "print(c)\n",
    "print(c>50)\n",
    "print(b/5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af2df05b-1d16-4d7b-98ba-2ed93c55f265",
   "metadata": {},
   "outputs": [],
   "source": [
    "#logical operator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ecaf1c50-303b-4df3-a285-58277bcbdfa0",
   "metadata": {},
   "outputs": [],
   "source": [
    "and,or,not"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "b3ea995b-02d9-4724-8b32-073b968b2097",
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
    "a=10\n",
    "b=10\n",
    "print(a>b and a==b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "37bcb9b7-a889-4b8d-b742-bf46f7f53b11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=10\n",
    "print(a>b or a==b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "a3114230-7e4b-490a-b6c9-67f91a78ed0c",
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
    "a=10\n",
    "b=10\n",
    "print(not( a==b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c75d2ad8-4ae6-4c19-bb74-f6c7be248ac7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Membership operator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cfa06c4a-279c-449d-90f3-4cf6e3f6640b",
   "metadata": {},
   "outputs": [],
   "source": [
    "in, not in"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "3f34a909-04b4-4c8e-9a03-2d2bb7f02474",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "3\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "a=[2,4,3,5]\n",
    "for x in a:\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "c9e6a9a8-8d84-4638-8a45-b5958b2be760",
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
    "a=[2,4,3,5]\n",
    "b=[2,6,3,9]\n",
    "print(a in b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "dc181720-ba2d-42c4-83b5-5bc88ea88bd5",
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
    "a=[2,4,3,5]\n",
    "b=[2,4,3,5]\n",
    "print(a in b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0f591cbd-89e8-4a2c-99ea-21464c83898f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a=\"python is imp\"\n",
    "print(\"is\" in a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "a332ad12-7071-4ffc-912e-31c0440d9f15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a=\"python is very imp\"\n",
    "print(\"very\" in a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "82ef1930-cb53-43e9-98eb-ba26f71cf573",
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
    "a=\"python is imp\"\n",
    "print(\"very\" in a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "c6535a62-28d4-4b72-8118-5ca2d2e36526",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the number 4\n",
      "Enter the number 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n",
      "20\n",
      "False\n",
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "#Question\n",
    "a=int(input(\"Enter the number\"))\n",
    "b=int(input(\"Enter the number\"))\n",
    "x=(a+b)\n",
    "y=(a*b)\n",
    "print(x)\n",
    "print(y)\n",
    "print(y==x)\n",
    "print(x>y)\n",
    "w=[10,20,30,40,50]\n",
    "print(3 in w)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b7cc2a8-bd35-40a0-aa0e-f909213b3821",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Identity operators"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "6c9f55a8-9029-4191-993d-505aae604919",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a=6\n",
    "b=7\n",
    "print(a is not b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "5fef4296-5083-452b-8277-2f8f09ebd60a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "a=6\n",
    "b=6\n",
    "print(a is b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54e10742-6d68-4b1d-a287-70f722db8aba",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Bitwise Operators"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "a41fcff2-f934-4577-8abc-c3a245d08f0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "b=3\n",
    "print(a & b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "8e98f990-aab3-41f9-a3e4-e98d8f4a3988",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "b=3\n",
    "print(a | b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc290e3c-2caf-419c-8403-ce32730f6042",
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
