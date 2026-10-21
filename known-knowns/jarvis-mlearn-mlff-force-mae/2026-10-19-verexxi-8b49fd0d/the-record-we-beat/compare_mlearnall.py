"""cmp_all.py : for each element, take the best-listed model on the mlearnall_<El>_forces page, fetch its published test-multimae predictions
(standard library only), and score them (a) on all structures in that file and (b) on the official test ids of mlearn_<El>_forces."""
import re, io, json, zipfile, urllib.request, sys, hashlib
UA = {'User-Agent': 'V3R1T4S-hunt (research agent)'}
RAW = 'https://raw.githubusercontent.com/usnistgov/jarvis_leaderboard/main/jarvis_leaderboard/'
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()
out = {}
for el in sys.argv[1:] or 'Cu Ge Li Mo Ni Si'.split():
    raw = get(f'https://pages.nist.gov/jarvis_leaderboard/AI/MLFF/mlearnall_{el}_forces/').decode('utf8')
    t = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<script.*?</script>|<style.*?</style>', '', raw, flags=re.S)))
    rows = sorted(re.findall(r'(\S+) mlearnall_' + el + r' ([0-9.eE+-]+) (\S+) (\d+) (\d\d-\d\d-\d{4})', t), key=lambda r: float(r[1]))
    model, listed = rows[0][0], float(rows[0][1])
    bm = json.loads((lambda z: z.read(z.namelist()[0]))(zipfile.ZipFile(io.BytesIO(get(RAW + f'benchmarks/AI/MLFF/mlearn_{el}_forces.json.zip'))))); test = set(bm['test'])
    z = zipfile.ZipFile(io.BytesIO(get(RAW + f'contributions/{model}/AI-MLFF-forces-mlearnall_{el}-test-multimae.csv.zip')))
    name = z.namelist()[0]; lines = z.read(name).decode().strip().splitlines()[1:]
    allr, tr = [], []
    for l in lines:
        i, tg, pr = l.split(',')
        e = [abs(float(a) - float(b)) for a, b in zip(tg.split(';'), pr.split(';'))]
        allr += e
        if i in test: tr += e
    out[el] = dict(model=model, listed=listed, mae_all=sum(allr)/len(allr), n_all=len(lines), mae_on_official_test=sum(tr)/len(tr) if tr else None, n_test=sum(1 for l in lines if l.split(',')[0] in test))
    print(el, out[el])
