{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import pandas_datareader as pdr\n",
    "import datetime \n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2020-06-08\n",
      "2019-01-25\n"
     ]
    }
   ],
   "source": [
    "current_date=datetime.date.today()\n",
    "print(current_date)\n",
    "\n",
    "period= datetime.timedelta(days=500)\n",
    "\n",
    "start_date= current_date-period\n",
    "print(start_date)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "stock = pdr.get_data_yahoo('BA', \n",
    "                          start=start_date, \n",
    "                          end=current_date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2019-01-24</td>\n",
       "      <td>363.179993</td>\n",
       "      <td>356.899994</td>\n",
       "      <td>358.910004</td>\n",
       "      <td>358.269989</td>\n",
       "      <td>2801300.0</td>\n",
       "      <td>348.129822</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-01-25</td>\n",
       "      <td>366.940002</td>\n",
       "      <td>360.329987</td>\n",
       "      <td>362.489990</td>\n",
       "      <td>364.200012</td>\n",
       "      <td>3185600.0</td>\n",
       "      <td>353.891968</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-01-28</td>\n",
       "      <td>363.170013</td>\n",
       "      <td>357.500000</td>\n",
       "      <td>360.649994</td>\n",
       "      <td>362.970001</td>\n",
       "      <td>3128900.0</td>\n",
       "      <td>352.696777</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-01-29</td>\n",
       "      <td>367.779999</td>\n",
       "      <td>362.410004</td>\n",
       "      <td>363.070007</td>\n",
       "      <td>364.910004</td>\n",
       "      <td>3202700.0</td>\n",
       "      <td>354.581909</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-01-30</td>\n",
       "      <td>391.970001</td>\n",
       "      <td>380.500000</td>\n",
       "      <td>387.399994</td>\n",
       "      <td>387.720001</td>\n",
       "      <td>12705300.0</td>\n",
       "      <td>376.746277</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  High         Low        Open       Close      Volume  \\\n",
       "Date                                                                     \n",
       "2019-01-24  363.179993  356.899994  358.910004  358.269989   2801300.0   \n",
       "2019-01-25  366.940002  360.329987  362.489990  364.200012   3185600.0   \n",
       "2019-01-28  363.170013  357.500000  360.649994  362.970001   3128900.0   \n",
       "2019-01-29  367.779999  362.410004  363.070007  364.910004   3202700.0   \n",
       "2019-01-30  391.970001  380.500000  387.399994  387.720001  12705300.0   \n",
       "\n",
       "             Adj Close  \n",
       "Date                    \n",
       "2019-01-24  348.129822  \n",
       "2019-01-25  353.891968  \n",
       "2019-01-28  352.696777  \n",
       "2019-01-29  354.581909  \n",
       "2019-01-30  376.746277  "
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Return first rows of `stock`\n",
    "stock.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2020-06-02</td>\n",
       "      <td>155.850006</td>\n",
       "      <td>151.809998</td>\n",
       "      <td>154.000000</td>\n",
       "      <td>153.309998</td>\n",
       "      <td>24780500.0</td>\n",
       "      <td>153.309998</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-06-03</td>\n",
       "      <td>173.779999</td>\n",
       "      <td>155.490005</td>\n",
       "      <td>157.100006</td>\n",
       "      <td>173.160004</td>\n",
       "      <td>66486400.0</td>\n",
       "      <td>173.160004</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-06-04</td>\n",
       "      <td>188.600006</td>\n",
       "      <td>177.399994</td>\n",
       "      <td>181.279999</td>\n",
       "      <td>184.300003</td>\n",
       "      <td>67155600.0</td>\n",
       "      <td>184.300003</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-06-05</td>\n",
       "      <td>218.789993</td>\n",
       "      <td>197.360001</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.429993</td>\n",
       "      <td>99604800.0</td>\n",
       "      <td>205.429993</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-06-08</td>\n",
       "      <td>234.130005</td>\n",
       "      <td>219.000000</td>\n",
       "      <td>222.940002</td>\n",
       "      <td>232.660004</td>\n",
       "      <td>40179459.0</td>\n",
       "      <td>232.660004</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  High         Low        Open       Close      Volume  \\\n",
       "Date                                                                     \n",
       "2020-06-02  155.850006  151.809998  154.000000  153.309998  24780500.0   \n",
       "2020-06-03  173.779999  155.490005  157.100006  173.160004  66486400.0   \n",
       "2020-06-04  188.600006  177.399994  181.279999  184.300003  67155600.0   \n",
       "2020-06-05  218.789993  197.360001  205.000000  205.429993  99604800.0   \n",
       "2020-06-08  234.130005  219.000000  222.940002  232.660004  40179459.0   \n",
       "\n",
       "             Adj Close  \n",
       "Date                    \n",
       "2020-06-02  153.309998  \n",
       "2020-06-03  173.160004  \n",
       "2020-06-04  184.300003  \n",
       "2020-06-05  205.429993  \n",
       "2020-06-08  232.660004  "
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Return last rows of `stock`\n",
    "stock.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>count</td>\n",
       "      <td>346.000000</td>\n",
       "      <td>346.000000</td>\n",
       "      <td>346.000000</td>\n",
       "      <td>346.000000</td>\n",
       "      <td>3.460000e+02</td>\n",
       "      <td>346.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>mean</td>\n",
       "      <td>323.718179</td>\n",
       "      <td>314.960606</td>\n",
       "      <td>319.560290</td>\n",
       "      <td>319.230086</td>\n",
       "      <td>1.183679e+07</td>\n",
       "      <td>314.936571</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>std</td>\n",
       "      <td>87.097474</td>\n",
       "      <td>88.844985</td>\n",
       "      <td>87.580042</td>\n",
       "      <td>88.394683</td>\n",
       "      <td>1.481661e+07</td>\n",
       "      <td>85.875830</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>min</td>\n",
       "      <td>103.570000</td>\n",
       "      <td>89.000000</td>\n",
       "      <td>98.750000</td>\n",
       "      <td>95.010002</td>\n",
       "      <td>1.390900e+06</td>\n",
       "      <td>95.010002</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>25%</td>\n",
       "      <td>328.437508</td>\n",
       "      <td>319.764992</td>\n",
       "      <td>323.337502</td>\n",
       "      <td>324.552498</td>\n",
       "      <td>3.691850e+06</td>\n",
       "      <td>322.632942</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>50%</td>\n",
       "      <td>354.625000</td>\n",
       "      <td>347.079987</td>\n",
       "      <td>350.184998</td>\n",
       "      <td>351.044998</td>\n",
       "      <td>5.136100e+06</td>\n",
       "      <td>346.501541</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>75%</td>\n",
       "      <td>376.029991</td>\n",
       "      <td>368.605011</td>\n",
       "      <td>372.377510</td>\n",
       "      <td>373.115005</td>\n",
       "      <td>1.104935e+07</td>\n",
       "      <td>366.624107</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>max</td>\n",
       "      <td>446.010010</td>\n",
       "      <td>440.190002</td>\n",
       "      <td>446.010010</td>\n",
       "      <td>440.619995</td>\n",
       "      <td>9.960480e+07</td>\n",
       "      <td>430.299988</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             High         Low        Open       Close        Volume  \\\n",
       "count  346.000000  346.000000  346.000000  346.000000  3.460000e+02   \n",
       "mean   323.718179  314.960606  319.560290  319.230086  1.183679e+07   \n",
       "std     87.097474   88.844985   87.580042   88.394683  1.481661e+07   \n",
       "min    103.570000   89.000000   98.750000   95.010002  1.390900e+06   \n",
       "25%    328.437508  319.764992  323.337502  324.552498  3.691850e+06   \n",
       "50%    354.625000  347.079987  350.184998  351.044998  5.136100e+06   \n",
       "75%    376.029991  368.605011  372.377510  373.115005  1.104935e+07   \n",
       "max    446.010010  440.190002  446.010010  440.619995  9.960480e+07   \n",
       "\n",
       "        Adj Close  \n",
       "count  346.000000  \n",
       "mean   314.936571  \n",
       "std     85.875830  \n",
       "min     95.010002  \n",
       "25%    322.632942  \n",
       "50%    346.501541  \n",
       "75%    366.624107  \n",
       "max    430.299988  "
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Describe `stock`\n",
    "stock.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2020-06-02</td>\n",
       "      <td>155.850006</td>\n",
       "      <td>151.809998</td>\n",
       "      <td>154.000000</td>\n",
       "      <td>153.309998</td>\n",
       "      <td>24780500.0</td>\n",
       "      <td>153.309998</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-06-03</td>\n",
       "      <td>173.779999</td>\n",
       "      <td>155.490005</td>\n",
       "      <td>157.100006</td>\n",
       "      <td>173.160004</td>\n",
       "      <td>66486400.0</td>\n",
       "      <td>173.160004</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-06-04</td>\n",
       "      <td>188.600006</td>\n",
       "      <td>177.399994</td>\n",
       "      <td>181.279999</td>\n",
       "      <td>184.300003</td>\n",
       "      <td>67155600.0</td>\n",
       "      <td>184.300003</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-06-05</td>\n",
       "      <td>218.789993</td>\n",
       "      <td>197.360001</td>\n",
       "      <td>205.000000</td>\n",
       "      <td>205.429993</td>\n",
       "      <td>99604800.0</td>\n",
       "      <td>205.429993</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-06-08</td>\n",
       "      <td>234.130005</td>\n",
       "      <td>219.000000</td>\n",
       "      <td>222.940002</td>\n",
       "      <td>232.660004</td>\n",
       "      <td>40179459.0</td>\n",
       "      <td>232.660004</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  High         Low        Open       Close      Volume  \\\n",
       "Date                                                                     \n",
       "2020-06-02  155.850006  151.809998  154.000000  153.309998  24780500.0   \n",
       "2020-06-03  173.779999  155.490005  157.100006  173.160004  66486400.0   \n",
       "2020-06-04  188.600006  177.399994  181.279999  184.300003  67155600.0   \n",
       "2020-06-05  218.789993  197.360001  205.000000  205.429993  99604800.0   \n",
       "2020-06-08  234.130005  219.000000  222.940002  232.660004  40179459.0   \n",
       "\n",
       "             Adj Close  \n",
       "Date                    \n",
       "2020-06-02  153.309998  \n",
       "2020-06-03  173.160004  \n",
       "2020-06-04  184.300003  \n",
       "2020-06-05  205.429993  \n",
       "2020-06-08  232.660004  "
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stock.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DatetimeIndex(['2019-01-24', '2019-01-25', '2019-01-28', '2019-01-29',\n",
       "               '2019-01-30', '2019-01-31', '2019-02-01', '2019-02-04',\n",
       "               '2019-02-05', '2019-02-06',\n",
       "               ...\n",
       "               '2020-05-26', '2020-05-27', '2020-05-28', '2020-05-29',\n",
       "               '2020-06-01', '2020-06-02', '2020-06-03', '2020-06-04',\n",
       "               '2020-06-05', '2020-06-08'],\n",
       "              dtype='datetime64[ns]', name='Date', length=346, freq=None)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stock.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'], dtype='object')"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stock.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date\n",
      "2020-05-26    144.729996\n",
      "2020-05-27    149.520004\n",
      "2020-05-28    149.820007\n",
      "2020-05-29    145.850006\n",
      "2020-06-01    151.389999\n",
      "2020-06-02    153.309998\n",
      "2020-06-03    173.160004\n",
      "2020-06-04    184.300003\n",
      "2020-06-05    205.429993\n",
      "2020-06-08    232.660004\n",
      "Name: Close, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "ts = stock['Close'][-10:]\n",
    "print(ts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.series.Series"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(ts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                  High         Low        Open       Close      Volume  \\\n",
      "Date                                                                     \n",
      "2019-08-15  328.070007  319.549988  323.000000  328.000000   4721800.0   \n",
      "2019-11-13  366.619995  361.119995  361.869995  362.500000   3453700.0   \n",
      "2019-10-04  376.130005  371.720001  372.250000  375.700012   2008400.0   \n",
      "2019-09-24  381.890015  375.309998  379.540009  381.649994   3533300.0   \n",
      "2020-01-29  327.179993  319.140015  324.350006  322.019989  12454700.0   \n",
      "2020-01-07  344.190002  330.709991  334.260010  337.279999   9898600.0   \n",
      "2020-01-31  321.929993  316.989990  321.750000  318.269989   4999600.0   \n",
      "2019-08-08  336.429993  328.859985  331.299988  336.350006   3673000.0   \n",
      "2020-01-09  341.730011  332.049988  334.950012  336.339996   8175600.0   \n",
      "2020-05-26  145.910004  142.610001  145.210007  144.729996  30338300.0   \n",
      "2019-06-11  355.470001  348.130005  355.420013  349.329987   2702700.0   \n",
      "2019-11-01  345.190002  339.500000  340.589996  345.190002   3538200.0   \n",
      "2020-05-27  149.649994  141.240005  149.139999  149.520004  32799900.0   \n",
      "2020-04-30  144.649994  132.309998  137.669998  141.020004  37732800.0   \n",
      "2020-04-21  141.899994  135.449997  139.009995  136.330002  27043800.0   \n",
      "2019-03-15  385.709991  366.450012  370.880005  378.989990  26697700.0   \n",
      "2019-02-28  441.420013  437.079987  438.700012  439.959991   5063100.0   \n",
      "2019-03-05  433.850006  428.640015  431.040009  430.119995   2844300.0   \n",
      "2020-01-22  312.839996  302.720001  309.820007  309.000000  18792600.0   \n",
      "2019-10-01  382.850006  374.630005  381.700012  374.940002   2943800.0   \n",
      "\n",
      "             Adj Close  \n",
      "Date                    \n",
      "2019-08-15  324.168243  \n",
      "2019-11-13  360.355988  \n",
      "2019-10-04  371.311035  \n",
      "2019-09-24  377.191498  \n",
      "2020-01-29  320.115387  \n",
      "2020-01-07  335.285156  \n",
      "2020-01-31  316.387573  \n",
      "2019-08-08  332.420715  \n",
      "2020-01-09  334.350708  \n",
      "2020-05-26  144.729996  \n",
      "2019-06-11  343.108063  \n",
      "2019-11-01  341.157440  \n",
      "2020-05-27  149.520004  \n",
      "2020-04-30  141.020004  \n",
      "2020-04-21  136.330002  \n",
      "2019-03-15  370.113434  \n",
      "2019-02-28  429.655426  \n",
      "2019-03-05  420.045898  \n",
      "2020-01-22  307.172424  \n",
      "2019-10-01  370.559875  \n"
     ]
    }
   ],
   "source": [
    "sample= stock.sample(20)\n",
    "print(sample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                  High         Low        Open       Close        Volume  \\\n",
      "Date                                                                       \n",
      "2019-01-31  373.671666  366.619995  369.946665  370.615000  5.317050e+06   \n",
      "2019-02-28  416.693157  410.242629  412.504211  414.595787  4.046453e+06   \n",
      "2019-03-31  396.023333  384.460477  390.220953  390.737620  1.222711e+07   \n",
      "2019-04-30  383.236190  376.097620  379.292383  379.660475  6.733733e+06   \n",
      "2019-05-31  359.304091  351.965454  355.725909  355.738635  4.672886e+06   \n",
      "2019-06-30  361.692499  354.167999  358.117001  358.659999  4.041470e+06   \n",
      "2019-07-31  361.281819  353.845000  357.979545  357.454540  4.735809e+06   \n",
      "2019-08-31  344.755001  336.792729  340.447728  341.082729  4.350559e+06   \n",
      "2019-09-30  378.212500  371.175497  374.488000  375.462003  3.919915e+06   \n",
      "2019-10-31  363.836521  355.996954  360.430003  359.127825  4.882070e+06   \n",
      "2019-11-30  366.720996  359.830496  362.849998  363.725000  4.336280e+06   \n",
      "2019-12-31  343.607144  336.685239  340.628572  339.137618  6.075300e+06   \n",
      "2020-01-31  329.884288  321.860953  326.113334  325.867141  8.645990e+06   \n",
      "2020-02-29  331.013158  322.677898  327.349474  326.097896  6.225953e+06   \n",
      "2020-03-31  190.251819  170.369089  183.179090  178.744089  3.380656e+07   \n",
      "2020-04-30  146.080000  134.798571  141.236191  138.653809  3.900821e+07   \n",
      "2020-05-31  136.704500  129.839500  133.878502  132.899001  3.059656e+07   \n",
      "2020-06-30  187.450002  174.268333  177.628334  183.375000  5.422234e+07   \n",
      "\n",
      "             Adj Close  \n",
      "Date                    \n",
      "2019-01-31  360.125407  \n",
      "2019-02-28  404.472746  \n",
      "2019-03-31  381.585932  \n",
      "2019-04-30  370.768226  \n",
      "2019-05-31  348.837008  \n",
      "2019-06-30  352.271889  \n",
      "2019-07-31  351.087903  \n",
      "2019-08-31  336.633258  \n",
      "2019-09-30  371.075786  \n",
      "2019-10-31  354.932434  \n",
      "2019-11-30  361.167482  \n",
      "2019-12-31  337.131787  \n",
      "2020-01-31  323.939796  \n",
      "2020-02-29  325.264197  \n",
      "2020-03-31  178.744089  \n",
      "2020-04-30  138.653809  \n",
      "2020-05-31  132.899001  \n",
      "2020-06-30  183.375000  \n"
     ]
    }
   ],
   "source": [
    "monthly_stock = stock.resample('M').mean()\n",
    "print(monthly_stock)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "stock['Close'].plot(grid=True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               Close\n",
      "Date                \n",
      "2019-01-24  0.000000\n",
      "2019-01-25  0.016416\n",
      "2019-01-28 -0.003383\n",
      "2019-01-29  0.005331\n",
      "2019-01-30  0.060633\n",
      "...              ...\n",
      "2020-06-02  0.012603\n",
      "2020-06-03  0.121754\n",
      "2020-06-04  0.062349\n",
      "2020-06-05  0.108540\n",
      "2020-06-08  0.124473\n",
      "\n",
      "[346 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "# Assign `Adj Close` to `daily_close`\n",
    "daily_close = stock[['Close']]\n",
    "\n",
    "# Daily returns\n",
    "daily_pct_change = daily_close.pct_change()\n",
    "\n",
    "# Replace NA values with 0\n",
    "daily_pct_change.fillna(0, inplace=True)\n",
    "\n",
    "# Daily log returns\n",
    "daily_log_returns = np.log(daily_close.pct_change()+1)\n",
    "\n",
    "#replace NA value with 0\n",
    "daily_log_returns.fillna(0, inplace=True)\n",
    "\n",
    "# Print daily log returns\n",
    "print(daily_log_returns)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x125562710>"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "daily_log_returns.plot(grid=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2019-01-31</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-02-28</td>\n",
       "      <td>0.134785</td>\n",
       "      <td>0.143949</td>\n",
       "      <td>0.133123</td>\n",
       "      <td>0.140916</td>\n",
       "      <td>-0.263924</td>\n",
       "      <td>0.146648</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-03-29</td>\n",
       "      <td>-0.134203</td>\n",
       "      <td>-0.142628</td>\n",
       "      <td>-0.141737</td>\n",
       "      <td>-0.133058</td>\n",
       "      <td>0.519761</td>\n",
       "      <td>-0.133057</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-30</td>\n",
       "      <td>-0.002721</td>\n",
       "      <td>0.000827</td>\n",
       "      <td>0.007915</td>\n",
       "      <td>-0.009779</td>\n",
       "      <td>-0.514887</td>\n",
       "      <td>-0.009779</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-05-31</td>\n",
       "      <td>-0.092591</td>\n",
       "      <td>-0.089828</td>\n",
       "      <td>-0.088669</td>\n",
       "      <td>-0.095528</td>\n",
       "      <td>-0.138020</td>\n",
       "      <td>-0.090332</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-06-28</td>\n",
       "      <td>0.058927</td>\n",
       "      <td>0.059204</td>\n",
       "      <td>0.052248</td>\n",
       "      <td>0.065572</td>\n",
       "      <td>0.472246</td>\n",
       "      <td>0.065572</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-07-31</td>\n",
       "      <td>-0.040794</td>\n",
       "      <td>-0.056753</td>\n",
       "      <td>-0.042399</td>\n",
       "      <td>-0.062718</td>\n",
       "      <td>0.101877</td>\n",
       "      <td>-0.062718</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-08-30</td>\n",
       "      <td>0.042927</td>\n",
       "      <td>0.062601</td>\n",
       "      <td>0.045568</td>\n",
       "      <td>0.067149</td>\n",
       "      <td>-0.397092</td>\n",
       "      <td>0.073808</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-09-30</td>\n",
       "      <td>0.047493</td>\n",
       "      <td>0.039432</td>\n",
       "      <td>0.051129</td>\n",
       "      <td>0.044989</td>\n",
       "      <td>0.011535</td>\n",
       "      <td>0.044989</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-10-31</td>\n",
       "      <td>-0.098262</td>\n",
       "      <td>-0.098861</td>\n",
       "      <td>-0.100000</td>\n",
       "      <td>-0.106605</td>\n",
       "      <td>0.215217</td>\n",
       "      <td>-0.106605</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-11-29</td>\n",
       "      <td>0.064266</td>\n",
       "      <td>0.078745</td>\n",
       "      <td>0.066144</td>\n",
       "      <td>0.077285</td>\n",
       "      <td>-0.640446</td>\n",
       "      <td>0.083572</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-12-31</td>\n",
       "      <td>-0.113304</td>\n",
       "      <td>-0.117046</td>\n",
       "      <td>-0.114531</td>\n",
       "      <td>-0.110383</td>\n",
       "      <td>2.565174</td>\n",
       "      <td>-0.110383</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-01-31</td>\n",
       "      <td>-0.014208</td>\n",
       "      <td>-0.019578</td>\n",
       "      <td>-0.011247</td>\n",
       "      <td>-0.022992</td>\n",
       "      <td>0.008228</td>\n",
       "      <td>-0.022993</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-02-28</td>\n",
       "      <td>-0.121362</td>\n",
       "      <td>-0.149500</td>\n",
       "      <td>-0.135758</td>\n",
       "      <td>-0.135608</td>\n",
       "      <td>2.075266</td>\n",
       "      <td>-0.130465</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-03-31</td>\n",
       "      <td>-0.432087</td>\n",
       "      <td>-0.447329</td>\n",
       "      <td>-0.442586</td>\n",
       "      <td>-0.457890</td>\n",
       "      <td>0.948215</td>\n",
       "      <td>-0.457890</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-04-30</td>\n",
       "      <td>-0.099539</td>\n",
       "      <td>-0.112013</td>\n",
       "      <td>-0.111806</td>\n",
       "      <td>-0.054445</td>\n",
       "      <td>0.259692</td>\n",
       "      <td>-0.054445</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-05-29</td>\n",
       "      <td>0.050812</td>\n",
       "      <td>0.080342</td>\n",
       "      <td>0.055422</td>\n",
       "      <td>0.034250</td>\n",
       "      <td>-0.101442</td>\n",
       "      <td>0.034250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-06-30</td>\n",
       "      <td>0.540329</td>\n",
       "      <td>0.532111</td>\n",
       "      <td>0.534343</td>\n",
       "      <td>0.595201</td>\n",
       "      <td>0.185056</td>\n",
       "      <td>0.595201</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                High       Low      Open     Close    Volume  Adj Close\n",
       "Date                                                                   \n",
       "2019-01-31       NaN       NaN       NaN       NaN       NaN        NaN\n",
       "2019-02-28  0.134785  0.143949  0.133123  0.140916 -0.263924   0.146648\n",
       "2019-03-29 -0.134203 -0.142628 -0.141737 -0.133058  0.519761  -0.133057\n",
       "2019-04-30 -0.002721  0.000827  0.007915 -0.009779 -0.514887  -0.009779\n",
       "2019-05-31 -0.092591 -0.089828 -0.088669 -0.095528 -0.138020  -0.090332\n",
       "2019-06-28  0.058927  0.059204  0.052248  0.065572  0.472246   0.065572\n",
       "2019-07-31 -0.040794 -0.056753 -0.042399 -0.062718  0.101877  -0.062718\n",
       "2019-08-30  0.042927  0.062601  0.045568  0.067149 -0.397092   0.073808\n",
       "2019-09-30  0.047493  0.039432  0.051129  0.044989  0.011535   0.044989\n",
       "2019-10-31 -0.098262 -0.098861 -0.100000 -0.106605  0.215217  -0.106605\n",
       "2019-11-29  0.064266  0.078745  0.066144  0.077285 -0.640446   0.083572\n",
       "2019-12-31 -0.113304 -0.117046 -0.114531 -0.110383  2.565174  -0.110383\n",
       "2020-01-31 -0.014208 -0.019578 -0.011247 -0.022992  0.008228  -0.022993\n",
       "2020-02-28 -0.121362 -0.149500 -0.135758 -0.135608  2.075266  -0.130465\n",
       "2020-03-31 -0.432087 -0.447329 -0.442586 -0.457890  0.948215  -0.457890\n",
       "2020-04-30 -0.099539 -0.112013 -0.111806 -0.054445  0.259692  -0.054445\n",
       "2020-05-29  0.050812  0.080342  0.055422  0.034250 -0.101442   0.034250\n",
       "2020-06-30  0.540329  0.532111  0.534343  0.595201  0.185056   0.595201"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Resample `aapl` to business months, take last observation as value \n",
    "monthly = stock.resample('BM').apply(lambda x: x[-1])\n",
    "\n",
    "# Calculate the monthly percentage change\n",
    "monthly.pct_change()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2019-01-31</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-05-31</td>\n",
       "      <td>0.037774</td>\n",
       "      <td>0.035496</td>\n",
       "      <td>0.036402</td>\n",
       "      <td>0.036438</td>\n",
       "      <td>0.309413</td>\n",
       "      <td>0.042436</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-09-30</td>\n",
       "      <td>-0.068864</td>\n",
       "      <td>-0.068622</td>\n",
       "      <td>-0.067975</td>\n",
       "      <td>-0.068672</td>\n",
       "      <td>-0.385924</td>\n",
       "      <td>-0.061439</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-01-31</td>\n",
       "      <td>-0.027565</td>\n",
       "      <td>-0.027965</td>\n",
       "      <td>-0.027206</td>\n",
       "      <td>-0.029876</td>\n",
       "      <td>0.398338</td>\n",
       "      <td>-0.022701</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-05-31</td>\n",
       "      <td>-0.434696</td>\n",
       "      <td>-0.456885</td>\n",
       "      <td>-0.442456</td>\n",
       "      <td>-0.448390</td>\n",
       "      <td>3.677730</td>\n",
       "      <td>-0.444611</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2020-09-30</td>\n",
       "      <td>-0.055642</td>\n",
       "      <td>-0.066413</td>\n",
       "      <td>-0.083532</td>\n",
       "      <td>-0.042120</td>\n",
       "      <td>0.938926</td>\n",
       "      <td>-0.041152</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                High       Low      Open     Close    Volume  Adj Close\n",
       "Date                                                                   \n",
       "2019-01-31       NaN       NaN       NaN       NaN       NaN        NaN\n",
       "2019-05-31  0.037774  0.035496  0.036402  0.036438  0.309413   0.042436\n",
       "2019-09-30 -0.068864 -0.068622 -0.067975 -0.068672 -0.385924  -0.061439\n",
       "2020-01-31 -0.027565 -0.027965 -0.027206 -0.029876  0.398338  -0.022701\n",
       "2020-05-31 -0.434696 -0.456885 -0.442456 -0.448390  3.677730  -0.444611\n",
       "2020-09-30 -0.055642 -0.066413 -0.083532 -0.042120  0.938926  -0.041152"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Resample `aapl` to quarters, take the mean as value per quarter\n",
    "quarter = stock.resample(\"4M\").mean()\n",
    "\n",
    "# Calculate the quarterly percentage change\n",
    "quarter.pct_change()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               Close\n",
      "Date                \n",
      "2019-01-24       NaN\n",
      "2019-01-25  0.016552\n",
      "2019-01-28 -0.003377\n",
      "2019-01-29  0.005345\n",
      "2019-01-30  0.062509\n",
      "...              ...\n",
      "2020-06-02  0.012682\n",
      "2020-06-03  0.129476\n",
      "2020-06-04  0.064334\n",
      "2020-06-05  0.114650\n",
      "2020-06-08  0.132551\n",
      "\n",
      "[346 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "# Daily returns\n",
    "daily_pct_change = daily_close / daily_close.shift(1) - 1\n",
    "\n",
    "# Print `daily_pct_change`\n",
    "print(daily_pct_change)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            Close\n",
      "count  345.000000\n",
      "mean    -0.000317\n",
      "std      0.043184\n",
      "min     -0.238484\n",
      "25%     -0.013341\n",
      "50%     -0.000240\n",
      "75%      0.012708\n",
      "max      0.243186\n"
     ]
    }
   ],
   "source": [
    "daily_pct_change.hist(bins=50)\n",
    "\n",
    "# Show the plot\n",
    "plt.show()\n",
    "\n",
    "# Pull up summary statistics\n",
    "print(daily_pct_change.describe())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               Close\n",
      "Date                \n",
      "2019-01-24       NaN\n",
      "2019-01-25  1.016552\n",
      "2019-01-28  1.013119\n",
      "2019-01-29  1.018534\n",
      "2019-01-30  1.082201\n",
      "...              ...\n",
      "2020-06-02  0.427917\n",
      "2020-06-03  0.483323\n",
      "2020-06-04  0.514417\n",
      "2020-06-05  0.573394\n",
      "2020-06-08  0.649399\n",
      "\n",
      "[346 rows x 1 columns]\n",
      "               Close\n",
      "Date                \n",
      "2019-01-31  1.041349\n",
      "2019-05-31  1.072151\n",
      "2019-09-30  0.998524\n",
      "2020-01-31  0.968692\n",
      "2020-05-31  0.534341\n",
      "2020-09-30  0.511835\n"
     ]
    }
   ],
   "source": [
    "# Calculate the cumulative daily returns\n",
    "cum_daily_return = (1 + daily_pct_change).cumprod()\n",
    "cum_monthly_return = cum_daily_return.resample(\"4M\").mean()\n",
    "\n",
    "# Print `cum_daily_return`\n",
    "print(cum_daily_return)\n",
    "print(cum_monthly_return)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot the cumulative daily returns\n",
    "cum_daily_return.plot(figsize=(12,8))\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date\n",
      "2020-05-26    135.648500\n",
      "2020-05-27    135.579500\n",
      "2020-05-28    135.596500\n",
      "2020-05-29    135.975251\n",
      "2020-06-01    136.678251\n",
      "2020-06-02    137.398001\n",
      "2020-06-03    138.007751\n",
      "2020-06-04    139.075751\n",
      "2020-06-05    140.539751\n",
      "2020-06-08    142.560251\n",
      "Name: Close, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Isolate the adjusted closing prices \n",
    "close_px = stock['Close']\n",
    "\n",
    "# Calculate the moving average\n",
    "moving_avg = close_px.rolling(window=40).mean()\n",
    "\n",
    "# Inspect the result\n",
    "print(moving_avg[-10:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Short moving window rolling mean\n",
    "stock['10'] = close_px.rolling(window=10).mean()\n",
    "\n",
    "# Long moving window rolling mean\n",
    "stock['20'] = close_px.rolling(window=20).mean()\n",
    "\n",
    "# Plot the adjusted closing price, the short and long windows of rolling means\n",
    "stock[['Close', '10', '20']].plot()\n",
    "\n",
    "# Show plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Define the minumum of periods to consider \n",
    "min_periods = 10\n",
    "\n",
    "# Calculate the volatility\n",
    "vol = daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods) \n",
    "\n",
    "# Plot the volatility\n",
    "vol.plot(figsize=(8, 5))\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            signal  short_mavg   long_mavg  positions\n",
      "Date                                                 \n",
      "2019-01-24     0.0  358.269989  358.269989        NaN\n",
      "2019-01-25     0.0  361.235001  361.235001        0.0\n",
      "2019-01-28     0.0  361.813334  361.813334        0.0\n",
      "2019-01-29     0.0  362.587502  362.587502        0.0\n",
      "2019-01-30     0.0  367.614001  367.614001        0.0\n",
      "...            ...         ...         ...        ...\n",
      "2020-06-02     0.0  137.398001  211.773799        0.0\n",
      "2020-06-03     0.0  138.007751  210.142000        0.0\n",
      "2020-06-04     0.0  139.075751  208.685799        0.0\n",
      "2020-06-05     0.0  140.539751  207.437899        0.0\n",
      "2020-06-08     0.0  142.560251  206.440999        0.0\n",
      "\n",
      "[346 rows x 4 columns]\n"
     ]
    }
   ],
   "source": [
    "# Initialize the short and long windows\n",
    "short_window = 40\n",
    "long_window = 100\n",
    "\n",
    "# Initialize the `signals` DataFrame with the `signal` column\n",
    "signals = pd.DataFrame(index=stock.index)\n",
    "signals['signal'] = 0.0\n",
    "\n",
    "# Create short simple moving average over the short window\n",
    "signals['short_mavg'] = stock['Close'].rolling(window=short_window, min_periods=1, center=False).mean()\n",
    "\n",
    "# Create long simple moving average over the long window\n",
    "signals['long_mavg'] = stock['Close'].rolling(window=long_window, min_periods=1, center=False).mean()\n",
    "\n",
    "# Create signals\n",
    "signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] \n",
    "                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   \n",
    "\n",
    "# Generate trading orders\n",
    "signals['positions'] = signals['signal'].diff()\n",
    "\n",
    "# Print `signals`\n",
    "print(signals)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Import `pyplot` module as `plt`\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Initialize the plot figure\n",
    "fig = plt.figure()\n",
    "\n",
    "# Add a subplot and label for y-axis\n",
    "ax1 = fig.add_subplot(111,  ylabel='Price in $')\n",
    "\n",
    "# Plot the closing price\n",
    "stock['Close'].plot(ax=ax1, color='r', lw=2.)\n",
    "\n",
    "# Plot the short and long moving averages\n",
    "signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)\n",
    "\n",
    "# Plot the buy signals\n",
    "ax1.plot(signals.loc[signals.positions == 1.0].index, \n",
    "         signals.short_mavg[signals.positions == 1.0],\n",
    "         '^', markersize=10, color='m')\n",
    "         \n",
    "# Plot the sell signals\n",
    "ax1.plot(signals.loc[signals.positions == -1.0].index, \n",
    "         signals.short_mavg[signals.positions == -1.0],\n",
    "         'v', markersize=10, color='k')\n",
    "         \n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Define a trailing 252 trading day window\n",
    "window = 200\n",
    "\n",
    "# Calculate the max drawdown in the past window days for each day \n",
    "rolling_max = stock['Adj Close'].rolling(window, min_periods=1).max()\n",
    "daily_drawdown = stock['Adj Close']/rolling_max - 1.0\n",
    "\n",
    "# Calculate the minimum (negative) daily drawdown (orange colour)\n",
    "max_daily_drawdown = daily_drawdown.rolling(window, min_periods=1).min()\n",
    "\n",
    "# Plot the results\n",
    "daily_drawdown.plot()\n",
    "max_daily_drawdown.plot()\n",
    "\n",
    "# Show the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
