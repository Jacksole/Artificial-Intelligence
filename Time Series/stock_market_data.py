import datetime
import warnings

import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from matplotlib.dates import MonthLocator, YearLocator

from hmmlearn.hmm import GaussianHMM

try:
    from matplotlib.finance import quotes_historical_yahoo_och1
except ImportError:
    from matplotlib.finance import (
        quotes_historical_yahoo as quotes_historical_yahoo_och1)


start_date = datetime.date(1995, 10, 10)
end_date = datetime.date(2015, 4, 25)
quotes = quotes_historical_yahoo_och1('INTC', start_date, end_date)

closing_quotes = np.array([quote[2] for quote in quotes])

volumes = np.array([quote[5] for quote in quotes])[1:]

diff_percentages = 100.0 * np.diff(closing_quotes) / closing_quotes[:-]
dates = np.array([quote[0] for quote in quotes], dtype=np.int)[1:]
training_data = np.column_stack([diff_percentages, volumes])

hmm = GaussianHMM(n_components=7, covariance_type='diag', n_iter=1000)
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    hmm.fit(training_data)

num_samples = 300
samples, _ = hmm.sample(num_samples)

plt.figure()
plt.title('Difference percentages')
plt.plot(np.arange(num_samples), samples[:, 0], c='black')

plt.figure()
plt.title('Volume of shares')
plt.plot(np.arange(num_samples), samples[:, 1], c='black')
plt.ylim(ymin=0)
plt.show()
