# eth2-etl
Collect, store and analyze data from prysm client

**Before using it, please start your eth1 node on Prysm first.**

## Function:
### **extract_block:**
#### Usage: 
eth2_etl.py extract_block [OPTIONS]


#### Options:
  _-h, --slot-head_ INTEGER  First slot to extract block  [required] </br>
  _-e, --slot-end_ INTEGER   Last slot to extract block(not included) 
                           [required] </br>
  _--help_                   Show this message and exit. </br>

### **extract_validator:**
#### Usage: 
eth2_etl.py extract_validator [OPTIONS]

#### Options:
  -e, --epoch INTEGER  The epoch to extract validator  [required] </br>
  --help               Show this message and exit.

### **extract_committee**
#### Usage: 
eth2_etl.py extract_committee [OPTIONS]

#### Options:
  -h, --epoch-head INTEGER  First epoch to extract committee  [required] </br>
  -e, --epoch-end INTEGER   Last epoch to extract committee(not included)
                            [required] </br>
  --help                    Show this message and exit. </br>
