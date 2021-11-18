`pip install lotusdb`
```python
from lotusdb import Database
db = Database('myfile.db')
db.put({ 'a': 'b' })
print(db.find(lambda x: x['a'] == 'b'))
db.remove(lambda x: x['a'] == 'b')
```
