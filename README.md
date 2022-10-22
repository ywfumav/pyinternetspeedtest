# PyInternetSpeedTest

An internet speed test monitor.

## Features

1. Some data are to be saved every 5 minutes.

   - Download speed (Mbps)
   - Upload speed (Mbps)
   - Ping latency (ms)

2. Webpage to display these records.

   - Filter across time, e.g. 1 hour, 10 hours, 1 day, 1 month, 1 year.
   - Graph the records.

3. Data persistency across Raspberry Pi reboots.

## Development Environment

Install a version of Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html).

For ALL the following commands, run inside an Anaconda prompt.

Run the following command to create the conda environment for development.

```bash
conda create -n pyist -c conda-forge python=3.10 speedtest-cli flask
conda activate pyist
```

## Deployment Environment

## Test Data Creation

Test data is required to be created for demonstration of testing.

A test data generation script is created in `data/gen_test_data.py`, which mocks the date of data generation and the triplet of values required in json.
