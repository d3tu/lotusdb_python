from typing import (
  Any,
  Callable
)
from os import (
  path,
  remove,
  rename
)
from ujson import loads
from rapidjson import dumps
class Database:
  def __init__(self, path: str = 'data.db'):
    self.path = path
    if not path.exists(path): 
      with open(path, 'x') as f: f.close()
  def put(self, data: Any) -> None:
    with open(self.path, 'a') as f: f.write(dumps(data, separators=(',', ':')) + '\n'); f.close()
  def find(self, cb: Callable[[Any], bool]) -> Any:
    with open(self.path, 'r') as f:
      r = None
      for l in f:
        j = loads(l)
        try:
          if cb(j): r = j; break
        except: pass
      f.close(); return r
  def remove(self, cb: Callable[[Any], bool]) -> None:
    with open(self.path, 'r') as r, open(self.path + '.bak', 'w') as w:
      o = True
      for l in r:
        try:
          if cb(loads(l)): o = False
          else: o = True
        except: o = True
        if o: w.write(l)
      r.close(); w.close(); remove(self.path); rename(self.path + '.bak', self.path)