import starvote
from starvote import hashed_ballots_tiebreaker

tasks = [
    { # all options
        "SuperMini nRF52840 (Cheapest)": 50, # https://www.aliexpress.com/item/1005006019812115.html
        "Seeed Studio XIAO nRF52840 (Smaller, but very expensive)": 50, # https://www.seeedstudio.com/Seeed-XIAO-BLE-nRF52840-p-5201.html
    }, # Score by price
    {
        "SuperMini nRF52840 (Cheapest) US $6.81": 90, # https://www.aliexpress.com/item/1005006019812115.html
        "Seeed Studio XIAO nRF52840 (Smaller, but very expensive) USD $9.90 ": 80, # https://www.seeedstudio.com/Seeed-XIAO-BLE-nRF52840-p-5201.html
    }, # Scope by size
    {
        "SuperMini nRF52840 (Cheapest) US $6.81": 50, # https://www.aliexpress.com/item/1005006019812115.html
        "Seeed Studio XIAO nRF52840 (Smaller, but very expensive) USD $9.90 ": 80, # https://www.seeedstudio.com/Seeed-XIAO-BLE-nRF52840-p-5201.html
    }
]

# "Compatible Inertial Measurement Unit/IMU Breakout Board"
# "BMI270 (IMU Wake on Motion Unfinished)": 10,
# "ICM-42688-P": 50,
# "ICM-42688-V": 50,
# "ICM-45686": 50,
# "ISM330BX": 50,
# "ISM330DHCX": 50,
# "LSM6DSO": 50,
# "LSM6DSR": 50,
# "LSM6DSV": 50,
# "LSM6DSV16B": 50,

# "Compatible Magnetometer (Optional)": 50,
# "AK09940": 50,
# "BMM150 (Not Tested)": 10,
# "BMM350 (Not Tested)": 10,
# "IIS2MDC": 50,
# "IST8306": 50,
# "IST8308": 50,
# "LIS2MDL": 50,
# "LIS3MDL (Not Tested)": 10,
# "MMC5983MA": 50,

# "Push Button/Momentary Switch": 50,

# "Slide Switch - Recommended, but optional": 50,

# "3.7V LiPo Battery": 50

seats = 1

results = starvote.election(
    method=starvote.star if seats < 2 else starvote.allocated,
    ballots=tasks,
    seats=seats,
    tiebreaker=hashed_ballots_tiebreaker,
    maximum_score=100,
)

print(results)
# % python3 elections/smol_slime_tracker.py
# ['Seeed Studio XIAO nRF52840 (Smaller, but very expensive) USD $9.90']