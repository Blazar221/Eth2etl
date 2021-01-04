# eth2-etl
Collect, store and analyze data from prysm client

**Before using it, please start your eth1 node on Prysm first. Also, specify the output directory in config.py**

## Function:
### **extract_block:**
extract the blocks of slot as csv to output dir
#### Usage: 
eth2_etl.py extract_block [slot:Integer]


### **extract_validator:**
extract the validator of epoch as csv to output dir
#### Usage: 
eth2_etl.py extract_validator [epoch:Integer]

### **extract_committee**
extract the committee of epoch as csv to output dir
#### Usage: 
eth2_etl.py extract_committee [epoch:Integer]

### **quest_genesis**
quest the genesis information for the current beacon chain
#### Usage: 
eth2_etl.py quest_genesis 

### **quest_chainhead**
quest the chain head information for the current beacon chain
#### Usage: 
eth2_etl.py quest_chainhead

### **check_time**
check whether the current timestamp config is right
#### Usage: 
eth2_etl.py check_time 


