# coding: utf-8
import json
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
root=Path(__file__).resolve().parents[1]
a=json.loads((root/'dist/data/posts.json').read_text(encoding='utf-8'))
b=json.loads((root/'dist/data/places.json').read_text(encoding='utf-8'))
assert a['schemaVersion']==b['schemaVersion']=='1.1.0'
ids={p['id'] for p in b['places']}
assert len(ids)==len(b['places'])
assert len({p['id'] for p in a['posts']})==len(a['posts'])
for p in a['posts']:
 for key in ['id','title','category','summary','body','publishedAt','updatedAt','campus','placeIds','sources','contentKind','verification','status','tags','rights','contentType','sourcePeriod','evidenceNote','simulatorUse']:
  assert key in p,(p['id'],key)
 assert p['category'] in ['news','event','meme']
 assert p['campus'] in ['yanchao','heping','university-wide']
 assert p['status']=='published'
 assert (p['contentKind'],p['verification']) in [('fact','verified'),('opinion','opinion'),('fiction','fiction'),('community','source-confirmed'),('source-index','link-only')]
 assert all(x in ids for x in p['placeIds'])
 assert p['body'] and all(isinstance(x,str) for x in p['body'])
 for key in ['publishedAt','updatedAt']:datetime.strptime(p[key],'%Y-%m-%d')
 if p['contentKind'] in ['fact','community','source-index']: assert p['sources']
 assert p['category']!='event','Single-day activities are excluded'
 assert p['contentType'] in ['guide','archive','source-index']
 if p['verification']=='link-only':
  assert p['contentType']=='source-index' and not p['placeIds']
  assert all(s.get('access')=='user-link-only' for s in p['sources'])
 if p['category']=='event':
  for key in ['eventStart','eventEnd','location','registrationDeadline','registrationUrl','registrationStatus']:assert key in p
  assert datetime.fromisoformat(p['eventEnd'])>=datetime.fromisoformat(p['eventStart'])
for item in a['posts']+b['places']:
 for s in item['sources']:
  assert urlparse(s['url']).scheme in ['http','https']
  datetime.strptime(s['accessedAt'],'%Y-%m-%d')
print('PASS:',len(a['posts']),'entries;',len(b['places']),'locations; fields, IDs, dates, references, source indices and no-event policy valid.')
