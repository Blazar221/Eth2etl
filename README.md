# eth2-etl
Collect, store and analyze data from prysm client

**Before using it, please start your eth1 node on Prysm first.**

## Function:
### **extract_block:**
#### Usage: 
eth2_etl.py extract_block [OPTIONS]


#### Options:
  _-s, --slot_ INTEGER  The slot to extract block  [required] </br>
  _--help_                   Show this message and exit. </br>

### **extract_validator:**
#### Usage: 
eth2_etl.py extract_validator [OPTIONS]

#### Options:
  _-e, --epoch_ INTEGER  The epoch to extract validator  [required] </br>
  _--help_               Show this message and exit.

### **extract_committee**
#### Usage: 
eth2_etl.py extract_committee [OPTIONS]

#### Options:
  _-e, --epoch_ INTEGER  The epoch to extract committee  [required] </br>
  _--help_                    Show this message and exit. </br>
