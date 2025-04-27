### Donation Points To The Pool
A script to donate points to the pool (even if you don't have em). 
<br>

### Logic
    Sends <HOW_MANY_POINTS> of POST requests to the endpoint at the same time using threads, 
    prevent checking responce .

### UsAGE

 Run:
```bash
python Donation_P42.py <END_POINT> <HOW_MANY_POINTS> <SESSION_ID> # (Check coockies to get the intra 42 session production)
```

### Example
    python3 Donation_P42.py https://profile.intra.42.fr/user_data/175652/give_correction_point?campus_id=16&cursus_slug=42cursus 20 65d6d8704f14d278542ds23s46973201
#### Author :
  TAHA MOUNIR