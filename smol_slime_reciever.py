import starvote
from starvote import hashed_ballots_tiebreaker

tasks = [
    {
        "eByte Dongle (E104-BT5040U) - Cheapest Receiver, free shipping from AliExpress, and has PCB Trace Antenna.": 50, # https://www.aliexpress.com/item/1005004262523219.html
        "Nordic Semiconductor nRF52840 Dongle (PCA10059) - More expensive, not free shipping from Digikey/Mouser, and has PCB Trace Antenna.": 50,
        "SuperMini nRF52840 - Cheapest option, but having a ceramic antenna and your trackers also having a ceramic antenna will reduce signal strength and range.": 50,
        "Seeed Studio XIAO nRF52840 - Expensive option, but having a ceramic antenna and your trackers also having a ceramic antenna will reduce signal strength and range.": 50
    },
    {   # Score by price
        "SuperMini nRF52840 8.47 USD": 90,
        "eByte Dongle (E104-BT5040U) 8.99 USD": 80, 
        "Seeed Studio XIAO nRF52840 9.90 USD": 70,
        "Nordic Semiconductor nRF52840 Dongle (PCA10059) $16.19 USD": 60,
    },
    { # Score by signal strength and range
        "SuperMini nRF52840 having a ceramic antenna and your trackers also having a ceramic antenna will reduce signal strength and range.": 10,
        "Seeed Studio XIAO nRF52840 - Expensive option, but having a ceramic antenna and your trackers also having a ceramic antenna will reduce signal strength and range.": 10,
        "eByte Dongle (E104-BT5040U) - Cheapest Receiver, free shipping from AliExpress, and has PCB Trace Antenna.": 60,
        "Nordic Semiconductor nRF52840 Dongle (PCA10059) - More expensive, not free shipping from Digikey/Mouser, and has PCB Trace Antenna.": 60,
    }
]

seats = 1

results = starvote.election(
    method=starvote.star if seats < 2 else starvote.allocated,
    ballots=tasks,
    seats=seats,
    tiebreaker=hashed_ballots_tiebreaker,
    maximum_score=100,
)

print(results)
# python3 elections/smol_slime_reciever.py 
# ['eByte Dongle (E104-BT5040U) - Cheapest Receiver, free shipping from AliExpress, and has PCB Trace Antenna.']